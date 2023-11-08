from datetime import timedelta
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestFormStrict
from sqlalchemy.orm import Session
from blog import schemas, database, models, token
from blog.hasing import Hash


router = APIRouter(
    prefix="/login",
    tags=["Authentication"]
)

@router.post("/")
def login(request:OAuth2PasswordRequestFormStrict = Depends(), db:Session = Depends(database.dbConnection)):
    user = db.query(models.User).filter(request.username==models.User.email).first()
    
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid Username",headers={"WWW-Authenticate": "Bearer"})
    
    if not Hash.verify(user.password,request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Invalid Password",headers={"WWW-Authenticate": "Bearer"})
    
    access_token = token.create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}
    
    # return user