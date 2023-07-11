from collections import deque
from random import *


class Airplane:

    def __init__(self):
        self.time_need = randint(1, 3)  # The time a plan will need to either land or takeoff. 1-3
        self.time_spent_inqueue = 0     # Keeps track of the number of minutes spent in a queue

    def get_needed_time(self):
        return self.time_need


class Airport:

    def __init__(self):
        self.landing_queue = deque()  # Created 3 deques. For landing, takeoff and runway
        self.takeoff_queue = deque()
        self.runway = deque()       # Length of runway never exceeds 1

        self.landing_rate = 0
        self.takeoff_rate = 0

        self.landing_rate_check = 0
        self.takeoff_rate_check = 0

        self.landing_queue_time_spent = []      # Keep track of the time each plane spend in the landing queue
        self.takeoff_queue_time_spent = []      # Keep track of the time each plane spend in the takeoff queue

        self.num_planes_landing = []        # Keeps track of the total number of planes added to the landing queue
        self.num_planes_takeoff = []        # Keeps track of the total number of planes added to the takeoff queue

    def rates(self):
        """ Used to calculate random takeoff and landing rates """
        self.landing_rate = randint(0, 30)
        self.takeoff_rate = randint(0, 30)

    def rate_checkers(self):
        """ Used to calculate random takeoff and landing rates """
        self.landing_rate_check = random()
        self.takeoff_rate_check = random()

    def add_landing_queue(self):
        """ Adds a plane to the landing queue if the rates are met """
        if len(self.landing_queue) == self.landing_queue.maxlen:
            self.landing_queue.extend([None])                   # If the queue is full then it is extended

        if self.landing_rate / 60 > self.landing_rate_check:
            self.landing_queue.appendleft(Airplane())

            self.num_planes_landing.append(1)       # Keeps track of the total number of planes landing

    def add_takeoff_queue(self):
        """ Adds a plane to the takeoff queue if the rates are met """
        if len(self.takeoff_queue) == self.takeoff_queue.maxlen:
            self.takeoff_queue.extend([None])                   # If the queue is full then it is extended

        if self.takeoff_rate / 60 > self.takeoff_rate_check:
            self.takeoff_queue.appendleft(Airplane())

            self.num_planes_takeoff.append(1)        # Keeps track of the total number of planes taking off

    def time_spent_update(self, q):
        """ Updates the time_spent_inqueue variable. To keep track of the time spend in the respective queue"""
        if len(q) >= 1:
            for i in range(len(q) - 1):
                q[i].time_spent_inqueue = q[i].time_spent_inqueue + 1

    def is_queue_empty(self, which_queue):
        """ Returns whether a queue is empty or not """
        if which_queue == "landing":
            return len(self.landing_queue) == 0
        if which_queue == "takeoff":
            return len(self.takeoff_queue) == 0
        if which_queue == "runway":
            return len(self.runway) == 0

    def add_runway_queue(self):
        """ Adds a plane from either the landing or takeoff queue to the runway queue """

        if self.is_queue_empty("runway") is True and len(self.landing_queue) >= 1:  # If the runway is empty and landing
            plane_at_front_landing = self.landing_queue.pop()                      # queue has a plane, its added to the
            self.runway.appendleft(plane_at_front_landing)                          # runway queue.

            self.landing_queue_time_spent.append(plane_at_front_landing.time_spent_inqueue)
            # To keep track of the time each plane spent in the landing queue.

        if self.is_queue_empty("runway") and self.is_queue_empty("landing") is True and len(self.takeoff_queue) >= 1:
            plane_at_front_takeoff = self.takeoff_queue.pop()       # If the runway and ladning queue is empty, and the
            self.runway.appendleft(plane_at_front_takeoff)      # takeoff queue has a plane. It is added to the runway.

            self.takeoff_queue_time_spent.append(plane_at_front_takeoff.time_spent_inqueue)
            # To keep track of the time each plane spent in the landing queue.

    def clear_runway(self):
        """ Removes a plane from the runway, once it uses up the time it needed """
        if self.is_queue_empty("runway") is True:
            return
        plane_on_runway = self.runway[0]
        if plane_on_runway.get_needed_time() == 0:
            self.runway.pop()       # Plane is removed from the runway
        else:
            plane_on_runway.time_need = plane_on_runway.time_need - 1   # Reduces the time, that the plane needed
            if plane_on_runway.get_needed_time() == 0:                  # to either takeoff or land.
                self.runway.pop()


def simulation():
    test = Airport()
    landing_size = [0]
    takeoff_size = [0]
    for i in range(1, 10081):  # Runs for 10080 minutes.( 1 week )

        test.rate_checkers()  # Updates landing_rate_check and takeoff_rate_check every iteration(every minute)

        if i == 1 or i % 60 == 0:  # Updates landing_rate_check and takeoff_rate_check every 60 minutes
            test.rates()

        if i % 1440 == 0:  # To get the number of planes being landed and taking off daily.
            landing_size.append(len(test.num_planes_landing))
            takeoff_size.append(len(test.num_planes_takeoff))
        # Functions are called, to begin the simulation.
        test.add_landing_queue()
        test.add_takeoff_queue()
        test.add_runway_queue()

        test.time_spent_update(test.landing_queue)
        test.time_spent_update(test.takeoff_queue)

        test.clear_runway()

    # Assigns and calculates the avg times and lengths of the queues and planes.
    landing_times, takeoff_times = test.landing_queue_time_spent, test.takeoff_queue_time_spent
    num_landed_planes, num_takeoff_planes = len(test.num_planes_landing), len(test.num_planes_takeoff)

    avg_time_landing = sum(landing_times) / num_landed_planes
    avg_time_takeoff = sum(takeoff_times) / num_takeoff_planes

    avg_len_landing = num_landed_planes / 7
    avg_len_takeoff = num_takeoff_planes / 7

    print("After running 1 week (10080 minutes), the statistics are: \n")
    print("Average time spent in Landing Queue: %.2f" % avg_time_landing, "Minutes")
    print("Average time spent in Takeoff Queue: %.2f" % avg_time_takeoff, "Minutes\n")

    print("Average Daily Length of Landing Queue: %d" % avg_len_landing)
    print("Average Daily Length of Takeoff Queue: %d" % avg_len_takeoff)

    graph_avg_len(landing_size, takeoff_size)
    graph_avg_time(landing_times, takeoff_times, avg_time_landing, avg_time_takeoff)


def graph_avg_len(ll, tl):
    """ Makes a line graph for the daily increase in length of both queues """
    import matplotlib.pyplot as plt

    plt.ylabel("Length of Queue")
    plt.xlabel("Day")

    plt.plot(ll, label="Length of landing Queue", color="orange")
    plt.plot(tl, label="Length of Takeoff Queue", color="c")

    plt.xlim(1, 7)

    plt.legend()
    plt.grid(True)
    plt.show()


def graph_avg_time(lt, tt, avg_l, avg_t):
    """ Makes 2 histograms for the time the planes spent in their queues """
    import matplotlib.pyplot as plt

    plt.figure(figsize=(9, 3))

    # Landing Queue histogram
    plt.subplot(131)
    plt.hist(lt, label="Time spent in landing queue", range=[min(lt), max(lt)],color="orange")

    plt.axvline(avg_l, color='k', linestyle='dashed', linewidth=1, label="Average time spent")

    plt.ylabel("Planes")
    plt.xlabel("Time spent in queue / Minutes")

    plt.legend(fontsize=6)
    plt.grid(True)

    # Takeoff queue histogram
    plt.subplot(132)
    plt.hist(tt, label="Time spent in takeoff queue", color="c", range=[min(tt), max(tt)])

    plt.axvline(avg_t, color='k', linestyle='dashed', linewidth=1, label="Average time spent")

    plt.ylabel("Planes")
    plt.xlabel("Time spent in queue / Minutes")

    plt.legend(fontsize=5)
    plt.grid(True)

    plt.show()


simulation()
