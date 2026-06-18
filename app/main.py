from fastapi import FastAPI, HTTPException

app = FastAPI()

employees = [
    {
        "id": 1,
        "name": "Alice",
        "department": "HR",
        "salary": 40000
    },
    {
        "id": 2,
        "name": "Bob",
        "department": "IT",
        "salary": 50000
    },
    {
        "id": 3,
        "name": "Charlie",
        "department": "Finance",
        "salary": 60000
    }
]

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

@app.get("/employees")
def get_employees():
    return employees  

 

