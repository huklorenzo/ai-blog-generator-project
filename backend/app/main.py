from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import crud, models, schemas
from .database import SessionLocal, engine
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os

import openai
from openai import OpenAI
from dotenv import load_dotenv
import os

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# CORS (so React frontend can connect)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

load_dotenv()  # Load environment variables from .env

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/ping")
def ping():
    return {"message": "pong"}

@app.post("/generate", response_model=schemas.Blog)
async def generate_blog(topic: str, db: Session = Depends(get_db)):
    prompt = f"Write a detailed blog post about {topic}."

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful blog writing assistant."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=500,
        temperature=0.7,
    )

    content = response.choices[0].message.content.strip()

    blog = schemas.BlogCreate(title=topic, content=content)
    return crud.create_blog(db, blog)

@app.get("/blogs", response_model=list[schemas.Blog])
async def read_blogs(db: Session = Depends(get_db)):
    return crud.get_blogs(db)

@app.delete("/blogs/{blog_id}")
async def delete_blog(blog_id: int, db: Session = Depends(get_db)):
    crud.delete_blog(db=db, blog_id=blog_id)
    return {"message": "Blog deleted"}