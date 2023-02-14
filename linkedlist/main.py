class Node():
    _index: int
    value: any
    _next: 'Node'

    def __init__(self, index, value):
        self._index = index
        self.value = value
        self._next = None

    def next(self):
        return self._next

class LinkedList():
    _first: Node
    _last: Node

    def __init__(self):
        self._first = None
        self._last = None

    def add(self, item):
        if not self._first:
            self._first = Node(index=0, value=item)
            self._last = self._first
        else:
            self._last._next = Node(index=self._last._index+1, value=item)
            self._last = self._last._next

    def first(self) -> Node:
        return self._first

    def last(self) -> Node:
        return self._last

    def index(self, index) -> Node:
        item = self._first

        while item._index != index:
            item = item.next()
            if not item:
                break

        return item

    def len(self) -> int:
        return self._last._index + 1

    def remove(self, index):
        previous = self.index(index - 1)
        item = previous.next()
        next = item.next()
        previous._next = next
        next = previous._next

        if not next:
            self._last = previous

        while next:
            next._index = next._index - 1
            next = next.next()


