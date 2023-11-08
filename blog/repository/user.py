from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from .. import models, schemas
from ..hasing import Hash

def create(db:Session,request:schemas.User):
    new_user = models.User(
        name = request.name,
        email=request.email,
        password=Hash.bcrypt(request.password),
        mobile=request.mobile
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

def index(db:Session):
    users = db.query(models.User).all()
    return users

def show(id,db:Session):
    user = db.query(models.User).filter(models.User.id==id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No data found")
    return user

def delete(id,db:Session):
    users = db.query(models.User).filter(models.User.id == id)
    if not users.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Not found")
    
    users.delete(synchronize_session=False)
    db.commit()
    return 'delete'

def update(id,db:Session,request:schemas.User):
    users = db.query(models.User).filter(models.User.id == id)
    if not users.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Not found")
    
           
    db.query(models.User).filter(models.User.id==id).update(
        {
            "name": request.name,
            "email": request.email,
            "mobile": request.mobile,
            "password": Hash.bcrypt(request.password)
        }
    )
    db.commit()
    return 'users'