from _queue import Empty
from random import *


class PriorityQueueBase:
    """ Abstract base class for a priority queue """

    class _Item:
        """ Lightweight composite to store priority queue items """
        __slots__ = '_key', '_value'

        def __init__(self, k, v):
            self._key = k
            self._value = v

        def __lt__(self, other):
            return self._key < other._key  # compare items based on their keys

    def is_empty(self):  # concrete method assuming abstract len
        """ Return True if the priority queue is empty """
        return len(self) == 0


class HeapPriorityQueue(PriorityQueueBase):
    """ A min-oriented priority queue implemented with a binary heap """
    """  """

    # ------------------------------ nonpublic behaviors ------------------------------
    def _parent(self, j):
        return (j - 1) // 2

    def _left(self, j):
        return 2 * j + 1

    def _right(self, j):
        return 2 * j + 2

    def _has_left(self, j):
        return self._left(j) < len(self._data)  # index beyond end of list?

    def _has_right(self, j):
        return self._right(j) < len(self._data)  # index beyond end of list?

    def _swap(self, i, j):
        """ Swap the elements at indices i and j of array """
        self._data[i], self._data[j] = self._data[j], self._data[i]

    def _upheap(self, j):
        parent = self._parent(j)
        if j > 0 and self._data[j] < self._data[parent]:
            self._swap(j, parent)
            self._upheap(parent)  # recur at position of parent

    def _downheap(self, j):
        if self._has_left(j):
            left = self._left(j)
            small_child = left  # although right may be smaller
            if self._has_right(j):
                right = self._right(j)
                if self._data[right] < self._data[left]:
                    small_child = right

            if self._data[small_child] < self._data[j]:
                self._swap(j, small_child)
                self._downheap(small_child)  # recur at position of small child

    # ------------------------------ public behaviors ------------------------------
    def __init__(self):
        """ Create a new empty Priority Queue """
        self._data = []

    def __len__(self):
        """ Return the number of items in the priority queue. """
        return len(self._data)

    def add(self, key, value):
        """ Add a key-value pair to the priority queue """
        self._data.append(self._Item(key, value))
        self._upheap(len(self._data) - 1)  # upheap newly added position

    def min(self):
        """
            Return but do not remove (k,v) tuple with minimum key.
            Raise Empty exception if empty.
        """
        if self.is_empty():
            raise Empty("Priority queue is empty")
        item = self._data[0]
        return (item._key, item._value)

    def remove_min(self):
        """
        Remove and return (k,v) tuple with minimum key.
        Raise Empty exception if empty.
        """

        if self.is_empty():
            raise Empty("Priority queue is empty")
        self._swap(0, len(self._data) - 1)  # put minimum item at the end
        item = self._data.pop()  # and remove it from the list;
        self._downheap(0)  # then fix new root
        return (item._key, item._value)

    def list_of_objs(self):
        """ Helper function for the simulation. Returns a list of all values, from the key,value pair
            currently in the heap.
        """

        objs = []
        for item in self._data:
            objs.append(item._value)
        return objs


class Jobs:
    newid = 0

    def __init__(self):
        self._id = Jobs.newid
        Jobs.newid += 1
        self._length = randint(1, 100)
        self._priority = randint(-20, 19)
        self._time_waiting = 0


class CPU:

    def __init__(self):
        self._job_queue = HeapPriorityQueue()
        self._processor = []  # Only 1 job at a time in this list.
        self.times_list = []  # Stores the waiting time of each job

        self.done_jobs = 0  # tracks number of jobs completed
        self._print_check = 0

    def add_job(self):
        """ Adds a job the heap, with 4% probability"""
        if 96 < randint(1, 100) <= 100:
            new_job = Jobs()
            self._job_queue.add(new_job._priority, new_job)

    def update_job_queue(self):
        """ When the processor is empty and a job is waiting in the queue,
            the job is removed from the heap and added to the processor.
            The jobs waiting time (before being serviced) is then added to the, _times_list.
        """

        if len(self._processor) == 0 and len(self._job_queue) >= 1:
            rem = self._job_queue.remove_min()
            self._processor.append(rem)
            self.times_list.append(rem[1]._time_waiting)

    def update_processor(self):
        """ The job in processor has its length -1.
            And if after that, length = 0, its removed from the processor.
        """

        if len(self._processor) == 1:
            self._processor[0][1]._length -= 1

            if self._processor[0][1]._length == 0:
                a = self._processor.pop()
                print("Job", a[1]._id, " finished.")

                self.done_jobs += 1
                self._print_check = 0

    def jobs_being_processed(self):
        """ Prints out the job ID and initial length. _print_check stops it from printing,
            the job and length in each time slice.
            Returns the id and length of ID.
         """

        if len(self._processor) == 1 and self._print_check == 0:
            cur = self._processor[0]
            print("Job", cur[1]._id, "is being processed.", "Needs,", cur[1]._length, ",time slices.")
            self._print_check = 1

        elif len(self._processor) == 1:
            cur = self._processor[0]
            return cur[1]._id, cur[1]._length

    def update_wait_times(self):
        """ Updates(+1) the _time_waiting variable of each item in the heap """

        li = self._job_queue.list_of_objs()
        for items in li:
            items._time_waiting += 1


def graph_wait_time(data, avg):
    """ Histogram of the waiting times and the average waiting time """

    import matplotlib.pyplot as plt

    plt.ylabel("Jobs")
    plt.xlabel("Time slices")

    plt.hist(data, label="Wait before service", color="c", range=[min(data), max(data)])
    plt.axvline(avg, color='k', linestyle='dashed', linewidth=1, label="Average time slices \nspent waiting (%.2f)" % avg)

    plt.legend()
    plt.grid(True)
    plt.show()


def simulation():
    test = CPU()
    final_job = None

    for time_slice in range(10081):
        test.add_job()
        test.update_job_queue()
        if time_slice == 10080:     # Stores job being run in last time slice.
            final_job = test.jobs_being_processed()
        else:
            test.jobs_being_processed()

        test.update_processor()
        test.update_wait_times()

    if final_job is not None:   # Prints the final job and the time remaining.
        print("Job", final_job[0], "was interrupted with,", final_job[1], "time slices remaining.")
    print()

    print("Jobs completed: ", test.done_jobs)
    print("Jobs left in queue: ", len(test._job_queue))

    avg_wait = (sum(test.times_list) / len(test.times_list))
    print("Average time spent before service: %.2f" % avg_wait, "slices")

    graph_wait_time(test.times_list, avg_wait)


simulation()
