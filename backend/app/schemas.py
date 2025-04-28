from pydantic import BaseModel

class BlogCreate(BaseModel):
    title: str
    body: str

class Blog(BlogCreate):
    id: int

    model_config = {
        "from_attributes": True
    }