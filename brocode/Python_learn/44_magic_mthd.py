# Magic methods = Dunder methods (double underscore) __init__, __str__, __eq__
# They are automatically called by many of Python's built-in operations.
# They allow developers to define or customize the behavior of objects

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        
    def __str__(self):
        return f"{self.title} by {self.author}"
    
    def __eq__(self, other):
        return self.title == other.title and self.author == other.author and self.pages == other.pages
    def __lt__(self, other):
        return self.pages < other.pages
    def __gt__(self, other):
        return self.pages > other.pages
    def __add__(self, other):
        return self.pages + other.pages
    def __contains__(self, keyword):
        return keyword in self.title or keyword in self.author
    def __getitem__(self, key):
        if key == "title":
            return self.title
        elif key == "author":
            return self.author
        elif key == "pages":
            return self.pages
        else:
            return f"key {key} was not found"
    
book1 = Book("War and Peace", "Leo Tolstoy", 1225)
book2 = Book("The Great Gatsby", "F. Scott Fitzgerald", 180)
# print(book1)
# print(book1 == book2)
# print(book2 < book1)
# print(book2 > book1)
# print(book1 + book2)

# print("Great" in book2)
print(book1["audio"])