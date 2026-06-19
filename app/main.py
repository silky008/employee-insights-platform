from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class Employee(BaseModel) :
    id:int
    name:str
    department:str
    salary:int




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

 
@app.get("/employees/{employee_id}")
def get_employee(employee_id: int):
    for employee in employees:
        if employee["id"] == employee_id:
            return employee
        
    raise HTTPException(
        status_code=404,
        detail="Employee not found"

    ) 

@app.get("/departments")
def get_departments():
    departments=[]
    for employee in employees:
        if employee['department']  not in departments:
            departments.append(employee['department'])

    return departments  

@app.post("/employees")
def add_employee(employee:Employee):
    for data in employees:
        if data["id"]==employee.id:
            raise HTTPException(
                status_code=400,
                detail="Employee ID already exists"
            )
    employees.append(employee.model_dump())
    return {
        "messsage":"Employee created successfully",
        "employee": employee
    }

       
