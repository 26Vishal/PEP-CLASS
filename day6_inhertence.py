class Human:
    def eat(self):
        print("Human can eat")
        
class Student(Human):
    def study(self):
        print("Student can study")
        
s1= Student()
s1.eat()

class Animal:
    def sound(self):
        print("Animal can speak")
        
class Dog(Animal):
    def Sound(self):
        print("dog can bark")
        
a1 = Dog()
a1.sound()


#Method overriding + child class method overriding will always always override the parent class methods
# '''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''


class Father:
    def programmer(self):
        print("I am an a programmer")
class Mother:
    def Nurse(self):
        print("I am a Nurse")
class Child(Father , Mother):
    def Student(self):
        print('I am a student')
        
obj = Child()
obj.programmer()
obj.Nurse()
obj.Student()


class teacher:
    def teaching(self):
        print("teaching")
class coder:
    def coding(self):
        print("coding")
class student(teacher,coder):
    def student(self):
        super().__init__()
        print("studing")
obj = student()
obj.teaching()
obj.coding()
obj.student()


class person:

    def __init__(self,name):
        self.__name = name
    def get_name(self):
        return self.__name
    
class children(person):
    def showname(self):
        print(self.get_name)
obj= children("xyz")
obj.showname()


