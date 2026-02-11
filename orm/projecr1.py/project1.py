from sqlalchemy import create_engine, Column, Integer, String, ForignKey
fromsqlalchemy.orm import declarative_base, sessionmaker
#data base connection
engine = create_engine("sqlite:///libtrack.db")
Base=declarative_base()
Session=sessionmaker(bind=engine)
session=Session()
class Category(Base):
    __tablename__="categories"
    id=Column(Integer, primary_key=True)
    name=Column(String)
    books=relationship("Book",back_populates="category")
    
class Book(Base):
    __tablename__="books"
    id=Column(Integer,primary_key=True)
    title=Column(String)
    author=Column(String)
    category_id=Column(Integer,ForeignKey("categories.id"))
    category=relationship("Category",back_populates="books")
    borrows=relationship("Borrow",back_populates="books")
class Borrow(Base):
    __tablename__="borrows"
    borrow_date=Column(String)
    book_id=Column(Integer,ForeignKey("book.id"))
    books=relationship("Book",back_populates="borrows")
class Limit(Base):
    __tablename="limits"
    id=Column(Integer,primary_key=True)
    month=Column(String)
    max_books=Column(Integer)
    
    
def add_category():
    name=input('category name: ')
    #create category object and save
    session.add((category(name=name)))
    session.commit()
    print("category added")
    
def add_book():
    title=input("book title: ")
    author=input("author name: ")
    category_id=int(input("Category id: "))
    #create book object
    session.add(Book(title=title,author=author,category_id=category_id))
    session.commit()
    
def borrow_book():
    book_id=int(input("Book ID:"))
    date=input("borrow date (YYYY-MM-DD):")
    #create a  borrow record
    session.add(Borrow(book_id=book_id,borrow_data=data))
    session.commit()
    print("Book borrowed")
    
def update_borrow():
    bid=int(input("Borrow id:"))
    #find borrow record
    borroe=session.query(Borrow).filter(Borrow.id==bid).first()
    if borrow:
        borrow.borrow_date+input("new data:")
        session.commit()
        print("borrow updated")
    else:
        print("borrow not found")
        
def delete_borrow():
    bid=int(input("Borrow id"))
    borrow=session.query(Borrow).filter(Borrow.id==bid).first()
    if borrow:
        session.delete(borrow)
        session.commit()
        print("borrow deleted")
    else:
        print("borrow not found")
        
def search_by_date():
    data=input("enetr date:")
    borrows=session.query(Borrow).filter