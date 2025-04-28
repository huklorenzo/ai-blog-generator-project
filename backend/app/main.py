import openai
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import crud, models, schemas
from .database import SessionLocal, engine
from fastapi.middleware.cors import CORSMiddleware

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

openai.api_key = ""

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
    prompt = f"Write a blog post about {topic}"
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        max_tokens=500,
    )
    
    content = response.choices[0]["text"]
    blog = schemas.BlogCreate(title=topic, body=content)
    return crud.create_blog(db=db, blog=blog)

@app.post("/blogs/", response_model=list[schemas.Blog])
async def read_blogs(db: Session = Depends(get_db)):
    return crud.get_blogs(db=db)

@app.delete("/blogs/{blog_id}")
async def delete_blog(blog_id: int, db: Session = Depends(get_db)):
    crud.delete_blog(db=db, blog_id=blog_id)
    return {"message": "Blog deleted"}