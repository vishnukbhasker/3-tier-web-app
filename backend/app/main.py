from fastapi import FastAPI, HTTPException
from .database import engine, Base, SessionLocal
from .models import User
from .crud import create_user, get_users

Base.metadata.create_all(bind=engine)
app = FastAPI()

@app.post("/users/")
def add_user(username: str, email: str):
    db = SessionLocal()
    user = create_user(db, username=username, email=email)
    db.close()
    return user

@app.get("/users/")
def list_users():
    db = SessionLocal()
    users = get_users(db)
    db.close()
    return users
