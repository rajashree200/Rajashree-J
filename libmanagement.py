class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def __repr__(self):
        return f"Book(title='{self.title}', author='{self.author}', isbn='{self.isbn}')"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def search_by_title(self, title):
        return [book for book in self.books if title.lower() in book.title.lower()]

    def search_by_author(self, author):
        return [book for book in self.books if author.lower() in book.author.lower()]

    def search_by_isbn(self, isbn):
        return [book for book in self.books if isbn == book.isbn]

    def display_books(self):
        for book in self.books:
            print(book)

def get_book_details():
    title = input("Enter title: ")
    author = input("Enter author: ")
    while True:
        isbntemp = input("Enter 13-digit ISBN number: ")
        if len(isbntemp)==13:
            isbn=isbntemp
            break
        else:
            print("enter 13 digit ISBN number")
        
    return Book(title, author, isbn)

if __name__ == "__main__":
    library = Library()
    
    while True:
        print("")
        print("Enter 1 Add a book")
        print("Enter 2 Search by title")
        print("Enter 3 Search by author")
        print("Enter 4 Search by ISBN")
        print("Enter 5 Display all books")
        print("Enter 6 Exit")       
        action = int(input("Enter your choice: "))
        
        if action==1:
            book = get_book_details()
            library.add_book(book)
        elif action==2:
            title = input("Enter title to search: ")
            print("Search results:", library.search_by_title(title))
        elif action==3:
            author = input("Enter author to search: ")
            print("Search results:", library.search_by_author(author))
        elif action==4:
            isbn = input("Enter ISBN to search: ")
            print("Search results:", library.search_by_isbn(isbn))
        elif action==5:
            library.display_books()
        elif action==6:
            print("over")
            break
        else:
            print("Invalid choice")
