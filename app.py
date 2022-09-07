from typing import List
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from db_connection import conn
from models.user_model import users
from schemas.user import User

app = FastAPI()

template = Jinja2Templates(directory = "templates")

@app.get("/")
async def root(request: Request):
    return template.TemplateResponse('index.html',  {"request": request},)

@app.post("/add")
async def addUser(user: User):
    print(user)
    conn.execute(users.insert().values(
      name = user.name,
      email = user.email,
      age = user.age
    ))
    return conn.execute(users.select()).fetchall()

@app.post("/user/{user_id}")
async def addUser(user_id: int):
    return conn.execute(users.select().where(users.c.id == user_id)).fetchall()


