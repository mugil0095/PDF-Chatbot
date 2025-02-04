# PDF Chatbot

## Overview

The PDF Chatbot is a conversational agent that allows users to upload a PDF file and interact with its contents through a chat interface. Built using FastAPI and OpenAI's Retrieval-Augmented Generation (RAG) method with the `deepset/roberta-base-squad2` 
 model, this project provides a seamless way to extract and query information from PDF documents.

## Features

- **PDF Upload**: Users can upload a PDF file to the chatbot.
- **Chat Interface**: Users can interact with the PDF contents through a chat interface.
- **Retrieval-Augmented Generation**: Utilizes OpenAI's RAG method for generating responses based on PDF content.
- **API Endpoints**: Provides API endpoints for uploading PDFs and querying the contents.
- **Unit Tests**: Includes unit tests to ensure functionality and reliability.

## deepset/roberta-base-squad2

The `deepset/roberta-base-squad2` model is a fine-tuned version of RoBERTa for the SQuAD2.0 dataset (Stanford Question Answering Dataset). It excels in reading comprehension tasks by answering questions based on given context. The model is particularly adept at handling unanswerable questions, making it a robust choice for document querying systems.

- **Model**: RoBERTa-base
- **Dataset**: SQuAD2.0
- **Use Case**: Reading comprehension, Question Answering

In this project, `deepset/roberta-base-squad2` is used to generate accurate and contextually relevant responses based on the content of uploaded PDF documents.

## Directory Structure

```
pdf_chatbot/
├── requirements.txt
├── Readme.md
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── routes.py
│   ├── sample.py
│   └── utils.py
└── tests/
    ├── __init__.py
    ├── sample_assignment.pdf
    └──test_main.py
```

## Installation

1. **Clone the repository**:
   ```
   git clone https://github.com/mugil0095/PDF-Chatbot.git
   cd pdf_chatbot
   ```

2. **Create a virtual environment**:
   ```
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install the dependencies**:
   ```
   pip install -r requirements.txt
   ```

## Running the Application

1. **Navigate to the \`app\` directory**:
   ```
   cd app
   ```

2. **Start the FastAPI server**:
   ```
   uvicorn main:app --reload
   ```

3. **Open your browser** go to `http://127.0.0.1:8000/upload_form` for the API and go to `http://127.0.0.1:8000/docs` to view the interactive API documentation.

## API Endpoints

- **Upload PDF**: 
  - \`POST /upload_pdf\`
  - Upload a PDF file to the chatbot.

- **Query PDF**: 
  - \`POST /query_pdf\`
  - Send a query to the chatbot to retrieve information from the uploaded PDF.

## Unit Tests

1. **Navigate to the root directory**:
   ```
   cd testsfolderpath
   ```

2. **Run the tests**:
   ```
   pytest
   ```

## File Descriptions

- **requirements.txt**: Contains the list of dependencies required for the project.
- **app/__init__.py**: Initializes the FastAPI app.
- **app/main.py**: Main entry point for the FastAPI application.
- **app/routes.py**: Defines the API endpoints and their corresponding handlers.
- **app/sample.py**: Example module (can be modified or removed based on the actual implementation).
- **app/utils.py**: Utility functions used across the application.
- **tests/__init__.py**: Initializes the test module.
- **tests/sample_assignment.pdf**: Sample PDF used for testing.
- **tests/test_main.py**: Contains unit tests for the application.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request or open an Issue for any bugs or feature requests.

## License

This project is Open Source and can be updated in the future. 

## Contact

For any questions or support, don't hesitate to contact [your email](Ilamugil.balasubramaniam1@gmail.com).
