from fastapi import FastAPI
from app.routers import employees

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

app.include_router(employees.router)

       
