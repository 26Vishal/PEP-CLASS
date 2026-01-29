# class Student:
#     print("Hey this is as First class")
    
# s1= Student()
# print(s1)

# class student:
#     def __init__(self):
#         self.name="Rahul"
#         print("This is our constructor")
        
# s2= student()
# print(s2.name)

# class marks:
#     def __init__(self):
#         self.name= input("Enter name")
#         self.Marks = int(input("Enter marks"))
#     def display(self):
#         print(self.name,self.Marks)
        
# m = marks()
# m.display()


# class Cars:
#     def __init__(self):
#         self.name = input("Enter the car name")
#         self.milage = int(input("enter the milage of car"))
#         self.price = int(input("enter the milage of car"))
        
#     def display(self):
#         print(self.name,self.milage,self.price)
        
# c = Cars()
# c.display()


class Student:
    Collage_name = "LPU"
    def __init__(self,fullname,marks):
        self.name = fullname
        self.marks = marks
        
s1 = Student("Rahul",86)
s2 = Student("Karan",63)
print(s1.name)
print(s2.name)
print(s1.Collage_name)
print(s2.Collage_name)


class Employee:
    Company_name = "AMAZON"
    def __init__(self,fullname , salary):
        self.name = fullname
        self.salary = salary
        
E1 = Employee("Rahul",86000)
E2 = Employee("Karan",63000)
print(E1.name)
print(E2.name)
print(E1.Company_name)
print(E2.Company_name)

class Student:
    college_name = "LPU"
    def __init__(self, student_name,marks):
        self.name = student_name
        self.marks = marks
s1 = Student("xyz",55)
s2 = Student("ABC",88)
s1.college_name = "IIT"
print(s1.name)
print(s1.college_name)
print(s2.name)
print(s2.college_name)



class Employee:
    Company_name = "AMAZON"
    def __init__(self,fullname , salary):
        self.name = fullname
        self.salary = salary
        
E1 = Employee("Rahul",86000)
E2 = Employee("Karan",63000)
print(E1.name)
print(E1.salary)
E1.salary = 90000
print(E1.salary)
print(E2.name)
print(E2.salary)
print(E1.Company_name)
print(E2.Company_name)


class student:
    def __init__()