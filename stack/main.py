from linkedlist.main import LinkedList


class Stack():
    list: LinkedList

    def __init__(self) -> None:
        self.list = LinkedList()

    def len(self):
        return self.list.len()

    def push(self, value):
        self.list.add(value)

    def pop(self):
        self.list.remove(self.list._last._index)

    def peek(self):
        return self.list._last.value

    def __str__(self) -> str:
        return self.list.__str__()
