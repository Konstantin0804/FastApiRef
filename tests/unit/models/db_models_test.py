from models.db_models import ToDoItem


def test_validate_todo_data():
    valid_todo_data = {
        "id": "2",
        "name": "John",
        "description": "nope",
        "is_complete": True,
    }

    valid_todo_object = ToDoItem(**valid_todo_data)

    assert ToDoItem.model_validate(valid_todo_data)
    assert valid_todo_object.id == valid_todo_data["id"]
