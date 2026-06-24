from fastapi import APIRouter,HTTPException,Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Employee ##SQLAlchemy model (Database)
from app.schemas import EmployeeCreate ## Pydantic model (Request validation)
from app.crud import employee as crud


router= APIRouter()

@router.get("/employees")
def get_employees(db:Session=Depends(get_db)):
    return crud.get_employees(db)

 
@router.get("/employees/{employee_id}")
def get_employee(employee_id: int, db:Session=Depends(get_db)):
    employee=crud.get_employee_by_id(db,employee_id)
    if not employee:
        raise HTTPException(status_code=404, detail="Employee not found")

    return employee

@router.get("/departments")
def get_departments(db:Session=Depends(get_db)):
    return crud.get_departments(db)  

@router.post("/employees")
def add_employee(employee: EmployeeCreate, db:Session=Depends(get_db)):
    return crud.create_employee(db,employee)
