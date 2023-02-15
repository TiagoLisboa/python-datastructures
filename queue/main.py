from linkedlist.main import LinkedList


class Queue():
    list: LinkedList

    def __init__(self) -> None:
        self.list = LinkedList()

    def len(self):
        return self.list.len()

    def enqueue(self, value):
        self.list.add(value)

    def dequeue(self):
        self.list.remove(self.list._first._index)

    def front(self):
        return self.list._last.value

    def __str__(self) -> str:
        return self.list.__str__()
