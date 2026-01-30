# composition
# don't relay on inhertence
#  use object of other class
class Address:
    def __init__(self,city):
        self.city=city
    def show_address(self):
        print("city:",self.city)

#Student class
class Student:
    def __init__(self,name,city):
        self.name= name
        # composition:
        # creating object classs inside student class
        self.address=Address(city)
    def show_student(self):
        print("Name",self.name)
        # using object of another  class
        self.address.show_address()
        
s=Student("Karan","delhi")
s.show_student()