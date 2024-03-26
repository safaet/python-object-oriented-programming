class Book:
 
    def __init__(self, title, author, num_pages, ISBN, publisher):
        self.title = title
        self.author = author
        self.__num_pages = num_pages
        self.__ISBN = ISBN
        self.__publisher = publisher