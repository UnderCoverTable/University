from _queue import Empty


class PriorityQueueBase:
    """ Lightweight composite to store priority queue items """

    class _Item:
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

    def heap_print(self):
        for i in range(len(self._data)):
            print(self._data[i]._key, self._data[i]._value)

    ## TASK 2
    def heappushpop(self, k, v):

        self._data.append(self._Item(k, v))                             # Add new key, value

        if self._data[0]._key > self._data[len(self._data) - 1]._key:   # If the new value is smaller then the root,
            removed_new_item = self._data.pop()                         # we can simply pop and return the value.
            return (removed_new_item._key, removed_new_item._value)
        else:
            removed_old_root = self.remove_min()                # else, we call remove min, which removes the smallest,
            return removed_old_root                             # value and downheaps.
    ## TASK 3
    def heapreplace(self, k, v):

        self._swap(0, len(self._data) - 1)
        rem = self._data.pop()                  # pop the smallest key

        self._data.append(self._Item(k, v))     # Add new key

        if k < rem._key:
            self._swap(0, len(self._data) - 1)      # if the new key is smaller then the one , just removed,
        else:                                      # we simply swap the new value with the root, currently having the largest key.
            self._swap(0, len(self._data) - 1)
            self._downheap(0)                      # else, we swap the values and then downheap

        return (rem._key, rem._value)


test_heap = HeapPriorityQueue()
test_heap.add(5, "A")
test_heap.add(8, "D")
test_heap.add(6, "U")
test_heap.add(9, "p")
test_heap.add(12, "S")


print(test_heap.heappushpop(7,"T"))
print(test_heap.heapreplace(1,"X"))
