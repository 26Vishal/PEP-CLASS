from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
engine=create_engine("sqlite:///company.db")
Base=declarative_base()
class Employee(Base):
    __tablename__="employees"
    id=Column(Integer,primary_key=True)
    name=Column(String)
    age=Column(Integer)
    department=Column(String)
Base.metadata.create_all(engine)
Session=sessionmaker(bind=engine)
session=Session()
s1=Employee(id=1,name="rahul",age=21,department="python")
s2=Employee(id=2,name="karan",age=22,department="java")
s3=Employee(id=3,name="rohit",age=23,department="python")
# Check if employees already exist before adding
existing_ids = [e.id for e in session.query(Employee.id).all()]
if 1 not in existing_ids:
    session.add(s1)
if 2 not in existing_ids:
    session.add(s2)
if 3 not in existing_ids:
    session.add(s3)
session.commit()
employees=session.query(Employee).all()
for i in employees:
    print(i.id,i.name,i.age,i.department)
employee_to_update = session.query(Employee).filter_by(id=1).first()
if employee_to_update:
    employee_to_update.name="Mandy"
    session.add(employee_to_update)
session.commit()
employees=session.query(Employee).all()
print("employee details after update")
for i in employees:
    print(i.id,i.name,i.age,i.department)
emp=session.query(Employee).filter(Employee.id==1).first()
if emp:
    session.delete(emp)
    session.commit()
employees=session.query(Employee).all()
print("employee details after delete")
for i in employees:
    print(i.id,i.name,i.age,i.department)
stu=session.query(Employee).filter(Employee.age>20).all()
for i in stu:
    session.delete(i)
session.commit()
#name is rahul and age is greater than 21
emp=session.query(Employee).filter(Employee.name=="rahul",Employee.age>21).all()

emp=session.query(Employee).order_by(Employee.id).all()
session.query(Employee).order_by(Employee.id).limit(2).all()

# ==-->equal
# !=->not equal
# >-->greater than
# <--> less than
# >=-->greater or equal
# <=-->less or equal


from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
class Department(Base):
    __tablename__="departments"
    id=Column(Integer,primary_key=True)
    name=Column(String)
    students= relationship("Student",back_populates="department")

class Department(Base):
    __tablename__="students"
    id=Column(Integer,primary_key=True)
    name=Column(String)
    age=Column(Integer)
    department_id = Column(Integer,ForeignKey("department.id"))
    department=relationship("deaprtment",back_populates="students")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------chat-gptcode-------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------

# from sqlalchemy import create_engine, Column, Integer, String, desc
# from sqlalchemy.orm import declara
# # Create engine
# engine = create_engine("sqlite:///company.db")

# # Base class
# Base = declarative_base()

# # Model
# class Employee(Base):
#     __tablename__ = "employees"

#     id = Column(Integer, primary_key=True)
#     name = Column(String)
#     age = Column(Integer)
#     department = Column(String)

# # Create table
# Base.metadata.create_all(engine)

# # Session
# Session = sessionmaker(bind=engine)
# session = Session()

# # Insert data
# s1 = Employee(id=1, name="rahul", age=21, department="python")
# s2 = Employee(id=2, name="karan", age=22, department="java")
# s3 = Employee(id=3, name="rohit", age=23, department="python")

# # Check existing IDs
# existing_ids = [e[0] for e in session.query(Employee.id).all()]

# if 1 not in existing_ids:
#     session.add(s1)
# if 2 not in existing_ids:tive_base, sessionmaker

#     session.add(s2)
# if 3 not in existing_ids:
#     session.add(s3)

# session.commit()

# # Display employees
# employees = session.query(Employee).all()
# for i in employees:
#     print(i.id, i.name, i.age, i.department)

# # Update employee
# employee_to_update = session.query(Employee).filter_by(id=1).first()
# if employee_to_update:
#     employee_to_update.name = "Mandy"

# session.commit()

# print("\nEmployee details after update")
# employees = session.query(Employee).all()
# for i in employees:
#     print(i.id, i.name, i.age, i.department)

# # Delete employee with id=1
# emp = session.query(Employee).filter(Employee.id == 1).first()
# if emp:
#     session.delete(emp)
#     session.commit()

# print("\nEmployee details after delete")
# employees = session.query(Employee).all()
# for i in employees:
#     print(i.id, i.name, i.age, i.department)

# # Delete employees with age > 20
# stu = session.query(Employee).filter(Employee.age > 20).all()
# for i in stu:
#     session.delete(i)

# session.commit()

# # Filter examples
# emp = session.query(Employee).filter(
#     Employee.name == "rahul",
#     Employee.age > 21
# ).all()

# # Query method examples

# # .all() → returns all records
# all_emp = session.query(Employee).all()

# # .first() → returns first record
# first_emp = session.query(Employee).first()

# # .one() → exactly one record (else error)
# # one_emp = session.query(Employee).filter(Employee.id == 2).one()

# # .one_or_none() → zero or one allowed
# one_or_none_emp = session.query(Employee).filter(Employee.id == 2).one_or_none()

# # Order by descending id
# ordered_emp = session.query(Employee).order_by(desc(Employee.id)).all()

# # Filter example
# emp = session.query(Employee).filter(Employee.age > 18).all()

# session.query(Employee).order_by(Employee.id).limit(2).all()