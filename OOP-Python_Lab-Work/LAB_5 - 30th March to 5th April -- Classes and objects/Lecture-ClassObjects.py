'''Implement a class Book that has three attributes title,author and publisher.
Initialize these instance variables in constructor. Also make mutators and accessors for mentioned attributes.
Lastly make a method bookInfo() that displays all the information of a book'''

class Book:
    bookId = 1000
    bookCount = 0
    
    def __init__(self,t="",a="",p=""):
        print("constructor")
        Book.bookId +=1
        self.id  = Book.bookId
        self.title = t
        self.author = a
        self.publisher = p
        Book.bookCount +=1
        
    def settitle(self,t):
        self.title = t
    def setauthor(self,a):
        self.author = a
    def setpublisher(self,p):
        self.publisher = p

    def gettitle(self):
        return self.title
    def getauthor(self):
        return self.author
    def getpublisher(self):
        return self.publisher

    def bookinfo(self):
        print(self.id,self.title,self.author,self.publisher)

    def getBookCount():
        return Book.bookCount;


def main():
    bookobj = Book("python","abc","xyz")    
    bookobj.bookinfo()
    bookobj2 = Book("C++")
    bookobj2.bookinfo()
    bookobj3 = Book()
    print(Book.getBookCount())
    

main()

        
