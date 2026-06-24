from fastapi import APIRouter,HTTPException,Depends
from sqlalchemy.orm import Session
from sqlalchemy import distinct
from app.database import get_db
from app.models import Employee ##SQLAlchemy model (Database)
from app.schemas import EmployeeCreate ## Pydantic model (Request validation)


router= APIRouter()

@router.get("/employees")
def get_employees(db:Session=Depends(get_db)):
    employees=db.query(Employee).all()
    return employees  

 
@router.get("/employees/{employee_id}")
def get_employee(employee_id: int, db:Session=Depends(get_db)):
    employee=db.query(Employee).filter(Employee.id==employee_id).first()
    if employee is None:
        raise HTTPException(
        status_code=404,
        detail="Employee not found"

    ) 
    return employee

@router.get("/departments")
def get_departments(db:Session=Depends(get_db)):
    departments=db.query(distinct(Employee.department)).all()
    return [department[0] for department in departments]   

@router.post("/employees")
def add_employee(employee: EmployeeCreate, db:Session=Depends(get_db)):
    new_employee=Employee(
         name=employee.name,
        department=employee.department,
        salary=employee.salary
    )
    db.add(new_employee)
    db.commit()
    db.refresh(new_employee)
    return {
        "messsage":"Employee created successfully",
        "employee": new_employee
    }

