# Standard Library
import logging
from typing import List

from fastapi import APIRouter, Request

from datasource.database import db
from models.db_models import ToDoItem

router = APIRouter()
logger = logging.getLogger(__name__)


@router.post("/insert", response_model=ToDoItem, status_code=201)
async def create_todo(request: Request, todo_item: ToDoItem) -> ToDoItem:
    await db.test_coll.replace_one({"id": todo_item.id}, todo_item.__dict__, True)
    return todo_item


@router.get(
    "/listall",
    response_description="List of all To-do items",
    response_model=List[ToDoItem],
)
async def list_todos(request: Request) -> List[ToDoItem]:
    cursor = [doc async for doc in db.test_coll.find()]
    logger.info(f"Got list of all To-Do items with len: {len(cursor)}")
    return cursor


@router.put("/update", response_model=ToDoItem, status_code=201)
async def replace_todo(request: Request, item_with_update: ToDoItem) -> ToDoItem:
    """
    Update an item. Id (which is also the PartitionKey in this case) values should reference the item to be updated:

    - **id**: [Mandatory] Old Item ID
    - **name**: [Optional] The new name.
    - **description**: [Optional] The new description
    - **isComplete**: [Optional] boolean flag to mark a Todo complete or incomplete
    """
    await db.test_coll.replace_one(
        {"id": item_with_update.id}, item_with_update.__dict__, True
    )
    return item_with_update


@router.delete("/delete")
async def delete_todo(request: Request, item_id: str):
    await db.test_coll.delete_one({"id": item_id})
