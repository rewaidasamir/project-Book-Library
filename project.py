from Client import Client
from Librarian import Librarian
from Book import Book
from BorrowingOrder import BorrowingOrder
from datetime import timedelta,date
import random

clients = []
librarians = []
books = []
borrowed_orders = []

clients = [
    Client(1, "roba", 20, "4058248795", "0599855845"),
    Client(2, "mai", 30, "4038459357", "0599685789"),
    Client(3, "lama", 50, "4098765428", "0599875364"),
]


books = [
    Book(1, "Clean Code", "how and why of writing clean code", "Robert C. Martin", "active"),
    Book(2, "Introduction to Algorithms", "All the algorithms discussed in the Introduction to Algorithms book ", "Thomas H. Cormen", "inactive"),
    Book(3, " Code Complete", "how to write robust code irrespective of the architecture of a programming language?", "Steve McConnell", "active"),
    Book(4, "The Pragmatic Programmer", "It’s the creative use of classic and modern anecdotes", " Andrew Hunt", "inactive"),
]
print("******************** Welcome to our library **************************")
def total_borrowed_books():
    total = 0
    for i in range(len(books)):
        if books[i].get_status() == "inactive":
            total = total + 1
    return total

def total_available_books():
    total = 0
    for i in range(0, len(books)):
        if books[i].get_status() == "active":
            total = total + 1
    return total

def total_borrowed_orders():
    return len(borrowed_orders)

def check_book_id(book_id):
    exist = "inactive"
    for i in range(len(books)):
        if book_id == int(books[i].get_id()):
            exist = "active"
            break
    return exist

def check_book_status(book_id):
    for i in range(len(books)):
        if book_id == int(books[i].get_id()) and books[i].get_status() == "inactive":
            return books[i]
        else:
            return "active"
def return_book(book_id):
    check_book_id(book_id)
    check_book_status(book_id)

    if check_book_id(int(book_id)):
        if check_book_status(int(book_id)):
            print("The book is returned successfully")
    else:
        print("There is no book with this id")
while True:
    for book in range(len(books)):
        print("Name : " + books[book].get_title())
    choice = int(input("1.Borrow book\n2.Return Book\n2.Exit\nWhat do you want to do? :"))
    if choice == 1:
        book_title=str(input("Enter book_title , please: "))
        for i in range(len(borrowed_orders)):
            if borrowed_orders[i].title.__eq__(book_id):
                client_id = int(input("Enter Client_id"))
                for i in range(len(clients)):
                    if clients[i].id == client_id:
                        borrowed_orders.append(
                            Book(client_id, book_id))
                    else:
                        print("You are not allowed to borrow the book")
                        break

    elif choice == 2:
        book_id = input("Enter book id, please: ")
        return_book(book_id)

    else:
        exit()
    print("total borrowed books: ", total_borrowed_books)
    print("total available books: ", total_available_books)
    print("total borrowed order: ", total_borrowed_orders)

