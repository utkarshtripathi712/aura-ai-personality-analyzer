# Yahan server.py ka poora code aayega. Main aage ke liye ek simple placeholder daal raha hoon.
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
app = FastAPI()
@app.get("/api")
def root():
    return {"message": "Aura AI Backend is Running!"}
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])
