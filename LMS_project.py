class LibraryItem:
    def __init__(self):                     # Encapsulation
        self.rate = 0  

    def calculate_cost(self, days):         # Abstraction
        pass

class Book(LibraryItem):                    # Inheritance
    def __init__(self):
        self.type = "Book"
        
    def calculate_cost(self, days):          # Polymorphism
        return days * 10

class Magazine(LibraryItem):
    def __init__(self):
        self.type = "Magazine"

    def calculate_cost(self, days):
        return days * 10

class LibraryApp:
    def __init__(self, item_obj):               # Composition
        self.item = item_obj

    def show_bill(self, days):
        print("Item Type:", self.item.type)
        print("Borrow Days:", days)
        print("Borrowing Charge:", self.item.calculate_cost(days))

b = Book()
m = Magazine()

app1 = LibraryApp(b)
app2 = LibraryApp(m)

app1.show_bill(5)
app2.show_bill(3)
            