the system should calculate salary for differnet type of employee using all opps concepts

employee - abstract class
full time emplyoee - child class
part time employee - child class
salary - encapuslated data
payroolsystem (HAS-A)
output-
employee created
 salary: 50000
 emplyee craeted 
 salart:40000
 the system should calculate salary for differnet type of employee using all opps concepts

employee - abstract class
full time emplyoee - child class
part time employee - child class
salary - encapuslated data
payroolsystem (HAS-A)
output-
employee created
 salary: 50000
 emplyee craeted 
 salart:40000
 
 
 

# Abstract class
class Employee():
    def __init__(self, salary):
        self.__salary = salary   

    @abstractmethod
    def show_salary(self):
        pass

    def get_salary(self):
        return self.__salary

class FullTimeEmployee(Employee):
    def show_salary(self):
        print("Employee created")
        print("Salary:", self.get_salary())



class PartTimeEmployee(Employee):
    def show_salary(self):
        print("Employee created")
        print("Salary:", self.get_salary())



class PayrollSystem:
    def process(self, emp):
        emp.show_salary()   # polymorphism


p = PayrollSystem()

e1 = FullTimeEmployee(50000)
p.process(e1)

e2 = PartTimeEmployee(40000)
p.process(e2)



design a console based library management system

a liabraryiten is the base(abstract) idea
book and magazine are differenet stypope of items
borrowing rules behave diff for each of them
a libraryapp controles items(has-a))