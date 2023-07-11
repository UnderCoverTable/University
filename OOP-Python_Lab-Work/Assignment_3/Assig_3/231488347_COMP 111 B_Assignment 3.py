from abc import ABC, abstractmethod
from functools import reduce

# TASK 1

class Person:

    def __init__(self,name,iden,number):
        self.name = name
        self.id = iden
        self.p_number = number

    def person_details(self):
        print("-Owner/Driver-")
        print("Name: ",self.name)
        print("ID: ",self.id)
        print("Contact: ",self.p_number)

class Vehicle:

    def __init__(self,manu="-",cylinders=0,name="-",iden=0,number="-"):
        self.manufacturer = manu
        self.cylinders = cylinders
        self.owner = Person(name,iden,number)

    def details(self):
        self.owner.person_details()
        print("-Vehicle-")
        print("Car Manufacturer: ",self.manufacturer)
        print("Engine Cylinders: ",self.cylinders)


class Truck(Vehicle):

    def __init__(self,manu="-",cylinders=0,name="-",iden=0,number="-",load_cap=0,tow_cap=0):
        super().__init__(manu,cylinders,name,iden,number)
        self.load_capacity = load_cap//1
        self.tow_capacity = tow_cap

    def details(self):
        super().details()
        print("Load capacity: ",self.load_capacity,"Tons")
        print("Tow capacity: ",self.tow_capacity,"KG")


class Route:

    def __init__(self,fare,source,destine,travel_time,dist):
        self.fare = fare
        self.travelling_time = travel_time
        self.distance = dist
        self.source = source
        self.destination = destine

    def route_details(self):
        print("\n-Bus route info: ")
        print("Ticket price: Rs.",self.fare)
        print("Source: ",self.source)
        print("Destination: ",self.destination)
        print("Travelling time: ",self.travelling_time,"Minutes")
        print("Distance: ",self.distance,"Km")



class Bus(Vehicle):

    def __init__(self,manu="-",cylinders=0,name="-",iden=0,number="-",passengers=0,luggage=0,route=0):
        super().__init__(manu,cylinders,name,iden,number)
        self.passenger_capacity = passengers
        self.luggage_weight = luggage
        self.route = route

    def route_info(self):
        self.route.route_details()

    def details(self):
        super().details()
        print("Passenger capacity: ",self.passenger_capacity,"People")
        print("Luggage weight capacity: ",self.luggage_weight,"Kg")
        self.route_info()




def main_task1():
    print(" Task 1\n", "-" * 6, end="")
    print()

    truck1 = Truck("Suzuki",6,"Jon",5981,"0322-1562348",100,150)
    truck2 = Truck("Mitsubishi",9,"Anwar",9658,"0655-5984261",200,130)
    truck_list=[truck1,truck2]
    for ele in range(len(truck_list)):
        print("Truck",ele+1,".")
        truck_list[ele].details()
        print()

    route1 = Route(60,"Lahore","karachi",180,19)
    route2 = Route(55,"Karachi","New York",60,11250)
    route3 = Route(25,"New York","Rawalpindi",90,9000)

    bus1 = Bus("Honda",18,"Hame",1689,"5269-2541985",25,125,route1)
    bus2 = Bus("Yamaha",16,"Khalid",2687,"0965-9562158",100,250,route2)
    bus3 = Bus("Suzuki",12,"Jonathan",3658,"0125874569",80,300,route3)

    bus_route=[bus1,bus2,bus3]
    for i in range(0,len(bus_route)):
        print("Bus-Route",i+1,"-")
        bus_route[i].details()
        print()


    print()
main_task1()





# TASK 2


class Player(ABC):
    @abstractmethod
    def __init__(self, name="-", n_matches=0):
        self.name = name
        self.matches = n_matches

    def Display(self):
        print("Player Name: ", self.name)
        print("Number of matches played: ", self.matches)

    def playerType(self):
        pass


class Batsman(Player):

    def __init__(self, name, n_matches):
        super().__init__(name, n_matches)

        self.average = 0  # Leaves Average = 0, to calculates in the, Calculate_age() function

        #  This block takes the players per match scores, and stores them in a list
        print("Number of matches Played by player: ", self.matches)

        score_count_check = 0
        while score_count_check != 1:

            match_scores = input("Please enter Player's scores, in all these matches -> (55 22 66 ...)\n: ")
            input_scores_list = match_scores.split()
            if len(input_scores_list) == self.matches:
                score_count_check = 1
            else:
                print(
                    "Players number of scores not equal to the matches player had played.\nPlease enter scores again..")

        self.per_match_score = input_scores_list

        #  Adds all elements from the players, per match score list. To find the total score.
        self.total_score = reduce(lambda x, y: int(x) + int(y), self.per_match_score)

    def Calculate_avg(self):
        self.average = self.total_score / self.matches
        return self.average

    def playerType(self):
        print("-Batsman-")

    def Display(self):
        super().Display()
        self.playerType()
        print("Per match scores : ")

        for i in range(len(self.per_match_score)):
            print(i + 1, "-", self.per_match_score[i])
        print("Total score : ", self.total_score)
        print("Score Average : %8.2f" % self.Calculate_avg())


class Bowler(Player):

    def __init__(self, name, n_matches):
        super().__init__(name, n_matches)

        #  This block takes the players per match wickets, and stores them in a list
        print("Number of matches Played by player: ", self.matches)

        score_count_check = 0
        while score_count_check != 1:

            match_scores = input("Please enter Player's wickets, in all these matches -> (55 22 66 ...)\n: ")
            input_scores_list = match_scores.split()
            if len(input_scores_list) == self.matches:
                score_count_check = 1
            else:
                print(
                    "Players number of scores not equal to the matches player had played.\nPlease enter scores again..")

        self.per_match_wickets = input_scores_list

        self.total_wickets = reduce(lambda x, y: int(x) + int(y), self.per_match_wickets)  # Gives the sum of a players,
                                                                                           # wickets
    def playerType(self):
        print("-Bowler-")

    def Display(self):
        super().Display()
        self.playerType()
        print("Per match wickets : ")

        for i in range(len(self.per_match_wickets)):
            print(i + 1, "-", self.per_match_wickets[i])
        print("Total  wickets : ", self.total_wickets)


def main_task2():
   print(" Task 2\n","-"*6,end="")
   print()
   batsman1 = Batsman("Buhadar Khan",3)  ##  Will take the score and wickets per matches, as input once run12
   batsman1.Display()
   print()
   bowler1 = Bowler("Sikandar Ali", 4)
   bowler1.Display()



main_task2()


