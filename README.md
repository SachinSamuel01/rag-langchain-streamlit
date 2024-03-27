# RAG Langchain Streamlit Chatbot

## Overview
This project is a web-based AI chatbot an implementation of the Retrieval-Augmented Generation (RAG) model, built using Streamlit and Langchain. It answers questions relevant to the data provided by the user. The chatbot utilizes OpenAI's GPT-4 model and accepts data in CSV format. Users can upload multiple CSV files, clear uploaded files, ask questions, and view responses through a Streamlit interface.

## Features
- Data Upload: Users can upload multiple CSV files containing the data they want the chatbot to learn from.
- Clear Data: Users can clear all previously uploaded files, allowing the model to learn from new files.
- Ask Questions: Users can ask questions related to the uploaded data, and the chatbot will generate responses based on its understanding of the data.

## Installation
To run this project, you will need Python and the necessary packages. Follow these steps to set up the environment:

Clone the repository:
```bash
git clone https://github.com/yourusername/rag-langchain-streamlit.git
cd rag-langchain-streamlit
```

Create and activate a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

Install the required packages:
```bash
pip install -r requirements.txt
```

Set up your OpenAI API key in a .env file:
```bash
OPENAI_API_KEY=your_api_key_here
```

## Usage
To start the Streamlit app, run the following command in your terminal:
```bash
streamlit run Langchain_streamlit.py
```

Then, follow the instructions on the web interface to upload CSV files, ask questions, and view responses.
