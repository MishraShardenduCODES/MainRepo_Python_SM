# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 

class Library :
    def __init__(self) :
        self.books = []
        self.no_books = 0

    def addbks(self,*books) : 
        for i in books :
            self.books.append(i)
            self.no_books +=1 
    
    def no_of_books(self) :
        return self.no_books   
    
    def dsply_bks(self) :
        if (self.no_books) == 0 :
            print("There are no books !!")
        else :
            print(f"There are {self.no_books} books and they are : \n")
            for i in self.books :
                print(i) 

# Creating a library
library = Library()

# Displaying books (initially empty)
library.dsply_bks()

# Adding multiple books
library.addbks("The Great Gatsby", "To Kill a Mockingbird", "1984", "Harry Potter")

# Displaying books after adding
library.dsply_bks()

# Getting the number of books
num_of_books = library.no_of_books()
print(f"Number of books in the library: {num_of_books}")

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 