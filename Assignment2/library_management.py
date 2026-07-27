# Book Class
class Book:
    # Constructor
    def __init__(self, title, author):
        self.title = title
        self.author = author


# Library Class
class Library:
    # Constructor
    def __init__(self):
        self.books = []

    # Add Book
    def addbook(self):
        title = input("Enter title: ")
        author = input("Enter author name: ")

        book = Book(title, author)
        self.books.append(book)

        print("Book added successfully!!")

    # Remove Book
    def remove_book(self):
        title = input("Enter book title: ")

        for book in self.books:
            if book.title.lower() == title.lower():
                self.books.remove(book)
                print("Book removed successfully!!")
                return

        print("Book not found!!\n")

    # Search Book
    def search_book(self):
        name = input("Enter title or author: ")

        found = False

        for book in self.books:
            if (name.lower() == book.title.lower() or
                    name.lower() == book.author.lower()):

                print("Title :", book.title)
                print("Author:", book.author)
                found = True

        if not found:
            print("Book not found!!\n")

    # Display Books
    def displaybooks(self):
        if len(self.books) == 0:
            print("Library is empty.")

        else:
            print("\nAvailable Books:")
            for book in self.books:
                print("Title :", book.title)
                print("Author:", book.author)
                print()


# Create Library Object
library = Library()

# Menu
while True:
    print("\n===== Library Menu =====")
    print("1. Add Book")
    print("2. Remove Book")
    print("3. Search Book")
    print("4. Display Books")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        library.addbook()

    elif choice == "2":
        library.remove_book()

    elif choice == "3":
        library.search_book()

    elif choice == "4":
        library.displaybooks()

    elif choice == "5":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!!")