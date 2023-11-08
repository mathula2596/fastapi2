from typing import List
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from .. import schemas, database,oauth2
from ..repository import user

router = APIRouter(
    prefix='/user',
    tags=["Users"]
)

@router.post('/')
def create(request: schemas.User, db:Session = Depends(database.dbConnection),current_user:schemas.User = Depends(oauth2.get_current_user)):
   return user.create(db,request)

@router.get('/',response_model=List[schemas.UserShow])
def all(db:Session = Depends(database.dbConnection),current_user:schemas.User = Depends(oauth2.get_current_user)):
   return user.index(db)


@router.get('/{id}',status_code=status.HTTP_200_OK, response_model=schemas.UserShow)
def show(id, db:Session = Depends(database.dbConnection),current_user:schemas.User = Depends(oauth2.get_current_user)):
   return user.show(id,db)

@router.delete('/{id}',status_code=status.HTTP_204_NO_CONTENT)
def destroy(id,db:Session = Depends(database.dbConnection),current_user:schemas.User = Depends(oauth2.get_current_user)):
   return user.delete(id,db)


@router.put('/{id}',status_code=status.HTTP_202_ACCEPTED)
def updates(id, request:schemas.User, db:Session = Depends(database.dbConnection),current_user:schemas.User = Depends(oauth2.get_current_user)):
    return user.update(id,request,db)

