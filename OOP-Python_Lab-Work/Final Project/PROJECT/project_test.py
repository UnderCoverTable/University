2nd last state

class Library:

    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.books = []
        self.staff = []
        self.students = []

    def library_info(self):
        print("Library :",self.name)
        print("Number of available books: ",len(self.books))
        print("Number of registered staff: ",len(self.staff))
        print("Number of registered students: ",len(self.students))
        print("Address: ",self.address)


    def update_NameAddress(self, name, address):
        self.name = name
        self.address = address

    def register_staff(self, lib):
        self.staff.append(lib)

    def remove_staff(self,lib_name):
        check = 0
        for i in range(0,len(self.staff)):
            if lib_name == self.staff[i].get_name():
                rem = self.staff[i]
                check = 1
        if check == 1:
            self.staff.remove(rem)
            rem.details()
            print("Mentioned Librarian has been removed")
        if check == 0:
            print("Librarian not found")


    def staff_list(self):
        print("Number of registered staff: ", len(self.staff))
        for i in range(0, len(self.staff)):
            self.staff[i].details()

    def find_staff_name(self,lib_name):
        check = 0
        for i in range(0, len(self.staff)):
            if lib_name == self.staff[i].get_name():
                nem = self.staff[i]
                check = 1
        if check == 1:
            nem.details()
        if check == 0:
            print("Librarian not found")

    def find_student_name(self,stu_name):
        che = 0
        for i in range(0,len(self.students)):
            if stu_name == self.students[i].get_name():
                nem = self.students[i]
                che = 1
        if che == 1:
            nem.details()
        if che == 0:
            print("Student not found")

    def find_staff_id(self,lib_name):
        check = 0
        for i in range(0, len(self.staff)):
            if lib_name == self.staff[i].get_id():
                nem = self.staff[i]
                check = 1
        if check == 1:
            nem.details()
        if check == 0:
            print("Librarian not found")

    def find_student_id(self,stu_name):
        check = 0
        for i in range(0, len(self.students)):
            if stu_name == self.students[i].get_id():
                nem = self.students[i]
                check = 1
        if check == 1:
            nem.details()
        if check == 0:
            print("Student not found")



    def register_student(self, stu):
        self.students.append(stu)

    def remove_student(self,stu_name):
        check = 0
        for i in range(0, len(self.students)):
            if stu_name == self.students[i].get_name():
                rem = self.students[i]
                check = 1
        if check == 1:
            self.students.remove(rem)
            rem.details()
            print("Mentioned Student has been removed")
        if check == 0:
            print("Student not found")

    def student_list(self):
        print("Number of registered Students: ", len(self.students))
        for i in range(0, len(self.students)):
            self.students[i].details()

    def add_books(self, bo):
        self.books.append(bo)

    def available_books(self):
        print("Number of Available Books: ", len(self.books))
        for i in range(0, len(self.books)):
            self.books[i].book_info()


class Book:
    tracker = 100

    def __init__(self, tit, genre, auth, return_date=0):
        self.return_deadline = return_date
        self.title = tit
        self.genre = genre
        self.author = auth
        self.tracker = Book.tracker
        Book.tracker += 5

    def get_title(self):
        return self.title
    def get_author(self):
        return self.author

    def get_tracker(self):
        return self.tracker

    def issued_status(self, book_name, lib_name):
        book_list = lib_name.books
        checkk = 0

        for i in range(0, len(book_list)):
            if book_list[i].get_title() == book_name:
                checkk = 1
        if checkk == 1:
            print("Yes, book is available at the library.")
        else:
            print("Sorry, book has already been issued./not available")

    def book_info(self):
        print("Book Title: ", self.title, "   -   ", "Genre: ", self.genre, "   -   ", "Tracking code: ", self.tracker)
        self.author.details()
        print()


class Date:

    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def get_day(self):
        return self.day

    def get_month(self):
        return self.month

    def get_year(self):
        return self.year

    def change_date(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def get_date(self):
        print(self.day, "/", self.month, "/", self.year)


class Person:

    def __init__(self, name="-", iden=0, email="--"):
        self.name = name
        self.id = iden
        self.email = email

    def change_name(self, name):
        self.name = name

    def change_id(self, iden):
        self.id = iden

    def change_email(self, email):
        self.email = email

    def get_name(self):
        return self.name

    def get_id(self):
        return self.id

    def get_email(self):
        return self.email

    def details(self):
        print("Name: ", self.name)
        print("ID: ", self.id)
        print("Email: ", self.email)


class Librarian(Person):

    def __init__(self, name="-", iden=0, email="--"):
        super().__init__(name, iden, email)

    def find_book_name_aux(self,name_or_id, lib_name):
        book_li = lib_name.books
        check = 0
        bb = 0
        for i in range(0, len(book_li)):
            if book_li[i].get_title() == name_or_id:
                check = 1
                bb = book_li[i]
                break
        if check == 1:
            return bb
        if check == 0:
            print("Book not available")


    def find_book_name(self,name_or_id, lib_name):

        book_li = lib_name.books
        check = 0
        bb = 0
        for i in range(0, len(book_li)):
            if book_li[i].get_title() == name_or_id:
                check = 1
                bb = book_li[i]
                break
        if check == 1:
            print("Yes book is available")
            want_info = input("Would you like more info? ")
            if want_info == 'yes':
                bb.book_info()

        if check == 0:
            print("Book not available")

    def find_book_id_aux(self, name_or_id, lib_name):
        book_li = lib_name.books
        check = 10
        bb = 0
        for i in range(0, len(book_li)):
            if book_li[i].get_tracker() == int(name_or_id):
                check = 1
                bb = book_li[i]
                break
            else:
                check = 0
        if check == 1:
            return bb
        if check == 0:
            print("Book not found")


    def find_book_id(self,name_or_id,lib_name):

        book_li = lib_name.books
        check = 10
        bb = 0
        for i in range(0, len(book_li)):
            if book_li[i].get_tracker() == int(name_or_id):
                check = 1
                bb = book_li[i]
                break
            else:
                check = 0
        if check == 1:
            print("Yes book is available")
            want_info = input("Would you like more info? ")
            if want_info == 'yes':
                bb.book_info()

        if check == 0:
            print("Could not find book with tracker id ", name_or_id)

    def issue_book(self, stu_name, book_name, day,mon,year, lib_name):
        global check_for_remove
        return_date = Date(day,mon,year)
        book_name.return_deadline = return_date

        book_list = lib_name.books
        stu_books = stu_name.issuedBooks
        a = len(book_list)

        check = 0
        for c in range(0, a):

            if book_list[c].get_title() == book_name.get_title():
                check = 1
                check_for_remove = book_list[c]

        if check == 1:
            book_list.remove(check_for_remove)
            stu_books.append(check_for_remove)
            print("Student will return book: ",book_name.get_title()), print("on Return date:"), return_date.get_date()
        if check == 0:
            print("Book not available")

    def receive_book(self, stu_name, book_name, day,mon,year, lib_name):

        global check_for_remove
        today_date = Date(day,mon,year)
        re_day = book_name.return_deadline

        book_list = lib_name.books
        stu_books = stu_name.issuedBooks
        a = len(stu_books)
        check = 0
        for i in range(0, a):
            if book_name.get_title() == stu_books[i].get_title():
                check_for_remove = stu_books[i]
                check = 1
                break
        if check == 1:
            stu_books.remove(check_for_remove)
            book_list.append(check_for_remove)
            print("Book has been recieved")
        if check == 0:
            print("Student did not have this book issued")

        if int(re_day.get_month()) == int(today_date.get_month()) and int(today_date.get_year()) == int(re_day.get_year()):
            if int(today_date.get_day()) < int(re_day.get_day()) or int(today_date.get_day()) == int(re_day.get_day()):
                print("Thank you for returning the book on time.")

            if int(today_date.get_day()) > int(re_day.get_day()):
                late_days = int(today_date.get_day()) - int(re_day.get_day())
                print("Returned book,",late_days," days late.")
                fine_amount = late_days*10
                print("You have been fined, Rs.",fine_amount)

                stu_list = lib_name.students
                for i in range(0, len(stu_list)):
                    if stu_name.get_name() == stu_list[i].get_name():
                        stu_list[i].fines += fine_amount

        if int(today_date.get_month()) > int(re_day.get_month()) and int(today_date.get_year()) == int(re_day.get_year()):

            late_days = (31 - int(re_day.get_day()))+int(today_date.get_day())
            print("Returned book,", late_days, " days late.")
            fine_amount = late_days*10
            print("You have been fined, Rs.", fine_amount)

            stu_list = lib_name.students
            for i in range(0, len(stu_list)):
                if stu_name.get_name() == stu_list[i].get_name():
                    stu_list[i].fines += fine_amount

        if int(today_date.get_year()) > int(re_day.get_year()) and int(today_date.get_month()) > int(re_day.get_month()):
            days_late = 365 + abs((31 - int(re_day.get_day())))+int(today_date.get_day())
            print("You have returned book,",days_late,"days late")
            print("You have been fined,",days_late*10)

            stu_list = lib_name.students
            for i in range(0, len(stu_list)):
                if stu_name.get_name() == stu_list[i].get_name():
                    stu_list[i].fines += days_late*10

        if int(today_date.get_year()) > int(re_day.get_year()) and int(today_date.get_month()) < int(re_day.get_month()):
            days_late = abs((int(re_day.get_month()) - int(today_date.get_month()) - 12) * 31 + (int(re_day.get_day()) - int(today_date.get_day())))

            print("You have returned book,", days_late, "days late")
            print("You have been fined,", days_late * 10)

            stu_list = lib_name.students
            for i in range(0, len(stu_list)):
                if stu_name.get_name() == stu_list[i].get_name():
                    stu_list[i].fines += days_late * 10






    def fine_student(self, stu_name, fine, lib_name):

        stu_list = lib_name.students

        for i in range(0, len(stu_list)):
            if stu_name == stu_list[i].get_name():
                stu_list[i].fines += fine
                print(stu_list[i].get_name(), "has been fined, Rs.", fine)
                check_stu_fines = input("Would you like to  check the students, accumalated fines? ")
                if check_stu_fines == "yes":
                    stu_list[i].details()

    def details(self):
        print("- Librarian:")
        super().details()


class Student(Person):
    def __init__(self, name="-", iden=0, email="--"):
        super().__init__(name, iden, email)
        self.issuedBooks = []
        self.fines = 0

    def get_name(self):
        return self.name

    def check_fines_aux(self):
        return self.fines

    def check_fines(self):
        print("You have payable fines, Rs.", self.fines)

    def pay_fine(self, pay):
        r_fines = self.fines
        if (r_fines - pay) < 0:
            print("Student fines is becoming negative. Please pay the correct amount")

        else:
            self.fines -= pay
            print("You have paid off,", "Rs.", pay)

    def receive_book_name_aux(self,name):
        check = 0
        for i in range(0,len(self.issuedBooks)):
            if self.issuedBooks[i].get_title() == name:
                check = 1
                bk = self.issuedBooks[i]
        if check == 1:
            return bk
        else: print("Book not found")



    def issued_book(self):
        for i in range(0, len(self.issuedBooks)):
            self.issuedBooks[i].book_info()

    def details(self):
        print("- Student:")
        super().details()
        print("Payable Fines: ", self.fines)


class Author(Person):
    def __init__(self, name="-", email="Not available"):
        super().__init__(name, email)
        self.writtenBooks = []

    def add_book(self, book_name):
        self.writtenBooks.append(book_name)

    def remove_book(self, book_name):
        check = 0
        for i in range(0, len(self.writtenBooks)):
            if self.writtenBooks[i].get_title() == book_name:
                rem_book = self.writtenBooks[i]
                check = 1
        if check == 1:
            self.writtenBooks.remove(rem_book)
            print("Book has been removed from authors portfolio")

        if check == 0:
            print("The library already did not possess this authors book")

    def portfolio(self,libaray):

        bok_list = libaray.books
        print("Authors books available at the library: ")
        for i in range(0, len(bok_list)):
            print(i + 1, ".",bok_list[i].get_title()," by ",bok_list[i].get_author().get_name())

    def details(self):
        print("- Author:")
        print("Name: ", self.name)
        print("Email: ", self.email)


def main_loop():

    main_library = Library("Library of Alexandria","Alexandria Governorate 21526, Egypt")
    head_lib = Librarian("head",5623,"test@gmail.com")
    main_library.register_staff(head_lib)
    test_auth = Author("TEST")
    test_main_book = Book("test","test",test_auth)

    run_check = 1
    while run_check != 0:

        menu_items = ["Library Info","Register Librarian/Remove Librarian","Librarian Info","Register/Remove Student","Student info","Student Fines",
                      "Add book to Library"," Library Catalogue","Search book by Name/ID","Issue Book","Receive Book","Book availability","All authors and their books",
                      "EXIT"]

        for i in range(6):
            print(i+1,".",menu_items[i], end=" | ")
        print()
        for i in range(6,13):
            print(i + 1, ".", menu_items[i], end=" | ")
        print()
        print("0.",menu_items[13])



        run = input("|Press menu number to perform action| ==> ")

        # EXIT
        if run == "0":
            print("- Program is exiting -")
            run_check = 0

        # Library Info
        if run == "1":
            print("-"*6)

            print("[ 1 . Library Info ]")
            main_library.library_info()

            print("-"*6)

        # Register Librarian/Remove Librarian
        if run == "2":
            print("-" * 6)
            print("[ 2 . Register Librarian/Remove Librarian ]")
            print("|Press menu number to perform action|")
            what_action = input("1. Register staff\n2. Remove staff\n= ")

            if what_action == "1":
                iden_li = []
                how_many = int(input("How many librarians do you want to register? --> "))
                for i in range(0,how_many):
                    info = input("-Please enter Name, ID, Email. As so, (Name/ID/Email)-\n= ")

                    info_list = info.split("/")
                    new_librarian = Librarian(info_list[0],int(info_list[1]),info_list[2])

                    if info_list[1] not in iden_li:
                        main_library.register_staff(new_librarian)
                        print("New librarian registered !")
                        iden_li.append(info_list[1])
                    else: print("There already exists a student with the ID,",info_list[1],". Please try registering again")


            if what_action == "2":
                rem_name = input("Enter name and ID of Librarian to remove: ")
                rem_li = rem_name.split()
                lib_list = main_library.staff
                cc = 0
                aa = 0

                for i in range(0,len(lib_list)):
                    if rem_li[0] == lib_list[i].get_name() and int(rem_li[1]) == lib_list[i].get_id():
                        aa = lib_list[i]
                        cc = 1
                if cc == 1:
                    main_library.remove_staff(aa.get_name())
                if cc == 0:
                    print("Librarian not found")
            print("-" * 6)

        # Librarian Info
        if run == "3":
            print("-" * 6)
            print("[ 3 . Librarian Info ]")
            print("|Press menu number to perform action|")

            what_action = input("1. All Librarian Info\n2. Specific Librarian Info\n= ")
            if what_action == "1":
                main_library.staff_list()
            if what_action == "2":
                librarian_name_id = input("Enter the Librarians Name or ID: ")

                if librarian_name_id.isalpha() == True:
                    main_library.find_staff_name(librarian_name_id)
                else:
                    main_library.find_staff_id(int(librarian_name_id))

            print("-" * 6)

        # Register/Remove Student
        if run == "4":
            print("-" * 6)
            print("[ 4 . Register Student/Remove Student ]")
            print("|Press menu number to perform action|")
            what_action = input("1. Register student\n2. Remove student\n= ")

            if what_action == "1":
                id_list = []
                how_many = int(input("How many students do you want to register? --> "))
                for i in range(0, how_many):
                    info = input("-Please enter Name, ID, Email. As so, (Name/ID/Email)\n= ")
                    info_list = info.split("/")
                    new_student = Student(info_list[0], int(info_list[1]), info_list[2])

                    if info_list[1] not in id_list:
                        main_library.register_student(new_student)
                        print("New Student registered !")
                        id_list.append(info_list[1])
                    else:
                        print("There already exists a student with the ID,",info_list[1],". Please try registering again")

            if what_action == "2":
                rem_name = input("Enter name and ID of Student to remove (Name/ID) : ")
                info_li = rem_name.split("/")
                stu_lst = main_library.students
                c = 0
                a = 0

                for i in range(0,len(stu_lst)):
                    if info_li[0] == stu_lst[i].get_name() and int(info_li[1]) == stu_lst[i].get_id():
                        a = stu_lst[i]
                        c = 1

                if c == 1:
                    main_library.remove_student(a.get_name())
                if c == 0:
                    print("Student not found")
            print("-" * 6)

        # Student Info
        if run == "5":
            print("-" * 6)
            print("[ 5 . Student Info ]")
            print("|Press menu number to perform action|")

            what_action = input("1. All Students Info\n2. Specific Student Info\n= ")
            if what_action == "1":
                main_library.student_list()
            if what_action == "2":
                student_name_id = input("Enter the Students Name or ID: ")

                if student_name_id.isalpha() == True:
                    main_library.find_student_name(student_name_id)
                else:
                    main_library.find_student_id(int(student_name_id))

            print("-" * 6)

        # Student Fines
        if run == "6":
            print("-" * 6)
            print("[ 6 . Student Fines ]")
            print("|Press menu number to perform action|")

            what_action = input("1. Allot Student fines\n2. Deduct Student Fines\n3. Check Student Fine\n= ")

            if what_action == "1":
                student_name = input("Please enter the students name and ID / How much fine (Name/ID/Fine): ")
                fine_list = student_name.split("/")
                stu_list = main_library.students
                check = 0

                for i in range(0,len(stu_list)):
                    if stu_list[i].get_name() == fine_list[0] and stu_list[i].get_id() == int(fine_list[1]):
                        check = 1
                if check == 1:
                    head_lib.fine_student(fine_list[0],int(fine_list[2]),main_library)
                if check == 0:
                    print("Student not found")

            if what_action == "2":
                student_name = input("Enter Student  name and ID / How much fine to deduct(Name/ID/payed fine) : ")
                pay_list = student_name.split("/")
                stu_list = main_library.students
                check = 0

                for i in range(0,len(stu_list)):
                    if stu_list[i].get_name() == pay_list[0] and stu_list[i].get_id() == int(pay_list[1]):
                        stu = stu_list[i]
                        check = 1
                if check == 1:
                    stu.pay_fine(int(pay_list[2]))
                    stu.details()
                if check == 0:
                    print("Student not found")

            if what_action == "3":
                find_stu = input("Enter Student  name and ID (Name/ID) : ")
                f_l = find_stu.split("/")
                stu_list = main_library.students
                check = 0

                for i in range(0,len(stu_list)):
                    if stu_list[i].get_name() == f_l[0] and stu_list[i].get_id() == int(f_l[1]):
                        stu = stu_list[i]
                        check = 1
                if check == 1:
                    stu.check_fines()
                if check == 0:
                    print("Student not found")








            print("-" * 6)

        #Add book to library
        if run == "7":
            print("-" * 6)
            print("[ 7 . Add book to catalogue ]")

            h_books = input("How many books do you want to register to library? --> ")
            for i in range(0,int(h_books)):
                author_info = input("Please enter the authors Name and/or Email (Name/Email or -): ")
                author_list = author_info.split("/")
                auth = Author(author_list[0],author_list[1])
                book_info = input("Enter book title and genre (Title/Genre): ")
                book_list = book_info.split("/")
                book = Book(book_list[0],book_list[1],auth)
                main_library.books.append(book)
                print()
                print("Book has been registered")
                book.book_info()
            print("-" * 6)

        # Library Catalogue
        if run == "8":
            print("-" * 6)
            print("[ 8 . Library Catalogue ]")

            main_library.available_books()
            print("-" * 6)

        #Searh book by name/id
        if run == "9":
            print("-" * 6)
            print("[ 9 . Search book by Name/ID ]")

            search_how = input("Enter Book Name or ID: ")

            if search_how.isalpha() is True:
                head_lib.find_book_name(search_how, main_library)

            if search_how.isdigit() is False and search_how.isalpha() is False:

                head_lib.find_book_name(search_how,main_library)

            if search_how.isdigit():
                head_lib.find_book_id(int(search_how),main_library)

            print("-" * 6)
            print("-" * 6)
            print("[ 9 . Search book by Name/ID ]")

        #Issue Book
        if run == "10":
            print("-" * 6)
            print("[ 10 . Issue Book ]")

            loop_check = 0


            print("-"*3)
            while loop_check != 1:
                search_how = input("Enter issuing Book Name or ID: ")

                if search_how.isalpha() is True:
                    issue_book = head_lib.find_book_name_aux(search_how, main_library)


                if search_how.isdigit() is False and search_how.isalpha() is False:
                    issue_book = head_lib.find_book_name_aux(search_how, main_library)


                if search_how.isdigit():
                    issue_book = head_lib.find_book_id_aux(int(search_how), main_library)

                if issue_book == None:
                    print("Enter a valid book.")
                if issue_book != None:
                    loop_check = 1
                    print(issue_book.get_title())
            print("-" * 3)
            loop_check2 = 0
            while loop_check2 != 1:
                stu_i = input("Enter ID of student, being issued too: ")
                stu_list = main_library.students
                ch = 0
                for i in range(0,len(stu_list)):
                    if stu_list[i].get_id() == int(stu_i):
                        student_issuing = stu_list[i]
                        ch = 1
                if ch == 1:
                    loop_check2 = 1
                if ch == 0:
                    print("Student not found")
                    print("Enter a valid, registered student.")
            print("-" * 3)
            return_date = input("Please enter date of return (D/M/Y) : ")
            return_list = return_date.split("/")

            head_lib.issue_book(student_issuing,issue_book,return_list[0],return_list[1],return_list[2],main_library)

            print("-" * 6)

        #Recieve book
        if run == "11":
            print("-" * 6)
            print("[ 11 . Receive Book ]")

            print("-" * 3)
            loop_check2 = 0
            while loop_check2 != 1:
                stu_i = input("Enter ID of student, returning book: ")
                stu_list = main_library.students
                ch = 0
                for i in range(0, len(stu_list)):
                    if stu_list[i].get_id() == int(stu_i):
                        student_issuing = stu_list[i]
                        ch = 1
                if ch == 1:
                    loop_check2 = 1
                if ch == 0:
                    print("Student not found")
                    print("Enter a valid, registered student.")
            print("-" * 3)

            loop_check3 = 0
            while loop_check3 != 1:
                book_name = input("Enter the returning book name: ")
                issued_book = student_issuing.receive_book_name_aux(book_name)
                if issued_book == None:
                    print("Enter a valid, issued book.")
                if issued_book != None:
                    loop_check3 = 1

            today_date = input("Please enter todays date (D/M/Y) : ")
            today_list = today_date.split("/")

            head_lib.receive_book(student_issuing, issued_book, today_list[0], today_list[1], today_list[2],main_library)

            print("-" * 6)

        #BOOK AVAILABILITY
        if run == "12":
            print("-" * 6)
            print("[ 12 . Book Availability ]")
            bk_name = input("Please enter a book title: ")

            test_main_book.issued_status(bk_name,main_library)

            print("-" * 6)

        #All authors and thier books
        if run == "13":
            print("-" * 6)
            print("[ 12 . Book Availability ]")
            test_auth.portfolio(main_library)
            print("-" * 6)

main_loop()









