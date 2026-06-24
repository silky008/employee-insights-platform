from fastapi import FastAPI
from app.routers import employees
from sqlalchemy.orm import Session
from fastapi import Depends
from app.database import get_db


app = FastAPI()
@app.get("/")
def home():
    return {
        "message": "Welcome to Employee Insights Platform"
        }

@app.get("/about")
def about():
    return {
           "project": "Employee Insights Platform",
            "version": "1.0"
    }  

@app.get("/health")
def health():
    return {
        "status": "OK",
        "application": "Employee Insights Platform"
    } 

@app.get("/db_test")
def db_test(db:Session=Depends(get_db)):
    return { "message": "Database session connected successfully"}

app.include_router(employees.router)

       
