# Medical-AI-ChatBot

## Overview

Medical-AI-ChatBot is an AI-powered assistant designed to provide users with cures and preventions for medical issues based on user inputs. Built using Hugging Face's advanced Natural Language Processing (NLP) models, the chatbot emphasizes accurate, empathetic, and user-friendly interactions while reminding users to consult healthcare professionals for proper diagnoses and treatment.

## Features

- **Medical Advice**: Provides tailored suggestions for cures and preventions.
- **Hugging Face NLP Models**: Delivers precise and relevant responses to user queries.
- **User-Friendly Interface**: Designed for seamless and intuitive interaction.
- **Accessible 24/7**: Always available to answer medical-related questions.

## Screenshot

![Image](https://github.com/user-attachments/assets/c2816976-f4dc-4d0c-8b1c-c7aa1b308f6c)

*(Replace `path/to/your/screenshot.png` with the actual path to your chatbot image)*

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
2. Open the application in your browser (default: [http://localhost:5000](http://localhost:5000/)).
3. Interact with the chatbot by typing your medical queries in the input box.

## Project Structure

- **`app.py`**: Main application script.
- **`requirements.txt`**: List of required Python packages.
- **`.env`**: Environment file containing sensitive API keys (not included in the repository).

## Key Libraries

- **Hugging Face Transformers**: For NLP model integration.
- **Flask/Streamlit (or your chosen framework)**: For building the user interface.
- **Python-dotenv**: For managing environment variables.

## Important Notes

- This chatbot is designed as a medical assistant but does not provide medical diagnoses or treatment plans.
- Always consult a certified healthcare professional for medical concerns.

## Future Enhancements

- Add support for multilingual queries.
- Enhance context retention for more cohesive responses.
- Incorporate region-specific medical guidelines for better localization.

## License

This project is licensed under the MIT License.

---

Enjoy using Medical-AI-ChatBot and feel free to contribute or report any issues!
