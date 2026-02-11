#import delaarative base
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
# //step1
engine=create_engine("sqlite:///school.db")
#step2
#create base class
Base = declarative_base()
#base will be parant of all  models
#step3
class Employee(Base):
    __tablename__="employees"
    id=Column(Integer,primary_key=True)
    name=Column(String)
    age=Column(Integer)
    department = Column(String)
    
#step 4
Base.metadata.create_all(engine)
#steep5
Session = sessionmaker(bind=engine)
session=Session()
e1=Employee(name="Nobita",age=14,department="collector")
e2=Employee(name="dekesuki",age =15,department="Peon")
session.add(e1)
session.add(e2)
session.commit()
#step6
employees=session.query(Employee).all()
for i in employees:
    print(i.id,i.name,i.age,i.department)
    
employees=session.query(Employee).filter_by(id=1).first()
employees.name="naman"
session.commit()
print("employee updated")
employees=session.query(Employee).all()
for i in employees:
    print(i.id,i.name,i.age,i.department)