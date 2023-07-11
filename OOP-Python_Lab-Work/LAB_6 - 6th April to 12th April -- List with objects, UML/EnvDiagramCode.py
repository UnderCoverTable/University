class Book:
    bookId = 1000
    
    def __init__(self,t=""):       
        Book.bookId +=1
        self.id  = Book.bookId
        self.title = t
    def settitle(self,t):
        self.title = t
    def gettitle(self):
        return self.title
    def bookinfo(self):
        print(self.id,self.title)

def main():
    bookobj = Book("python")    
    bookobj.bookinfo()
    bookobj2 = Book("C++")
    bookobj2.bookinfo()
    print (bookobj)
    print(bookobj2)
main()

        
