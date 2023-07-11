class Tree:
    """ Abstract base class representing a tree structures """

    # ------------------------------- nested Position class -------------------------------
    class Position:
        """ An abstraction representing the location of a single element """

        def element(self):
            """ Return the element stored at this Postition """
            raise NotImplementedError("Must be implemented by subclass")

        def __eq__(self, other):
            """ Return True if other Position represents the same location."""
            raise NotImplementedError("Must be implemented by subclass")

        def __ne__(self, other):
            """ Return True if other does not represent the same location. """
            return not (self == other)  # opposite of __eq__

    # ---------- abstract methods that concrete subclass must support ----------
    def root(self):
        """Return Position representing the tree s root (or None if empty)  """
        raise NotImplementedError("Must be implemented by subclass")

    def parent(self, p):
        """ Return Position representing p s parent (or None if p is root) """
        raise NotImplementedError("Must be implemented by subclass")

    def num_children(self, p):
        """ Return the number of children that Position p has. """
        raise NotImplementedError("Must be implemented by subclass")

    def children(self, p):
        """ Generate an iteration of Positions representing p s children """
        raise NotImplementedError("Must be implemented by subclass")

    def __len__(self):
        """ Return the total number of elements in the tree """
        raise NotImplementedError("Must be implemented by subclass")

    # ---------- concrete methods implemented in this class ----------
    def is_root(self, p):
        """ Return True if Position p represents the root of the tree """
        return self.root() == p

    def is_leaf(self, p):
        """ Return True if Position p does not have any children  """
        return self.num_children(p) == 0

    def is_empty(self):
        """ Return True if the tree is empty """
        return len(self) == 0


class BinaryTree(Tree):
    """ Abstract base class representing a binary tree structure """

    # --------------------- additional abstract methods ---------------------
    def left(self, p):
        """  Return a Position representing p s left child.
             Return None if p does not have a left child.
        """
        raise NotImplementedError("Must be implemented by subclass")

    def right(self, p):
        """  Return a Position representing p s right child.
             Return None if p does not have a right child.
        """
        raise NotImplementedError("Must be implemented by subclass")

    # ---------- concrete methods implemented in this class ----------
    def sibling(self, p):
        """ Return a Position representing p s sibling (or None if no sibling) """
        parent = self.parent(p)
        if parent is None:  # p must be the root
            return None  # root has no sibling
        else:
            if p == self.left(parent):
                return self.right(parent)  # possibly None
            else:
                return self.left(parent)  # possibly None

    def children(self, p):
        """ Generate an iteration of Positions representing p s children. """
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)


class LinkedBinaryTree(BinaryTree):
    """ Linked representation of a binary tree structure """

    class _Node:  # Lightweight, nonpublic class for storing a node.
        __slots__ = '_element', '_parent', '_left', '_right'

        def __init__(self, element, parent=None, left=None, right=None):
            self._element = element
            self._parent = parent
            self._left = left
            self._right = right

    class Position(BinaryTree.Position):
        """ An abstraction representing the location of a single element """

        def __init__(self, container, node):
            """ Constructor should not be invoked by user """
            self._container = container
            self._node = node

        def element(self):
            """ Return the element stored at this Position """
            return self._node._element

        def __eq__(self, other):
            """ Return True if other is a Position representing the same location """
            return type(other) is type(self) and other._node is self._node

    def _validate(self, p):
        """ Return associated node, if position is valid """
        if not isinstance(p, self.Position):
            raise TypeError("p must be in proper Position type")
        if p._container is not self:
            raise ValueError("p does not belong in this container")
        if p._node._parent is p._node:  # convention for deprecated nodes
            raise ValueError("p is no longer valid")
        return p._node

    def _make_position(self, node):
        """ Return Position instance for given node (or None if no node) """
        return self.Position(self, node) if node is not None else None

    # -------------------------- binary tree constructor --------------------------
    def __init__(self):
        """ Create an initially empty binary tree.””” """
        self._root = None
        self._size = 0

    # -------------------------- public accessors --------------------------
    def __len__(self):
        """ Return the total number of elements in the tree """
        return self._size

    def root(self):
        """ Return the root Position of the tree (or None if tree is empty) """
        return self._make_position(self._root)

    def parent(self, p):
        """ Return the Position of p s parent (or None if p is root) """
        node = self._validate(p)
        return self._make_position(node._parent)

    def left(self, p):
        """ Return the Position of p s left child (or None if no left child). """
        node = self._validate(p)
        return self._make_position(node._left)

    def right(self, p):
        """ Return the Position of p s right child (or None if no right child) """
        node = self._validate(p)
        return self._make_position(node._right)

    def num_children(self, p):
        """ Return the number of children of Position p """
        node = self._validate(p)
        count = 0
        if node._left is not None:  # left child exists
            count += 1
        if node._right is not None:  # right child exists
            count += 1
        return count

    def _add_root(self, e):
        """ Place element e at the root of an empty tree and return new Position.
            Raise ValueError if tree nonempty.
        """

        if self._root is not None: raise ValueError("Root exists")
        self._size = 1
        self._root = self._Node(e)
        return self._make_position(self._root)

    def _add_left(self, p, e):
        """ Create a new left child for Position p, storing element e.
            Return the Position of new node.
            Raise ValueError if Position p is invalid or p already has a left child.
        """

        node = self._validate(p)
        if node._left is not None: raise ValueError("Left child exists")
        self._size += 1
        node._left = self._Node(e, node)  # node is its parent
        return self._make_position(node._left)

    def _add_right(self, p, e):
        """ Create a new right child for Position p, storing element e.
            Return the Position of new node.
            Raise ValueError if Position p is invalid or p already has a right child.
        """

        node = self._validate(p)
        if node._right is not None: raise ValueError("Right child exists")
        self._size += 1
        node._right = self._Node(e, node)  # node is its parent
        return self._make_position(node._right)

    def _replace(self, p, e):
        """ Replace the element at position p with e, and return old element """
        node = self._validate(p)
        old = node._element
        node._element = e
        return old

    def _delete(self, p):
        """ Delete the node at Position p, and replace it with its child, if any.
            Return the element that had been stored at Position p.
            Raise ValueError if Position p is invalid or p has two children.
        """

        node = self._validate(p)
        if self.num_children(p) == 2: raise ValueError("p has 2 children")
        child = node._left if node._left else node._right

        if child is not None:
            child._parent = node._parent  # child s grandparent becomes parent
        if node is self._root:
            self._root = child  # child becomes root
        else:
            parent = node._parent
            if node is parent._left:
                parent._left = child
            else:
                parent._right = child
        self._size -= 1
        node._parent = node  # convention for deprecated node
        return node._element

    def _attach(self, p, t1, t2):
        """ Attach trees t1 and t2 as left and right subtrees of external p """
        node = self._validate(p)
        if not self.is_leaf(p): raise ValueError("position must be leaf")
        if not type(self) is type(t1) is type(t2):  # all 3 trees must be same type
            raise TypeError("Tree types must match")
        self._size += len(t1) + len(t2)
        if not t1.is_empty():  # attached t1 as left subtree of node
            t1._root._parent = node
            node._left = t1._root
            t1._root = None  # set t1 instance to empty
            t1._size = 0
        if not t2.is_empty():  # attached t2 as right subtree of node
            t2._root._parent = node
            node._right = t2._root
            t2._root = None  # set t2 instance to empty
            t2._size = 0


from collections.abc import MutableMapping


class MapBase(MutableMapping):
    """ Our own abstract base class that includes a nonpublic _Item class """

    # ------------------------------- nested Item class -------------------------------
    class _Item:
        """ Lightweight composite to store key-value pairs as map items """
        __slots__ = '_key', '_value', '_hash'

        def __init__(self, k, v):
            self._key = k
            self._value = v
            self._hash = hash(k)

        def __eq__(self, other):
            return self._key == other._key  # compare items based on their keys

        def __ne__(self, other):
            return not (self == other)  # opposite of __eq__

        def __lt__(self, other):
            return self._key < other._key  # compare items based on their keys


class TreeMap(LinkedBinaryTree, MapBase):
    """  """

    # ---------------------------- override Position class ----------------------------

    class Position(LinkedBinaryTree.Position):
        def key(self):
            """  """
            return self.element()._key

        def value(self):
            """  """
            return self.element()._value

    # ------------------------------- nonpublic utilities -------------------------------

    def _subtree_search(self, p, k):
        """  """
        if k == p.key():
            return p
        elif k < p.key():
            if self.left(p) is not None:
                return self._subtree_search(self.left(p), k)

        else:
            if self.right(p) is not None:
                return self._subtree_search(self.right(p), k)

        return p

    def _subtree_first_position(self, p):
        """  """
        walk = p
        while self.left(walk) is not None:
            walk = self.left(walk)
        return walk

    def _subtree_last_position(self, p):
        """  """
        walk = p
        while self.right(walk) is not None:
            walk = self.right(walk)
        return walk

    def first(self):
        """  """
        return self._subtree_first_position(self.root()) if len(self) > 0 else None

    def last(self):
        """  """
        return self._subtree_last_position(self.root()) if len(self) > 0 else None

    def before(self, p):
        """

        """
        self._validate(p)
        if self.left(p):
            return self._subtree_last_position(self.left(p))
        else:
            # walk upward
            walk = p
            above = self.parent(walk)
            while above is not None and walk == self.left(above):
                walk = above
                above = self.parent(walk)
            return above

    def after(self, p):
        """

        """

        self._validate(p)
        if self.left(p):
            return self._subtree_last_position(self.left(p))
        else:
            # walk upward
            walk = p
            above = self.parent(walk)
            while above is not None and walk == self.left(above):
                walk = above
                above = self.parent(walk)
            return above

    def find_position(self, k):
        """  """
        if self.is_empty():
            return None
        else:
            p = self._subtree_search(self.root(), k)
            self._rebalance_access(p)
            return p

    def find_min(self):
        """  """
        if self.is_empty():
            return None
        else:
            p = self.first()
            return (p.key(), p.value())

    def find_ge(self, k):
        """  """

        if self.is_empty():
            return None
        else:
            p = self.find_position(k)
            if p.key() < k:
                p = self.after(p)
            return (p.key, p.value()) if p is not None else None

    def find_range(self, start, stop):
        """  """

        if not self.is_empty():
            if start is None:
                p = self.first()
            else:
                # we initialize p with logic similar to find ge
                p = self.find_position(start)
                if p.key() < start:
                    p = self.after(p)
            while p is not None and (stop is None or p.key() < stop):
                yield (p.key(), p.value())
                p = self.after(p)

    def __getitem__(self, k):
        """  """
        if self.is_empty():
            raise KeyError('Key Error: ' + repr(k))
        else:
            p = self._subtree_search(self.root(), k)
            self._rebalance_access(p)
            if k != p.key():
                raise KeyError('Key Error: ' + repr(k))
            return p.value()

    def __setitem__(self, k, v):
        """  """
        if self.is_empty():
            leaf = self._add_root(self._Item(k, v))
        else:
            p = self._subtree_search(self.root(), k)
            if p.key() == k:
                p.element()._value = v
                self._rebalance_access(p)
                return
            else:
                item = self._Item(k, v)
                if p.key() < k:
                    leaf = self._add_right(p, item)
                else:
                    leaf = self._add_left(p, item)
        self._rebalance_insert(leaf)

    def __iter__(self):
        """  """
        p = self.first()
        while p is not None:
            yield p.key()
            p = self.after(p)

    def delete(self, p):
        """  """
        self._validate(p)
        if self.left(p) and self.right(p):
            replacement = self._subtree_last_position(self.left(p))
            self._replace(p, replacement.element())
            p = replacement
        # now p has at most one child
        parent = self.parent(p)
        self._delete(p)
        self._rebalance_delete(parent)

    def __delitem__(self, k):
        """  """
        if not self.is_empty():
            p = self._subtree_search(self.root(), k)
            if k == p.key():
                self.delete(p)
                return
            self._rebalance_access(p)
        raise KeyError('Key Error: ' + repr(k))

    def _relink(self, parent, child, make_left_child):

        if make_left_child:
            parent._left = child
        else:
            parent._right = child
        if child is not None:
            child._parent = parent

    def _rotate(self, p):

        x = p._node
        y = x._parent
        z = y._parent
        if z is None:
            self._root = x
            x._parent = None
        else:
            self._relink(z,x,y == z._left)

        if x == y._left:
            self._relink(y,x._right,True)
            self._relink(x,y,False)
        else:
            self._relink(y,x._left, False)
            self._relink(x,y,True)

    def _restructure(self,x):

        y = self.parent(x)
        z = self.parent(y)
        if (x == self.right(y)) == (y == self.right(z)):
            self._rotate(y)
            return y
        else:
            self._rotate(x)
            self._rotate(x)
            return x


class AVLTreeMap(TreeMap):
    """  """

    # -------------------------- nested Node class --------------------------
    class _Node(TreeMap._Node):
        """  """
        __slots__ = '_height'

        def __init__(self, element, parent=None, left=None, right=None):
            super().__init__(element, parent, left, right)
            self._height = 0

        def left_height(self):
            return self._left._height if self._right is not None else 0

        def right_height(self):
            return self._right._height if self._right is not None else 0

    # ------------------------- positional-based utility methods -------------------------

    def _recompute_height(self, p):
        p._node._height = 1 + max(p._node.left_height(), p._node.right_height())

    def _isbalanced(self, p):
        return abs(p._node.left_height() - p._node.right_height()) <= 1

    def _tall_child(self, p, favorleft=False):
        if p._node.left_height() + (1 if favorleft else 0) > p._node.right_height():
            return self.left(p)
        else:
            return self.right(p)

    def _tall_grandchild(self, p):
        child = self._tall_child(p)
        # if child is on left, favor left grandchild; else favor right grandchild
        alignment = (child == self.left(p))
        return self._tall_child(child, alignment)

    def _rebalance(self, p):
        while p is not None:
            old_height = p._node._height
            if not self._isbalanced(p):
                # perform trinode restructuring, setting p to resulting root,
                # and recompute new local heights after the restructuring
                p = self._restructure(self._tall_grandchild(p))
                self._recompute_height(self.left(p))
                self._recompute_height(self.right(p))
            self._recompute_height(p)
            if p._node._height == old_height:
                p = None
            else:
                p = self.parent(p)

    # ---------------------------- override balancing hooks ----------------------------

    def _balance_insert(self, p):
        self._rebalance(p)

    def _rebalance_delete(self, p):
        self._rebalance(p)
