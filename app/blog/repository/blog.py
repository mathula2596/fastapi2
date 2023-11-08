from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from blog import models, schemas

def create(request:schemas.Blog,db:Session):
    new_blog = models.Blog(
        title = request.title,
        body = request.body,
        user_id = 1
    )
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def index(db:Session):
    blogs = db.query(models.Blog).all()
    return blogs

def show(id,db:Session):
    blog = db.query(models.Blog).filter(models.Blog.id==id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No data found")
    return blog 

def destroy(id,db:Session):
    blogs = db.query(models.Blog).filter(models.Blog.id == id)
    if not blogs.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Not found")
    
    blogs.delete(synchronize_session=False)
    db.commit()
    return 'delete'

def update(id,db:Session,request:schemas.Blog):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Not found")
    
           
    db.query(models.Blog).filter(models.Blog.id==id).update(
        {
            "title": request.title,
            "body": request.body,
          
        }
    )
    db.commit()
    return 'blog updated'