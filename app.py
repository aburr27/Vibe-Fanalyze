from fastapi import FastAPI
from dotenv import load_dotenv
import os

# Load env variables
load_dotenv()

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Vibe-Fanalyze is live!"}
