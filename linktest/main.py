from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from db import engine, SessionLocal
import models

app = FastAPI()

# Create tables
models.Base.metadata.create_all(bind=engine)

# DB dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"message": "FastAPI + PostgreSQL connected 🚀"}
