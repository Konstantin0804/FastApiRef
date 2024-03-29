# Standard Library
from typing import Optional

from pydantic import BaseModel


class ToDoItem(BaseModel):
    id: str
    name: Optional[str]
    description: Optional[str]
    is_complete: Optional[bool]
