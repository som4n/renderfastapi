from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.responses import HTMLResponse
from fastapi.security import OAuth2PasswordRequestForm
from typing import List, Optional
from datetime import datetime, timedelta
from auth import (
    User, Token, authenticate_user, create_access_token,
    get_current_user, ACCESS_TOKEN_EXPIRE_MINUTES, users_db
)

app = FastAPI(
    title="Todo API",
    description="""A secure Todo API with user authentication.
    
    ## Features
    * User registration and authentication
    * JWT token-based security
    * CRUD operations for todo items
    * Per-user todo management
    
    ## Authentication
    * Register a new user at `/register`
    * Get your access token at `/token`
    * Use the token in the Authorization header for protected endpoints
    
    ## Todo Operations
    All todo operations require authentication.
    * Create new todos
    * List your todos
    * Update existing todos
    * Delete todos
    """,
    version="2.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

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


# User registration
@app.post("/register", response_model=User, tags=["auth"])
async def register(username: str, password: str, email: Optional[str] = None):
    """Register a new user.
    
    - **username**: Unique username
    - **password**: Strong password
    - **email**: Optional email address
    """
    if username in users_db:
        raise HTTPException(
            status_code=400,
            detail="Username already registered"
        )
    hashed_password = get_password_hash(password)
    user_dict = {
        "username": username,
        "hashed_password": hashed_password,
        "email": email,
        "disabled": False
    }
    users_db[username] = user_dict
    return user_dict

@app.post("/token", response_model=Token, tags=["auth"])
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    """Get access token.
    
    Use your username and password to get an access token.
    This token is required for all protected endpoints.
    """
    user = authenticate_user(users_db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

# Protected todo endpoints
@app.get("/todos", response_model=List[TodoItem], tags=["todos"])
def get_todos(current_user: User = Depends(get_current_user)):
    """Get all todos for the current user."""
    return [todo for todo in todos if todo.owner_id == current_user.username]

@app.post("/todos", response_model=TodoItem, tags=["todos"])
def create_todo(todo: TodoItem, current_user: User = Depends(get_current_user)):
    """Create a new todo for the current user.
    
    - **title**: Todo title (required)
    - **description**: Detailed description
    - **completed**: Todo status (default: false)
    """
    todo.owner_id = current_user.username
    todo.id = len(todos) + 1
    todos.append(todo)
    return todo
    