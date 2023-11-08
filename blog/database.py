from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("mysql+mysqldb://root:@localhost:3306/fastapi",echo=True)

SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)

Base = declarative_base()

def dbConnection():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()



