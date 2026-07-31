from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

todos = []

class Todo(BaseModel):
    id: int
    title: str
    completed: bool

@app.post("/create_CRUD")
def create_CRUD(todo: Todo):
    todos.append(todo)
    return {
        "message": "Data Added",
        "data": todo
    }

@app.get("/todos")
def read_CRUD():
    return todos

@app.get("/todo/{todo_id}")
def get_todo(todo_id: int):
    for i in todos:
        if i.id == todo_id:
            return i
    return {"message": "todo not found!!"}

@app.put("/todo/{todo_id}")
def update_todo(todo_id: int, updated_todo: Todo):
    for i, j in enumerate(todos):
        if j.id == todo_id:
            todos[i] = updated_todo
            return {
                "message": "todo updated successfully",
                "data": updated_todo
            }
    return {"message": "todo not found!!"}

@app.delete("/todo/{todo_id}")
def delete_todo(todo_id: int):
    for i, j in enumerate(todos):
        if j.id == todo_id:
            deleted_todo = todos.pop(i)
            return {
                "message": "todo deleted successfully",
                "data": deleted_todo
            }
    return {"message": "todo not found!!"}
