from fastapi import FastAPI
from blog import  models
from blog.database import engine
from blog.routers import blog, user, authentication
# from blog.routers import blog, user
models.Base.metadata.create_all(engine)



app = FastAPI()

app.include_router(blog.router)
app.include_router(user.router)
app.include_router(authentication.router)



@app.get("/")
def read_root():
    return {"Hello": "World"}
