# Abstract class
# Method name is present
# Method Body is Absent
# Child class will complete method without body


class Payment:
    def pay(self, amount):
        pass
class UPI(Payment):
    def pay(self,amount):
        print("Paid using UPI:",amount)
        
class card(Payment):
    def pay(self, amount):
        print("Paid using CArd:",amount)
class cash(Payment):
    def pay(self,amount):
        print("Paid with cash",amount)
        
obj1 = card()       
obj2 = cash() 
obj = UPI()
obj.pay(12)
obj2.pay(12)
obj1.pay(12)

class shape:
    def Shape(self, _shape):
        pass
class Triangle(shape):
    def Shape(self, _shape):
        print("The SHAPE IS ",_shape)
class circle(shape):
    def Shape(self, _shape):
        print("The SHAPE IS  ",_shape)
        
class rectangle(shape):
    def Shape(self, _shape):
        print("The SHAPE IS  ",_shape)
obj3 = Triangle()       
obj4 = circle() 
obj5 = rectangle()
obj5.Shape(12)
obj4.Shape(12)
obj3.Shape(12)


##create  a program where abstract class name corse it has row method course_ifo and duration then you j=have to make interface examInterface it has method exam exam_type() in the last you have ton  ake a childn class where Pyton_course(course, examINterfacxe ) which has method like duration and examtype()





class Course:
    
    def couse_info(self):
        pass
    def duration(self):
        
    
        pass
    
class ExamInterface:
    def exam_type(self):
        pass
    
class PythonCourse(Course, ExamInterface):
    
    def course_info(self):
        print("course ")
    def duation(self):
        print("3 hrs")
    def exam_type(self):
        print("offline")
    
obj = PythonCourse()
obj.course_info()
obj.duation()
obj.exam_type()