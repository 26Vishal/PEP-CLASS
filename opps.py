# class Student:
#     def __init__(self,marks):
#         self.__marks = marks
#     def get_marks(self):
#         return self.__marks
#     def set_markd(self,newmarks):
        
        
# s1 = Student(100)
# print(s1.marks)
        
        
class Account:
    def __init__(self, balance):
        self.__balance = balance 
        
    def show_balance(self):
        print(self.__balance)
        
    def set_balance(self,new_balance):
        self.__balance = new_balance
        
a = Account(1000)
a.show_balance()
a.set_balance(10000)
a.show_balance()