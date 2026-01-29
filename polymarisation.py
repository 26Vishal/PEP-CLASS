class Vehicle:
    def drive(self):
        print("Vehicle is moving")
class Car(Vehicle):
    def drive(self):
        print("Car is driving fast")

class Bus(Vehicle):
    def drive(self):
        print("Bus is carrying passengers")

class Truck(Vehicle):
    def drive(self):
        print("Truck is carrying heavy load")
c = Car()
b = Bus()
t = Truck()

c.drive()
b.drive()
t.drive()



a = [1,2,3]
b = a
b.append(4)
print(a)