
from pydantic import BaseModel

# from schemas.user import UserShow
# from .schemas import UserBase


class Blog(BaseModel):
    title:str
    body:str
   
class User(BaseModel):
    name:str
    email:str
    password:str
    mobile:str
    
# class UserBase(User):
#     id:int
#     class config:
#         orm_mode = True
    
class UserShow(BaseModel):
    name:str
    email:str
    mobile:str
    blogs:list[Blog]
    
    class config:
        orm_mode = True
        
class BlogShow(BaseModel):
    title:str
    body:str
    creators:User
    
    class config:
        orm_mode = True
        
class Login(BaseModel):
    username:str
    password:str
    
class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str | None = None