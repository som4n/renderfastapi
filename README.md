# 📝 FastAPI Todo API with Authentication

A secure and feature-rich **Todo API** built using [FastAPI](https://fastapi.tiangolo.com/) and deployed on [Render](https://render.com/). This API provides CRUD operations for todo items with user authentication and detailed documentation.

🔗 **Live Demo**: [https://renderfastapi-saxg.onrender.com](https://renderfastapi-saxg.onrender.com)  
📘 **Swagger Docs**: [https://renderfastapi-saxg.onrender.com/docs](https://renderfastapi-saxg.onrender.com/docs)  
📖 **ReDoc**: [https://renderfastapi-saxg.onrender.com/redoc](https://renderfastapi-saxg.onrender.com/redoc)

## 🚀 Features

### Core Features
- User registration and authentication
- JWT token-based security
- CRUD operations for todo items
- Per-user todo management
- Input validation
- Interactive API documentation

### API Endpoints

#### Authentication
- `POST /register` - Register a new user
- `POST /token` - Get access token

#### Todo Operations
- `GET /todos` - List all todos (authenticated)
- `GET /todos/{todo_id}` - Get specific todo
- `POST /todos` - Create new todo
- `PUT /todos/{todo_id}` - Update todo
- `DELETE /todos/{todo_id}` - Delete todo

## 📂 Project Structure
renderfastapi/
├── main.py # Main FastAPI app with endpoints
├── models.py # Pydantic models
├── database.py # In-memory or persistent DB logic
└── requirements.txt

## 🛠️ Tech Stack

- **FastAPI** (v0.109.0+) - Modern web framework
- **Uvicorn** (v0.27.0+) - ASGI server
- **Pydantic** (v2.0.0+) - Data validation
- **Python-Jose** - JWT token handling
- **Passlib** - Password hashing
- **Python-Multipart** - Form data parsing

---


# Deploy FastAPI on Render

Use this repo as a template to deploy a Python [FastAPI](https://fastapi.tiangolo.com) service on Render.

See https://render.com/docs/deploy-fastapi or follow the steps below:

## 📦 Deployment
This project is configured for deployment on Render. The deployment process is automated using the render.yaml configuration file.

### Manual Deployment Steps
1. Fork this repository
2. Create a new Web Service on Render
3. Connect your repository
4. Render will automatically:
   - Detect Python
   - Install dependencies
   - Start the service using uvicorn main:app --host 0.0.0.0 --port $PORT
## 📚 API Documentation
- Swagger UI : Visit /docs for interactive API documentation
- ReDoc : Visit /redoc for alternative documentation view
## 🤝 Contributing
1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request