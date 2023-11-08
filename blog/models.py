
from sqlalchemy import Column, ForeignKey, Integer, String
from .database import Base
from sqlalchemy.orm import relationship



class Blog(Base):
    __tablename__ = "blog"
    
    id = Column(Integer,primary_key=True, index=True)
    title = Column(String(255))
    body =  Column(String(255))
    user_id = Column(Integer, ForeignKey("user.id"))
      
    creators = relationship("User", back_populates="blogs")
    

class User(Base):
    __tablename__ = "user"
    
    id = Column(Integer,primary_key=True, index=True)
    name = Column(String(255))
    email =  Column(String(255))
    mobile = Column(String(255))   
    password = Column(String(255))       
    
    blogs = relationship("Blog", back_populates="creators")
        
 
    
    
         
