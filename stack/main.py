from linkedlist.main import LinkedList


class Stack():
    list: LinkedList = LinkedList()

    def len(self):
        return self.list.len()

    def push(self, value):
        self.list.add(value)

    def pop(self):
        self.list.remove(self.list._last._index)
