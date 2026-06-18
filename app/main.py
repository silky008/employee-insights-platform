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
       
