#import delaarative base
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
# //step1
engine=create_engine("sqlite:////school.db")
#step2
#create base class
Base = declarative_base()
#base will be parant of all  models
#step3
class Student(Base):
    __tablename__="student"
    id=Column(Integer,primary_key=True)
    name=Column(String)
    age=Column(Integer)
    course = Column(String)
#step4
Base.metadata.create_all(engine)
  
Session = sessionmaker(bind=engine)
session = Session()
s1 = Student(id=1,name="Vishal",age=20,course="Python")
s2 = Student(id=2,name="Rahul",age =20,course="python")
session.add(s1)
session.add(s2)
session.commit()
students = session.query(Student).all()
for i in students:
    print(i.id,i.name,i.age,i.course)

