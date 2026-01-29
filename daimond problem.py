class A:
    def message(self):
        print("Grandfather inhertinace")
        
class B(A):
    def message(self):
        print("father inhertinace")
        
class C(A):
    def message(self):
        print("mother inhertinace")
        
class D(B,C):
    def message(self):
        print("Grandfather inhertinace")
    
s1 = D()
s1.message()
# s1.message()
# s1.message()
class