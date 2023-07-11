from random import *


class Animal:
    def __init__(self, gen=" ", strength=0):
        self.gender = gen
        if self.gender == " ":
            self.gender = choice(["M", "F"])
        self.strength = strength
        if self.strength == 0:
            self.strength = randint(0, 10)

    def get_gender(self):
        return self.gender

    def get_strength(self):
        return self.strength

    def get_specie(self):
        pass

    def animal_bio(self):
        return [self.get_specie(), self.gender, self.strength]

    def locate_animal(self, river, direction):
        """
        Locates the indices of the animal and the one besides it.
        Returns the indices and the info of the animals
        """

        animal_location = river.index(self)
        animal = river[animal_location]  # Animal object

        if direction == 1:  # Decides direction
            animal_adjacent_location = animal_location + 1
        else:
            animal_adjacent_location = animal_location - 1

        animal_adjacent = river[animal_adjacent_location]  # Adjacent animal object

        if animal_adjacent is not None:
            ani_adja_info = animal_adjacent.animal_bio()  # Adjacent animal info
        else:
            ani_adja_info = animal_adjacent  # In case of the adjacent spot being empty. It stays None

        ani_info = animal.animal_bio()  # Animal info

        return [ani_info, animal_location, ani_adja_info, animal_adjacent_location]

    def move(self, river, direction):
        """
        Uses the animals from function, locate animals.  And resolves their movements
        Left or Right depending on the direction input
        """

        all_info = self.locate_animal(river, direction)

        animal_location = all_info[1]
        animal = river[animal_location]
        ani_info = all_info[0]

        animal_adjacent_location = all_info[3]
        animal_adjacent = river[animal_adjacent_location]
        ani_adja_info = all_info[2]

        if type(animal) == type(animal_adjacent):
            # If type is same. Then either fight or mate
            if ani_info[1] == ani_adja_info[1]:

                # FIGHT
                loser_strength = (lambda x, y: x if x <= y else y)(ani_info[2], ani_adja_info[2])
                if loser_strength == ani_info[2]:
                    river[animal_location] = None
                else:
                    river[animal_location] = None
                    river[animal_adjacent_location] = animal

            else:  # MATE
                if ani_info[0] == "Bear":
                    offspring = Bear()
                else:
                    offspring = Fish()

                none_check = [i for i in river if i is None]  # Creates a list of empty spaces
                if len(none_check) > 0:

                    index = river.index(choice(none_check))

                    river[index] = offspring
                else:
                    return "END"  # No empty spaces left, ending program

        else:  # EAT FISH / MOVE
            if ani_adja_info is None or ani_info[0] == "Bear":
                river[animal_adjacent_location] = animal
                river[animal_location] = None

            else:
                river[animal_location] = None


class Fish(Animal):
    def __init__(self, gen=" ", strength=0):
        super().__init__(gen, strength)

    def get_specie(self):
        return "Fish"


class Bear(Animal):
    def __init__(self, gen=" ", strength=0):
        super().__init__(gen, strength)

    def get_specie(self):
        return "Bear"


def populate_river():
    river = []
    for animals in range(10000):
        animal_specie = random()

        if animal_specie < 0.02:
            river.append(Bear())

        if 0.02 <= animal_specie <= 0.52:
            river.append(Fish())

        if animal_specie > 0.52:
            river.append(None)

    return river


def census(river):
    fishes = 0
    bears = 0
    empties = 0

    for ii in range(len(river) - 1):
        if river[ii] is None:
            empties += 1
        elif river[ii].get_specie() == "Fish":
            fishes += 1
        else:
            bears += 1

    return [fishes, bears, empties]


def resolve_collisions(d_list, river_list, direction):
    """
    Resolves the collisions according to the list the object comes from.
     Moves the animals right or left.
    """
    for go in range(0, len(d_list)):
        if d_list[go] in river_list:
            end_check = d_list[go].move(river_list, direction)
            if end_check == "END":
                return "Stop"


def plot_points(pop_list, plot_fish, plot_bear, plot_empty):
    """
    Collects the points for the graph
    """

    plot_fish.append(pop_list[0])
    plot_bear.append(pop_list[1])
    plot_empty.append(pop_list[2])

    return [plot_fish, plot_bear, plot_empty]


def graph(all_pop_list):
    import matplotlib.pyplot as plt
    import numpy as np

    plt.ylabel("Population")
    plt.xlabel("Step")

    plt.plot(all_pop_list[0], label="Fish")
    plt.plot(all_pop_list[1], label="Bear")
    plt.plot(all_pop_list[2], label="Empty spaces")

    plt.yticks(np.arange(0, 11000, 1000))

    plt.legend()
    plt.show()


def simulation():
    river_eco = populate_river()
    fish_population, bear_population, empty_population = [], [], []

    pop_data = census(river_eco)
    plot_points(pop_data, fish_population, bear_population, empty_population)
    print("Initial Population:", "\n", "Fishes: ", pop_data[0], "\n", "Bears: ", pop_data[1], "\n", "Empty: ",
          pop_data[2])

    for step in range(100000):
        go_right = []
        go_left = []
        for movement in range(0, len(river_eco) - 1):

            decide = randint(0, 1)  # Move or not
            '''
            Adds the animal object to go_right or go_left depending on the direction they were 
            going to move
            '''
            if decide != 0 and river_eco[movement] is not None:
                direction = randint(0, 1)
                if direction == 1:
                    go_right.append(river_eco[movement])
                else:
                    go_left.append(river_eco[movement])

        if resolve_collisions(go_right, river_eco, 1) or \
                resolve_collisions(go_left, river_eco, 0) == "Stop":
            '''
            In case no empty spaces are left. Simulation ends.
            '''
            pop_data3 = census(river_eco)
            b = plot_points(pop_data3, fish_population, bear_population, empty_population)
            graph(b)

            print("Final Population:", "\n", "Fishes: ", pop_data3[0], "\n", "Bears: ", pop_data3[1], "\n", "Empty: ",
                  pop_data3[2])
            return

        pop_data2 = census(river_eco)
        a = plot_points(pop_data2, fish_population, bear_population, empty_population)
    graph(a)

    print("Final Population:", "\n", "Fishes: ", pop_data2[0], "\n", "Bears: ", pop_data2[1], "\n", "Empty: ",
          pop_data2[2])


for total_runs in range(5):
    print(total_runs + 1)
    simulation()
    print("-" * 5)
