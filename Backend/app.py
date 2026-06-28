from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from generator import generate_branding

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class StartupInput(BaseModel):
    description: str

@app.get("/")
def home():
    return {
        "message": "AI Startup Branding Generator Backend Running"
    }

@app.post("/generate")
def generate(data: StartupInput):
    return generate_branding(data.description)