
# #kata: library shelf

# #goal: model a tiny library in pure python — no files, no web.

# constraints:

# a Book class with title, author, year
# a Library class that holds books, can add(book), find(title) (case-insensitive), and list_all()
# a short __main__ that creates a library, adds 3+ books, finds one, prints the list
# success check: running the script prints the found book and the full shelf, no crashes.

# stretch (optional): mark a book overdue with a bool and have list_overdue() return only those.


class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __repr__(self):
        return f"Book({self.title!r}, {self.author!r}, {self.year})"

class Library:

    def __init__(self):
        self.books = []

    def add(self, book):
        self.books.append(book)

    def find(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book

    def list_all(self):
        return(self.books)

if __name__ == "__main__":
    library = Library()
    the_hobbit = Book("the hobbit", "J.R.R. Tolkien", 1937)
    nineteen_eighty_four = Book("1984", "George Orwell", 1949)
    pride_and_prejudice = Book("Pride and Prejudice", "Jane Austen", 1813)
    
    library.add(the_hobbit)
    library.add(nineteen_eighty_four)
    library.add(pride_and_prejudice)

    print(library.find("the hobbit"))

    print(library.list_all())