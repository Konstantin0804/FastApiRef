from fastapi import FastAPI
from contextlib import asynccontextmanager
from datasource.database import db
from api.auxiliary import router as todo_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    records_count = db.list_collection_names()
    print(records_count)
    yield


app = FastAPI(
    lifespan=lifespan,
    title='train',
    version='0.0.1'
)

app.include_router(todo_router, tags=["todos"], prefix="/todos")
