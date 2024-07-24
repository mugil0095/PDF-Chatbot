import os
import logging
from fastapi import APIRouter, UploadFile, File, HTTPException, Form
from fastapi.responses import HTMLResponse
from io import BytesIO
from PyPDF2 import PdfReader
from transformers import pipeline

# Initialize logger
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

router = APIRouter()

# Load environment variables
from dotenv import load_dotenv
load_dotenv()

# Initialize text generation pipeline
qa_pipeline = pipeline("question-answering", model="deepset/roberta-base-squad2")

content_storage = {}
last_uploaded_filename = None

@router.post("/upload/")
async def upload_pdf(file: UploadFile = File(...)):
    global last_uploaded_filename
    filename = file.filename
    contents = await file.read()

    # Convert PDF contents to text
    pdf_reader = PdfReader(BytesIO(contents))
    text = ""
    for page in range(len(pdf_reader.pages)):
        text += pdf_reader.pages[page].extract_text()

    # Store the PDF content
    content_storage[filename] = text
    last_uploaded_filename = filename
    return {"filename": filename, "text": text}

@router.post("/query/")
async def query_pdf(question: str = Form(...)):
    logger.info(f"Received query - Question: {question}")

    if not last_uploaded_filename or last_uploaded_filename not in content_storage:
        raise HTTPException(status_code=404, detail="No PDF content found.")

    context = content_storage[last_uploaded_filename]

    # Generate response using the text generation pipeline
    try:
        result = qa_pipeline(question=question, context=context)
        answer = result['answer']
    except Exception as e:
        logger.error(f"Error generating answer: {e}")
        raise HTTPException(status_code=500, detail="Error generating answer.")

    return {"answer": answer}

@router.get("/")
async def read_root():
    return {"message": "Hello World"}

@router.get("/upload_form", response_class=HTMLResponse)
async def upload_form():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>PDF Chatbot</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f4f4f9;
                color: #333;
                margin: 0;
                padding: 0;
                display: flex;
                flex-direction: column;
                align-items: center;
            }
            h1 {
                margin-top: 20px;
                color: #007bff;
            }
            .container {
                width: 80%;
                max-width: 900px;
                margin: 20px auto;
                background: #fff;
                border-radius: 8px;
                box-shadow: 0 0 10px rgba(0,0,0,0.1);
                padding: 20px;
            }
            form {
                display: flex;
                flex-direction: column;
                gap: 10px;
            }
            input[type="file"], input[type="text"], input[type="submit"] {
                padding: 10px;
                border: 1px solid #ddd;
                border-radius: 4px;
            }
            input[type="file"] {
                font-size: 16px;
            }
            textarea {
                width: 100%;
                padding: 10px;
                border: 1px solid #ddd;
                border-radius: 4px;
                font-size: 16px;
                resize: vertical;
            }
            .btn {
                background-color: #007bff;
                color: #fff;
                border: none;
                cursor: pointer;
                padding: 10px;
                border-radius: 4px;
                font-size: 16px;
                transition: background-color 0.3s;
            }
            .btn:hover {
                background-color: #0056b3;
            }
            .answer {
                padding: 10px;
                background-color: #e9ecef;
                border: 1px solid #ddd;
                border-radius: 4px;
            }
            .error {
                color: #dc3545;
                font-size: 14px;
            }
        </style>
        <script>
            let lastUploadedFilename = null;

            async function handleUpload(event) {
                event.preventDefault();
                const formData = new FormData(event.target);
                const response = await fetch('/upload/', {
                    method: 'POST',
                    body: formData
                });
                const result = await response.json();
                if (response.ok) {
                    lastUploadedFilename = result.filename;
                    document.getElementById('pdf-text').textContent = result.text;
                } else {
                    document.getElementById('error-message').textContent = 'Error uploading PDF.';
                }
            }

            async function handleQuery(event) {
                event.preventDefault();
                if (!lastUploadedFilename) {
                    alert("Please upload a PDF file first.");
                    return;
                }
                const formData = new FormData(event.target);
                const response = await fetch('/query/', {
                    method: 'POST',
                    body: formData
                });
                const result = await response.json();
                if (response.ok) {
                    document.getElementById('query-answer').textContent = result.answer;
                } else {
                    document.getElementById('query-answer').textContent = 'Error querying PDF.';
                }
            }
        </script>
    </head>
    <body>
        <div class="container">
            <h1>Upload PDF and Chat with It</h1>
            <form id="upload-form" onsubmit="handleUpload(event)">
                <input type="file" name="file" required>
                <input type="submit" value="Upload" class="btn">
                <div id="error-message" class="error"></div>
            </form>
            <br>
            <textarea id="pdf-text" rows="10" readonly></textarea>
            <br>
            <form id="query-form" onsubmit="handleQuery(event)">
                <input type="text" name="question" placeholder="Ask a question" required>
                <input type="submit" value="Ask" class="btn">
            </form>
            <br>
            <div id="query-answer" class="answer"></div>
        </div>
    </body>
    </html>
    """
