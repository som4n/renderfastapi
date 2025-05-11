# 📝 FastAPI Todo API (Deployed on Render)

A simple and clean **Todo API** built using [FastAPI](https://fastapi.tiangolo.com/) and deployed on [Render](https://render.com/). It offers basic CRUD operations to manage todo items.

🔗 **Live Demo**: [https://renderfastapi-saxg.onrender.com](https://renderfastapi.onrender.com)  
📘 **Swagger Docs**: [https://renderfastapi.onrender.com/docs](https://renderfastapi.onrender.com/docs)

---

## 🚀 Features

- Create todo items
- Read all or specific todos
- Update todo items
- Delete todo items
- Interactive Swagger UI for testing

---

## 📂 Project Structure
renderfastapi/
├── main.py # Main FastAPI app with endpoints
├── models.py # Pydantic models
├── database.py # In-memory or persistent DB logic
└── requirements.txt

## 🛠️ Tech Stack

- **FastAPI** – High performance web framework
- **Uvicorn** – Lightning-fast ASGI server
- **Pydantic** – Data validation

---


# Deploy FastAPI on Render

Use this repo as a template to deploy a Python [FastAPI](https://fastapi.tiangolo.com) service on Render.

See https://render.com/docs/deploy-fastapi or follow the steps below:

## Manual Steps

1. You may use this repository directly or [create your own repository from this template](https://github.com/render-examples/fastapi/generate) if you'd like to customize the code.
2. Create a new Web Service on Render.
3. Specify the URL to your new repository or this repository.
4. Render will automatically detect that you are deploying a Python service and use `pip` to download the dependencies.
5. Specify the following as the Start Command.

    ```shell
    uvicorn main:app --host 0.0.0.0 --port $PORT
    ```

6. Click Create Web Service.

Or simply click:

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com/deploy?repo=https://github.com/render-examples/fastapi)

## Thanks

Thanks to [Harish](https://harishgarg.com) for the [inspiration to create a FastAPI quickstart for Render](https://twitter.com/harishkgarg/status/1435084018677010434) and for some sample code!
