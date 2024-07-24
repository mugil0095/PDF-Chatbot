from dotenv import load_dotenv
import os
from fastapi import FastAPI
from app.routes import router as pdf_router

load_dotenv()

app = FastAPI()

app.include_router(pdf_router)

@app.get("/")
async def read_root():
    return {"message": "Hello World"}
