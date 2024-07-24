# tests/test_main.py
import pytest
from fastapi.testclient import TestClient
from app.main import app  # Ensure app is imported from the correct path

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}

def test_upload_pdf():
    # You may want to use a small sample PDF file for testing
    with open("tests/sample_assignment.pdf", "rb") as file:
        response = client.post("/upload/", files={"file": ("sample_assignment.pdf", file, "application/pdf")})
        assert response.status_code == 200
        assert "filename" in response.json()
        assert "text" in response.json()

def test_query_pdf():
    # First, upload a PDF file to ensure there is content
    with open("tests/sample_assignment.pdf", "rb") as file:
        client.post("/upload/", files={"file": ("sample_assignment.pdf", file, "application/pdf")})

    # Now query the uploaded PDF
    response = client.post("/query/", data={"question": "What is the main topic of the document?"})
    assert response.status_code == 200
    assert "answer" in response.json()

