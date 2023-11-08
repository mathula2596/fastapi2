from typing import List
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from .. import schemas,database, oauth2
from ..repository import blog

router = APIRouter(
    prefix="/blog",
    tags=["Blogs"]
)

@router.post('/')
def create(request: schemas.Blog, db:Session = Depends(database.dbConnection),current_user:schemas.User = Depends(oauth2.get_current_user)):
    return blog.create(request,db)
   

@router.get('/', response_model=List[schemas.BlogShow])
def all(db:Session = Depends(database.dbConnection), current_user:schemas.User = Depends(oauth2.get_current_user)):
    return blog.index(db)


@router.get('/{id}',status_code=status.HTTP_200_OK, response_model=schemas.BlogShow)
def show(id, db:Session = Depends(database.dbConnection),current_user:schemas.User = Depends(oauth2.get_current_user)):
  return blog.show(id,db)

@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT)
def destroy(id,db:Session = Depends(database.dbConnection),current_user:schemas.User = Depends(oauth2.get_current_user)):
    return destroy(id,db)


@router.put('/{id}',status_code=status.HTTP_202_ACCEPTED,)
def updates(id, request:schemas.Blog, db:Session = Depends(database.dbConnection),current_user:schemas.User = Depends(oauth2.get_current_user)):
   return blog.update(id,db,request)

