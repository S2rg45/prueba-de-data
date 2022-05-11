from fastapi import FastAPI
import model
from config import engine
import router

model.base.metadata.create_all(bind=engine)


app = FastAPI()


@app.get('/')
async def Home():
  return "Welcome"


app.include_router(router.router, prefix="/data", tags=["data"])