class library:
    def __init__(self,listofbooks) -> None:
        self.books = listofbooks
    def displayavailablebooks(self):
        print("The number of books available : ")
        for book in self.books:
            print(" *"+book)
    def borrowbook(self,bookName):
        if bookName in self.books:
            print(f"You have been issued {bookName}. please keep it safe and return within 30 days")
            self.books.remove(bookName)
            return True
        else:
            print("Sorry this book is not available or this book is already issued to someone else. please wait until the book is returned or the book is available")
            return False
    def returnbook(self,bookName):
        self.books.append(bookName)
        print("Thanks for returning the book! hope you enjoyed reading it. Have a nice day ")
       


class student:
    def requestbook(self):
        self.book = input("Enter the book you want: ")
        return self.book
    def returnbook(self):
        self.book = input("Enter the book you want to return: ")
        return self.book
    

if __name__== "__main__": 
    central_library = library(["python", "django", "c++", "java","java advance","linux","mongodb","Algorithms"])
    student = student()
    # central_library.displayavailablebooks()
    while(True):
        WelcomeMsg ='''
        =====Welcome to Central  Library=====
        Please choose an option:
        1.List all the Books
        2.Request a Book
        3.Add/Return a Book
        4.Exit
        '''
        print(WelcomeMsg)
        
        a = int(input("Enter a choice : "))
        if a ==1:
            central_library.displayavailablebooks()
        elif a==2:
            central_library.borrowbook(student.requestbook())
        elif a==3:
            central_library.returnbook(student.returnbook())
        elif a==4:
            print("Thanks for choosing Central Library. Have a great day ahead")
            exit()
        else: 
            print("Invalid choice!")
       
        