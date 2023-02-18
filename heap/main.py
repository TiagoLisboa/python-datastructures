from array import array


class Heap():
    list: array

    def __init__(self):
        self.list = []

    def len(self):
        return len(self.list)

    def insert(self, value):
        # insert at end
        self.list.append(value)

        self.heapify_bottom_up(self.len()-1)

    def heapify_bottom_up(self, pos):
        parent = int((pos-1)/2)

        if self.list[parent] > 0:
            if self.list[pos] > self.list[parent]:
                self.list[pos], self.list[parent] = self.list[parent], self.list[pos]

                self.heapify_bottom_up(parent)

    def extract_max(self):
        max = self.list[0]
        self.list[0] = self.list[-1]
        self.list.pop(-1)
        self.heapify_top_down(0)

        return max

    def heapify_top_down(self, pos):
        largest = pos
        l = 2 * pos + 1
        r = 2 * pos + 2

        if l  < len(self.list) and self.list[l] > self.list[largest]:
            largest = l

        if r  < len(self.list) and self.list[r] > self.list[largest]:
            largest = r

        if largest != pos:
            self.list[pos], self.list[largest] = self.list[largest], self.list[pos]

            self.heapify_top_down(largest)

