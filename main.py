# Standard Library
import logging.config
from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI

from api.auxiliary import router as todo_router
from datasource.database import db

logging.config.fileConfig("logging.conf", disable_existing_loggers=False)
logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    db.list_collection_names()
    logger.info(f"FastAPI started with MongoDB connection")
    yield


app = FastAPI(lifespan=lifespan, title="train", version="0.0.1")

app.include_router(todo_router, tags=["todos"], prefix="/todos")

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
