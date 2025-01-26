# Medical-AI-ChatBot

## Overview

Medical-AI-ChatBot is an AI-powered assistant designed to provide users with cures and preventions for medical issues based on user inputs. Built using Hugging Face's advanced Natural Language Processing (NLP) models, the chatbot emphasizes accurate, empathetic, and user-friendly interactions while reminding users to consult healthcare professionals for proper diagnoses and treatment.

## Features

- Personalized Medical Suggestions: Tailored advice for cures and preventions based on user inputs.
- Hugging Face FAISS: Leverages fast, scalable similarity search for precise and context-aware responses.
- Streamlit Interface: Clean, interactive, and easy-to-use user interface.
- 24/7 Accessibility: Always available to address medical-related queries.

## Screenshot

![Image](https://github.com/user-attachments/assets/c2816976-f4dc-4d0c-8b1c-c7aa1b308f6c)



## Prerequisites

To run Medical-AI-ChatBot locally, ensure you have the following:

- Python 3.8+
- A valid Hugging Face API key in the `.env` file
- Libraries specified in `requirements.txt`

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/Medical-AI-ChatBot.git
   cd Medical-AI-ChatBot
   ```
2. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Set up your environment variables by creating a `.env` file in the root directory:
   ```env
   HUGGINGFACE_API_KEY=your_hugging_face_api_key_here
   ```

## Usage

1. Run the application:
   ```bash
   python app.py
   ```
2. Open the application in your browser (default: (http://localhost:8501/)).
3. Interact with the chatbot by typing your medical queries in the input box.

## Project Structure

- app.py: Main Streamlit application script.
- requirements.txt: List of required Python libraries.
- .env: Environment variables file (excluded from version control).
- models/: Directory for storing FAISS-related models or data.


## Key Libraries

- **Hugging Face Transformers**: For NLP model integration.
- **Streamlit **: For building the user interface.
- **Python-dotenv**: For managing environment variables.

## Important Notes

- This chatbot is designed as a medical assistant but does not provide medical diagnoses or treatment plans.
- Always consult a certified healthcare professional for medical concerns.

## Future Enhancements

- Support for multilingual queries.
- Improved context retention for extended conversations.
- Integration of region-specific medical guidelines.


## License

This project is licensed under the MIT License.

---

Enjoy using Medical-AI-ChatBot and feel free to contribute or report any issues!
