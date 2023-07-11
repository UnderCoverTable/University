from _queue import Empty


##TASK 1
class ArrayQueue:
    DEFAULT_CAPACITY = 10

    def __init__(self):

        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __len__(self):

        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):

        if self.is_empty():
            raise Empty('Queue is empty')
        return self._data[self._front]

    def dequeue(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        answer = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        return answer

    def enqueue(self, e):
        if self._size == len(self._data):
            self.resize(2 * len(self._data))
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1

    def resize(self, cap):
        old = self._data
        self._data = [None] * cap
        walk = self._front
        for k in range(self._size):
            self.data[k] = old[walk]
            walk = (1 + walk) % len(old)
        self._front = 0

    def queue_status(self):
        return self._data


##TASK 2
class LinkedQueue:
    class _Node:
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._head._element

    def dequeue(self):

        if self.is_empty():
            raise Empty('Queue is empty')
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.is_empty():
            self._tail = None
        return answer

    def enqueue(self, e):
        newest = self._Node(e, None)
        if self.is_empty():
            self._head = newest
        else:
            self._tail._next = newest
        self._tail = newest
        self._size += 1


##TASK 3
class ArrayStack:

    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def push(self, e):
        self._data.append(e)

    def top(self):
        if self.is_empty():
            raise Empty("Stack is empty")
        return self._data[-1]

    def pop(self):
        if self.is_empty():
            raise Empty("Stack is empty")
        return self._data.pop()


def task3(s, x):
    print("TASK 3")

    q = ArrayQueue()
    check = 0

    for ele in range(s.__len__()):
        q.enqueue(s.pop())

    for ele1 in range(q.__len__()):
        s.push(q.dequeue())

    for ele2 in range(s.__len__()):
        q.enqueue(s.pop())

    for ele3 in range(q.__len__()):
        removed = q.dequeue()
        s.push(removed)
        if removed == x:
            check = 1

    if check == 1:
        return True
    else:
        return False


test_stack = ArrayStack()
for i in range(1, 4):
    test_stack.push(i)

print(task3(test_stack, 7))
print(task3(test_stack, 2))


##TASK 4

class Deque:
    DEFAULT_CAPACITY = 10

    def __init__(self):
        self._data = [None] * Deque.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def queue_status(self):
        return self._data

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):

        if self.is_empty():
            raise Empty('Queue is empty')
        return self._data[self._front]

    def last(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        return self._data[self._front + self._size - 1]

    def add_first(self, e):
        """""
        Adding e to the end of the queue, then swapping everything 1 place to the right
        """""
        if self._size == len(self._data):
            self.resize(2 * len(self._data))
        avail = (self._front - 1)
        self._data[avail] = e
        self._size += 1
        self._data = self._data[-1:] + self._data[:-1]

    def add_last(self, e):
        """""
        Same as Enqueue
        """""
        if self._size == len(self._data):
            self.resize(2 * len(self._data))
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1

    def delete_first(self):
        """""
        Same as dequeue
        """""
        if self.is_empty():
            raise Empty('Queue is empty')
        answer = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        return answer

    def delete_last(self):
        if self.is_empty():
            raise Empty('Queue is empty')
        answer = self._data[self._size - 1]
        self._data[self._size - 1] = None
        self._size -= 1
        return answer

    def resize(self, cap):
        old = self._data
        self._data = [None] * cap
        walk = self._front
        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (1 + walk) % len(old)
        self._front = 0


def task4():
    print("\nTASK 4")
    d = Deque()
    d.add_last(5)
    d.add_first(3)
    d.add_first(7)
    print(d.first())
    print(d.delete_last())
    print(d.__len__())
    print(d.delete_last())
    print(d.delete_last())
    d.add_first(6)
    print(d.last())
    d.add_first(8)
    print(d.is_empty())
    print(d.last())
    print(d.queue_status())


task4()
