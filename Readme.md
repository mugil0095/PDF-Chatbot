# PDF Chatbot

## Overview

The PDF Chatbot is a conversational agent that allows users to upload a PDF file and interact with its contents through a chat interface. Built using FastAPI and OpenAI's Retrieval-Augmented Generation (RAG) method, this project provides a seamless way to extract and query information from PDF documents.

## Features

- **PDF Upload**: Users can upload a PDF file to the chatbot.
- **Chat Interface**: Users can interact with the PDF contents through a chat interface.
- **Retrieval-Augmented Generation**: Utilizes OpenAI's RAG method for generating responses based on PDF content.
- **API Endpoints**: Provides API endpoints for uploading PDFs and querying the contents.
- **Unit Tests**: Includes unit tests to ensure functionality and reliability.

## Directory Structure

\`\`\`
pdf_chatbot/
├── requirements.txt
├── .pytest_cache/
│   ├── .gitignore
│   ├── CACHEDIR.TAG
│   ├── README.md
│   └── v/
│       └── cache/
│           ├── lastfailed
│           ├── nodeids
│           └── stepwise
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── routes.py
│   ├── sample.py
│   ├── utils.py
│   └── __pycache__/
│       ├── __init__.cpython-311.pyc
│       ├── main.cpython-311.pyc
│       ├── routers.cpython-311.pyc
│       ├── routes.cpython-311.pyc
│       └── utils.cpython-311.pyc
└── tests/
    ├── __init__.py
    ├── sample_assignment.pdf
    ├── test_main.py
    └── __pycache__/
        ├── __init__.cpython-311.pyc
        └── test_main.cpython-311-pytest-8.3.1.pyc
\`\`\`

## Installation

1. **Clone the repository**:
   \`\`\`bash
   git clone https://github.com/yourusername/pdf_chatbot.git
   cd pdf_chatbot
   \`\`\`

2. **Create a virtual environment**:
   \`\`\`bash
   python3 -m venv venv
   source venv/bin/activate
   \`\`\`

3. **Install the dependencies**:
   \`\`\`bash
   pip install -r requirements.txt
   \`\`\`

## Running the Application

1. **Navigate to the \`app\` directory**:
   \`\`\`bash
   cd app
   \`\`\`

2. **Start the FastAPI server**:
   \`\`\`bash
   uvicorn main:app --reload
   \`\`\`

3. **Open your browser** and go to \`http://127.0.0.1:8000/docs\` to view the interactive API documentation.

## API Endpoints

- **Upload PDF**: 
  - \`POST /upload_pdf\`
  - Upload a PDF file to the chatbot.

- **Query PDF**: 
  - \`POST /query_pdf\`
  - Send a query to the chatbot to retrieve information from the uploaded PDF.

## Unit Tests

1. **Navigate to the root directory**:
   \`\`\`bash
   cd ..
   \`\`\`

2. **Run the tests**:
   \`\`\`bash
   pytest
   \`\`\`

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

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Contact

For any questions or support, please contact [your email](mailto:youremail@example.com).
