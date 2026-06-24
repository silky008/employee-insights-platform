from sqlalchemy.orm import Session
from app.models import Employee ##SQLAlchemy model (Database)
from app.schemas import EmployeeCreate ## Pydantic model (Request validation)

def create_employee(db:Session,employee: EmployeeCreate):
    new_employee=Employee(
         name=employee.name,
        department=employee.department,
        salary=employee.salary
    )
    db.add(new_employee)
    db.commit()
    db.refresh(new_employee)
    return new_employee

def get_employees(db:Session):
    return db.query(Employee).all()
    
def get_employee_by_id(db:Session,employee_id: int):
    return db.query(Employee).filter(Employee.id==employee_id).first()


def get_departments(db:Session):
    departments=db.query(Employee.department).distinct().all()
    return [d[0] for d in departments]  
