from fastapi import APIRouter,HTTPException
from app.models import Employee
from app.data import employees

router= APIRouter()

@router.get("/employees")
def get_employees():
    return employees  

 
@router.get("/employees/{employee_id}")
def get_employee(employee_id: int):
    for employee in employees:
        if employee["id"] == employee_id:
            return employee
        
    raise HTTPException(
        status_code=404,
        detail="Employee not found"

    ) 

@router.get("/departments")
def get_departments():
    departments=[]
    for employee in employees:
        if employee['department']  not in departments:
            departments.append(employee['department'])

    return departments  

@router.post("/employees")
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

