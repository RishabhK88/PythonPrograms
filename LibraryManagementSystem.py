class Library:
    def __init__(self, LibraryName, BookList=None, lb={}):
        self.LibraryName = LibraryName
        if BookList is None:
            BookList = []
        if BookList is not None:
            self.BookList = BookList
        if lb is not None:
            self.lb = lb

    def DisplayBooks(self, BookList):
        for i, Book in enumerate(self.BookList, 1):
            print(f"{i}. {Book}")

    def AddBook(self, Book):
        self.BookList.append(Book)
        print(f"{Book} successfully added to the library")

    def LendBook(self, Book, Owner):
        self.BookList.remove(Book)
        print(f"{Book} has been successsfully lend to {Owner}")
        print(f"{Book} is no longer available in library")
        self.lb.update({Book: Owner})

    def ReturnBooks(self, Book, Owner):
        self.BookList.append(Book)
        print(f"{Book} has been recieved by {Owner}")
        print("Thank you for returning the Book")
        self.lb.pop(Book)


Name = input("What do you want to call your Library? ")
n = int(input("Number of books available in your library: "))
print("Enter the name of Books currently available in your Library: ")

lst = []
for i in range(n):
    j = input("Book Name: ")
    lst.append(j)
MyLibrary = Library(Name, lst)
ch1 = "y"
while(ch1 == "y" or ch1 == "Y"):
    print("Library Management System")
    print("1. Display Available Books")
    print("2. Add Book in Library")
    print("3. Lend Book from Library")
    print("4. Return Back Book")
    ch = 0
    ch = int(input("Enter your Choice(1-4): "))
    if ch == 1:
        MyLibrary.DisplayBooks(lst)
    elif ch == 2:
        A_Book = input("Enter the name of the book to be added: ")
        MyLibrary.AddBook(A_Book)
    elif ch == 3:
        B_Book = input("Enter the book to be lend: ")
        Own1 = input("Enter the name of the owner: ")
        MyLibrary.LendBook(B_Book, Own1)
    elif ch == 4:
        C_Book = input("Enter the book to be returned: ")
        Own2 = input("Enter the name of the owner: ")
        MyLibrary.ReturnBooks(C_Book, Own2)
    ch1 = input("Do you Want to Continue(y/n)? ")
    if ch1 == "n" or ch1 == "N":
        exit
