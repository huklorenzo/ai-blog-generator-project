from sqlalchemy.orm import Session
from . import models, schemas

def create_blog(db: Session, blog: schemas.BlogCreate):
    db_blog = models.Blog(title=blog.title, body=blog.body)
    db.add(db_blog)
    db.commit()
    db.refresh(db_blog)
    return db_blog

def get_blogs(db: Session):
    return db.query(models.Blog).all()

def delete_blog(db: Session, blog_id: int):
    blog = db.query(models.Blog).filter(models.Blog.id == blog_id).delete()
    if blog:
        db.delete(blog)
        db.commit()
        