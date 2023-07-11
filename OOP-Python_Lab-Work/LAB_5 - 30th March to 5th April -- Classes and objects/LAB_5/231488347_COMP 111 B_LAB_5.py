# QUESTION 1

class Flower:

    def __init__(self,n="-",pe=0,pr=0.0):
        print("*")
        self.name = str(n)
        self.petals = int(pe)
        self.price = float(pr)

    #Mutators
    def set_name(self,n):
        self.name = str(n)
    def set_petals(self,pe):
        self.petals = int(pe)
    def set_price(self,pr):
        self.price = float(pr)

    #Accessors
    def get_name(self):
        return self.name
    def get_petals(self):
        return self.petals
    def get_price(self):
        return self.price

    def get_info(self):
        print("Name:",self.name," - ","Petals:",self.petals," - ","Price: ",self.price)

def flower_main():

    flower_obj1 = Flower()
    flower_obj1.set_name("Rose")
    flower_obj1.set_petals(16)
    flower_obj1.set_price(7.5)

    flower_obj2 = Flower("Hydrangea",23,6)

    flower_obj1.get_info()
    flower_obj2.get_info()
flower_main()


# QUESTION 2

class dayType:

    def __init__(self,d="-",day_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday","Sunday"]):
        print("**")
        self.day = d
        self.day_list = day_list


    #Set the day
    def set_day(self,d="Monday"):
        self.day = d

    #Print the day
    def print_day(self):
        print(self.day)

    #Return the day
    def get_day(self):
        return self.day

    #Returns the next day
    def next_day(self):

        if self.day == self.day_list[0]:
            return self.day_list[1]
        if self.day == self.day_list[1]:
            return self.day_list[2]
        if self.day == self.day_list[2]:
            return self.day_list[3]
        if self.day == self.day_list[3]:
            return self.day_list[4]
        if self.day == self.day_list[4]:
            return self.day_list[5]
        if self.day == self.day_list[5]:
            return self.day_list[6]
        if self.day == self.day_list[6]:
            return self.day_list[0]

    #Returns the previous day
    def prev_day(self):

        if self.day == self.day_list[0]:
            return self.day_list[6]
        if self.day == self.day_list[6]:
            return self.day_list[5]
        if self.day == self.day_list[5]:
            return self.day_list[4]
        if self.day == self.day_list[4]:
            return self.day_list[3]
        if self.day == self.day_list[3]:
            return self.day_list[2]
        if self.day == self.day_list[2]:
            return self.day_list[1]
        if self.day == self.day_list[1]:
            return self.day_list[0]

    #Prints the day, n days in the future
    def future_day(self,n=0):

        if n<7:
            a=self.day_list.index(self.get_day())
            return self.day_list[a+n]

        if n>7: #20
            a = self.day_list.index(self.get_day())
            while n>7:
                n=n-7
            return self.day_list[a+n]


def day_main():
    day_obj = dayType()
    day_obj.set_day("Monday")
    day_obj.print_day()

    print(day_obj.next_day())
    print(day_obj.prev_day())
    print(day_obj.future_day(4))

day_main()


# QUESTION 3
class Message:

    # Constructor initially asks to enter a sender and recipinet,
    # but they can be changed later in needed, through their respective functions.
    def __init__(self, s="-", r="_"):
        print("***")
        self.sender = input("Please enter a sender: ")
        self.recipient = input("Please enter a recipient: ")
        self.message_body = []

    # To change the sender or recipient, that the
    # constructor set previously.
    def change_sender(self, s="-"):
        self.sender = s

    def change_recipient(self, r="_"):
        self.recipient = r

    # To check the sender and recipient
    def get_sender(self):
        return self.sender
    def get_recipient(self):
        return self.recipient

    # To add text to a mesasge
    def add_message(self, text=""):
        self.message_body.append(text)
    def print_message(self):
        for i in range(0, len(self.message_body)):
            print(self.message_body[i])

    # To print the message sender, recipient and message.
    def toString(self):
        print("From: ", self.sender)
        print("To: ", self.recipient)
        self.print_message()

def email_prof():
    email1 = Message()
    email1.add_message("I wanted to get a confirmation on the submission of my research paper.")
    email1.toString()

    email2 = Message()
    email2.add_message("Could you please review the sample Ive attached below, related to the assignment")
    email2.toString()

email_prof()


# QUESTION 4

class Customer:

    # class variable customer_id keeps track of the number of customers
    customer_id = 0
    def __init__(self, bal=0, a_id=0):
        print("****")
        Customer.customer_id += 1
        self.balance = bal
        self.account_id = a_id

    # To set an account ID and Balance seperately
    def set_accountID(self, a_id=0):
        self.account_id = a_id
    def set_balance(self,bal=0):
        self.balance = bal

    # To return account/customer ID and balance
    def AccountID(self):
        return self.account_id
    def CustomerID(self):
        return self.customer_id
    def CurrentBalance(self):
        return self.balance

    # Displays all information of a customer
    def DisplayInfo(self):
        print("Customer ID: ", self.customer_id)
        print("Account ID: ",self.account_id)
        print("Balance: ","$",self.balance)

def customer_main():

    customer1 = Customer(22300,101)
    customer1.DisplayInfo()
    customer2 = Customer(15000,102)
    customer2.DisplayInfo()

    customer3 = Customer()
    customer3.set_accountID(103)
    customer3.set_balance(12300)
    customer3.DisplayInfo()
customer_main()

