class Book:
 
    def __init__(self, title, author, num_pages, ISBN, publisher):
        self.title = title
        self.author = author
        self.__num_pages = num_pages
        self.__ISBN = ISBN
        self.__publisher = publisher
        
myBook = Book("The Alchemist", "Paulo Coelho", 208, "978-0062315007", "HarperOne")  
print(myBook.title)
print(myBook.author)    
print(myBook._num_pages)
print(myBook._ISBN)
print(myBook._publisher)
