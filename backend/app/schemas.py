from pydantic import BaseModel

class BlogCreate(BaseModel):
    title: str
    body: str

class Blog(BlogCreate):
    id: int

    class Config:
        orm_mode = True