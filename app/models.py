##from pydantic import BaseModel
##class Employee(BaseModel) :
  ##  id:int
  ##  name:str
   ## department:str
   ## salary:int

from sqlalchemy import Integer, String, Column
from app.database import engine
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class Employee(Base):
    __tablename__="employees"
    id= Column(Integer,primary_key=True)
    name=Column(String)
    department=Column(String)
    salary=Column(Integer)
