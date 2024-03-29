from dotenv import load_dotenv

from fastapi import FastAPI
from contextlib import asynccontextmanager
from datasource.database import db
from api.auxiliary import router as todo_router


load_dotenv()

@asynccontextmanager
async def lifespan(app: FastAPI):
    db.list_collection_names()
    yield


app = FastAPI(
    lifespan=lifespan,
    title='train',
    version='0.0.1'
)

app.include_router(todo_router, tags=["todos"], prefix="/todos")
