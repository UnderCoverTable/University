from time import time

class _DoublyLinkedBase:
    """
    A base class providing a doubly linked list representation
    """

    class _Node:
        __slots__ = '_element', '_prev', '_next'

        def __init__(self, element, prev, next):
            self._element = element  # users element
            self._prev = prev  # previous node reference
            self._next = next  # next node reference

    def __init__(self):
        """ Create an empty list """
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._header._next = self._trailer  # trailer is after header
        self._trailer._prev = self._header  # header is before trailer
        self._size = 0  # number of elements

    def __len__(self):
        """Return the number of elements in the list  """
        return self._size

    def is_empty(self):
        """Return True if list is empty  """
        return self._size == 0

    def _insert_between(self, e, predecessor, successor):
        """ Add element e between two existing nodes and return new node """
        newest = self._Node(e, predecessor, successor)  # linked to neighbors
        predecessor._next = newest
        successor._prev = newest
        self._size += 1
        return newest

    def _delete_node(self, node):
        """  Delete non-sentinel node from the list and return its element"""
        predecessor = node._prev
        successor = node._next

        predecessor._next = successor
        successor._prev = predecessor
        self._size -= 1
        element = node._element  # record deleted element
        node._prev = node._next = node._element = None  # deprecate node
        return element  # return deleted element

    # TASK 2
    def reverse(self):
        current_node = self._header
        while current_node:
            previous_node = current_node._prev

            current_node._prev = current_node._next
            current_node._next = previous_node
            current_node = current_node._prev

        head = self._header
        self._header = self._trailer
        self._trailer = head


class PositionalList(_DoublyLinkedBase):
    """  A sequential container of elements allowing positional access"""

    # -------------------------- nested Position class --------------------------
    class Position:
        """ An abstraction representing the location of a single element """

        def __init__(self, container, node):
            """ Constructor should not be invoked by user """
            self._container = container
            self._node = node

        def element(self):
            """  Return the element stored at this Position """
            return self._node._element

        def __eq__(self, other):
            """ Return True if other is a Position representing the same location. """
            return type(other) is type(self) and other._node is self._node

        def __ne__(self, other):  # Not Equal
            """ Return True if other does not represent the same location """
            return not (self == other)  # opposite of __eq__

    # ------------------------------- utility method -------------------------------

    def _validate(self, p):
        """ Return position s node, or raise appropriate error if invalid """

        if not isinstance(p, self.Position):
            raise TypeError("p must be proper position type")
        if p._container is not self:
            raise ValueError("p does not belong to this container")
        if p._node._next is None:  # convention for deprecated nodes
            raise ValueError("p is no longer valid")
        return p._node

    # ------------------------------- utility method -------------------------------

    def _make_position(self, node):
        """Return Position instance for given node (or None if sentinel)  """
        if node is self._header or node is self._trailer:
            return None  # boundary violation
        else:
            return self.Position(self, node)  # legitimate position

    # ------------------------------- accessors -------------------------------

    def first(self):
        """Return the first Position in the list (or None if list is empty) """
        return self._make_position(self._header._next)

    def last(self):
        """  Return the last Position in the list (or None if list is empty)"""
        return self._make_position(self._trailer._prev)

    def before(self, p):
        """ Return the Position just before Position p (or None if p is first) """
        node = self._validate(p)
        return self._make_position(node._prev)

    def after(self, p):
        """ Return the Position just after Position p (or None if p is last) """
        node = self._validate(p)
        return self._make_position(node._next)

    def __iter__(self):
        """ Generate a forward iteration of the elements of the list """
        cursor = self.first()
        while cursor is not None:
            yield cursor.element()
            cursor = self.after(cursor)

    # ------------------------------- mutators -------------------------------
    # override inherited version to return Position, rather than Node

    def _insert_between(self, e, predecessor, successor):
        """ Add element between existing nodes and return new Position """
        node = super()._insert_between(e, predecessor, successor)
        return self._make_position(node)

    def add_first(self, e):
        """ Insert element e at the front of the list and return new Position """
        return self._insert_between(e, self._header, self._header._next)

    def add_last(self, e):
        """ Insert element e at the back of the list and return new Position """
        return self._insert_between(e, self._trailer._prev, self._trailer)

    def add_before(self, p, e):
        """ Insert element e into list before Position p and return new Position """
        original = self._validate(p)
        return self._insert_between(e, original._prev, original)

    def add_after(self, p, e):
        """  Insert element e into list after Position p and return new Position"""
        original = self._validate(p)
        return self._insert_between(e, original, original._next)

    def delete(self, p):
        """Remove and return the element at Position p  """
        original = self._validate(p)
        return self._delete_node(original)  # inherited method returns element

    def replace(self, p, e):
        """ Replace the element at Position p with e.
        Return the element formerly at Position p. """
        original = self._validate(p)
        old_value = original._element  # temporarily store old element
        original._element = e  # replace with new element
        return old_value  # return the old element value

    def print_list(self):
        node = self._header
        while node:
            print(node._element)
            node = node._next

    # TASK 3
    def swap(self, p, q):
        p_node = self._validate(p)
        q_node = self._validate(q)
                                    # Creating variables for all the
        ahead_p = p_node._next      ## nessecary nodes
        behind_p = p_node._prev

        ahead_q = q_node._next
        behind_q = q_node._prev

        next_of_p1 = behind_p._next
        prev_of_p2 = ahead_p._prev

        next_of_q1 = q_node._prev._next
        prev_of_q2 = q_node._next._prev
        # ------------------------------------------------

        if p_node._next == q_node:  # When p and q are adjacent

            behind_p._next = ahead_p
            q_node._next._prev = behind_q

            q_node._next = next_of_p1
            q_node._prev = behind_p

            p_node._next = ahead_q
            p_node._prev = prev_of_q2
        # ------------------------------------------------
        elif p_node._prev == q_node:
            print("**")
            behind_q._next = ahead_q
            p_node._next._prev = behind_p

            q_node._next = ahead_p
            q_node._prev = ahead_p._prev

            p_node._next = behind_q._next
            p_node._prev = behind_q

        # -------------------------------------------------
        else:  # p and q not adjacent

            behind_p._next = next_of_q1
            q_node._prev._next = next_of_p1

            ahead_p._prev = prev_of_q2
            q_node._next._prev = prev_of_p2

            p_node._next = q_node._next
            p_node._prev = q_node._prev

            q_node._next = ahead_p
            q_node._prev = behind_p


## TASK 4
def bubble_sort(PL):
    for i in range(len(PL)):
        node = PL._validate(PL.first())
        node_next = node._next

        for j in range(len(PL)):

            if node_next._element is None:
                break

            if node._element > node_next._element:
                PL.swap(PL._make_position(node), PL._make_position(node_next))

            node = node_next
            node_next = node_next._next
    PL.print_list()


def task2():
    print("\n TASK 2")
    pl = PositionalList()
    p1 = pl.add_first(1)
    p2 = pl.add_after(p1, 2)
    p3 = pl.add_after(p2, 3)
    p4 = pl.add_after(p3, 4)
    p5 = pl.add_last(5)

    pl.reverse()
    pl.print_list()


def task3():
    print("\n TASK 3")
    pl = PositionalList()
    p1 = pl.add_first(1)
    p2 = pl.add_after(p1, 2)
    p3 = pl.add_after(p2, 3)
    #p4 = pl.add_after(p3, 4)
    #p5 = pl.add_last(5)

    pl.swap(p3,p2)
    #pl.swap(p2,p3)
    #pl.swap(p4, p2)
    pl.print_list()


def task4(): # 0.0221 sec runtime
    print("\n TASK 4")
    pl = PositionalList()
    p1 = pl.add_first(2)
    p2 = pl.add_after(p1, 6)
    p3 = pl.add_after(p2, 3)
    p4 = pl.add_after(p3, 7)
    p5 = pl.add_last(1)

    start = time()
    bubble_sort(pl)
    end = time()
    print("Elapsed Time:", end - start)
    


#task2()
task3()
#task4()
