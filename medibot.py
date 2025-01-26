import re
import os
import time
import streamlit as st
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.chains import RetrievalQA
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate
from langchain.llms import HuggingFaceEndpoint  

DB_FAISS_PATH = "vectorstore/db_faiss"

# Cache the vector store loading process to avoid redundant calls.
@st.cache_resource
def get_vectorstore():
    embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    try:
        db = FAISS.load_local(
            DB_FAISS_PATH,
            embedding_model,
            allow_dangerous_deserialization=True
        )
        return db
    except Exception as e:
        st.error(f"Failed to load vector store: {str(e)}")
        return None

# Set up the custom prompt.
def set_custom_prompt(custom_prompt_template):
    prompt = PromptTemplate(
        template=custom_prompt_template,
        input_variables=["context", "question"]
    )
    return prompt

# Load LLM once during the session.
def load_llm(huggingface_repo_id, HF_TOKEN):
    try:
        llm = HuggingFaceEndpoint(
            repo_id=huggingface_repo_id,
            temperature=0.5,
            model_kwargs={
                "token": HF_TOKEN,
                "max_length": 512
            }
        )
        return llm
    except Exception as e:
        st.error(f"Failed to load LLM: {str(e)}")
        return None

# Main function to handle the UI and logic flow.
def main():
    st.title("Ask Chatbot!")

    # Initialize session state if not already initialized.
    if 'message' not in st.session_state:
        st.session_state.message = []

    # Initialize the vectorstore and LLM if not already done.
    if 'vectorstore' not in st.session_state:
        st.session_state.vectorstore = get_vectorstore()
        if st.session_state.vectorstore is None:
            st.error("Failed to load the vector store")
            return

    if 'llm' not in st.session_state:
        HUGGINGFACE_REPO_ID = "mistralai/Mistral-7B-Instruct-v0.3"
        HF_TOKEN = os.environ.get("HF_TOKEN")
        st.session_state.llm = load_llm(huggingface_repo_id=HUGGINGFACE_REPO_ID, HF_TOKEN=HF_TOKEN)
        if st.session_state.llm is None:
            st.error("Failed to load the LLM")
            return

    # Display all messages.
    for message in st.session_state.message:
        st.chat_message(message['role']).markdown(message['content'])

    # Capture user input.
    prompt = st.chat_input("Pass your prompt here")

    if prompt:
        # Display user message.
        st.chat_message('user').markdown(prompt)
        st.session_state.message.append({'role': 'user', 'content': prompt})

        # Check if the query has already been processed before making a new request
        if prompt not in st.session_state.get("responses_cache", {}):
            # Define the custom prompt template.
            CUSTOM_PROMPT_TEMPLATE = """
            Use the pieces of information provided in the context to answer the user's question.
            If you don't know the answer, just say that you don't know. Don't try to make up an answer.
            Don't provide anything outside the given context.

            Context: {context}
            Question: {question}

            Start the answer directly. No small talk, please.
            """
            
            # Add a small delay to avoid hitting the API rate limit
            #time.sleep(2)  # Sleep for 2 seconds debugging

            try:
                # Initialize the retrieval QA chain if not already done.
                qa_chain = RetrievalQA.from_chain_type(
                    llm=st.session_state.llm,
                    chain_type="stuff",
                    retriever=st.session_state.vectorstore.as_retriever(search_kwargs={"k": 3}),
                    return_source_documents=True,
                    chain_type_kwargs={
                        "prompt": set_custom_prompt(CUSTOM_PROMPT_TEMPLATE)
                    }
                )

                # Perform the query to get a response.
                response = qa_chain.invoke({"query": prompt})
                result = response["result"]

                #source_documents = response["source_documents"]    #Debugging
            
                # Split the text at numbers followed by a period
                result_to_show = re.sub(r'(\d+\.)', r'\n\1', result).strip()

                # Cache the response for this query to avoid repeating the request.
                if "responses_cache" not in st.session_state:
                    st.session_state.responses_cache = {}
                st.session_state.responses_cache[prompt] = result_to_show

                # Display the assistant's response.
                st.chat_message('assistant').markdown(result_to_show)
                st.session_state.message.append({'role': 'assistant', 'content': result_to_show})

            except Exception as e:
                st.error(f"Error: {str(e)}")
        else:
            # If the query was previously answered, use the cached response.
            cached_response = st.session_state.responses_cache[prompt]
            st.chat_message('assistant').markdown(cached_response)
            st.session_state.message.append({'role': 'assistant', 'content': cached_response})

if __name__ == "__main__":
    main()
