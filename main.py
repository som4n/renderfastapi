from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

app = FastAPI()

# Pydantic model for TODO item
class TodoItem(BaseModel):
    id: Optional[int] = None
    title: str
    description: str
    completed: bool = False
    created_at: datetime = datetime.now()


# In-memory storage for todos 

todos = []
current_id = 1

@app.get("/", response_class=HTMLResponse)
async def root():
    return """
    <h1>Welcome to the Todo API</h1>
    <p>Use the <a href="/docs">Swagger Docs</a> to try it out.</p>
    """

@app.get("/todos", response_model=List[TodoItem])
def get_todos():
    return todos

@app.get("/todos/{todo_id}", response_model=TodoItem)
def get_todo(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            return todo
    raise HTTPException(status_code=404, detail="Todo not found")

@app.post("/todos", response_model=TodoItem)
def create_todo(todo: TodoItem):
    global current_id
    todo.id = current_id
    current_id += 1
    todos.append(todo)
    return todo

@app.put("/todos/{todo_id}", response_model=TodoItem)
def update_todo(todo_id: int, updated_todo: TodoItem):
    for i, todo in enumerate(todos):
        if todo.id == todo_id:
            updated_todo.id = todo_id
            todos[i] = updated_todo
            return updated_todo
    raise HTTPException(status_code=404, detail="Todo not found")

@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    for i, todo in enumerate(todos):
        if todo.id == todo_id:
            todos.pop(i)
            return {"message": "Todo deleted successfully"}
    raise HTTPException(status_code=404, detail="Todo not found")
    