from fastapi import FastAPI

from pydantic import BaseModel


app = FastAPI();


todos=[];

class Todo(BaseModel):
    id:int;
    title:str;
    completed:bool;

@app.post("/crete_CRUD")
def crete_CRUD(todo:Todo):
    todos.append(todo)
    return {
        "message":"Data Added",
        "data":todo
    }


@app.get("/todos")
def read_CRUD():
    return todos



@app.get("/todo/{todo_id}")
def get_todo(todo_id:int):
    for i in todos:
        if (i.id == todo_id):
            return i
    return {"message:todo not found!!"}


@app.put("/todo/{todo_id}")
def update_todo(todo_id:int,updated_todo:Todo):
    for i ,j in enumerate(todos):
        if(j.id == todo_id ):
            todos[i]=updated_todo;
            return {"message":"todo  found!!",
                    "data": updated_todo
                    }
    return {"message:todo not found!!"}
