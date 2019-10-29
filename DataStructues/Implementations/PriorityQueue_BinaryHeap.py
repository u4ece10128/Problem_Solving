# Priority Q using binary heap implementation O(logn)

class BinaryHeap():
    def __init__(self):
        self.items = [0]  # initialize to zero, so the actual list starts index from 1

    def __len__(self):
        return len(self.items) - 1

    def percolate_up(self):
        i = len(self)
        while i // 2 > 0:
            if self.items[i] < self.items[i // 2]: # if a child node < parent node
                self.items[i // 2], self.items[i] = self.items[i], self.items[i // 2]  # swap them
            i = i // 2

    def insert(self, k):
        self.items.append(k)
        self.percolate_up()

    def delete_min(self):
        return_value = self.items[1]  # return the minimum value
        self.items[1] = self.items[len(self)] # swap last nodes vale to the root node
        self.items.pop() # remove the last entry
        self.percolate_down(1) # move the root node to maitain the heap property
        return return_value

    def min_child(self, i):
        if 2*i > len(self):  # if only node of the parent
            return 2*i
        if self.items[2*i] < self.items[2*i + 1]:
            return 2*i
        return (2*i) + 1

    def percolate_down(self, i):
        while 2*i > len(self):
            mc = self.min_child(i)
            if self.items[i] > self.items[mc]:
                self.items[i] ,self.items[mc] = self.items[mc], self.items[i]
            i = mc

    def build_heap(self, alist):
        i = len(alist) // 2  # parent nodes
        self.items = [0] + alist
        while i > 0:
            self.percolate_down(i)
            i = i - 1
