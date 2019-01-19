import math

def heap_sort(l):
    h = Heap(l)
    h.build_max_heap()

    while (h.size != 0):
        max = h.extract_max()
        h.elements[h.size] = max
        h.max_heapify(0)

    return h.elements

class Heap:
    def __init__(self, elements):
        self.elements = elements
        self.size = len(elements)

    def extract_max(self):
        result = self.elements[0]
        self.elements[0] = self.elements[self.size - 1]
        self.size -= 1

        self.max_heapify(0)

        return result

    def insert(self, elt):
        if (self.size >= self.size):
            self.elements.append(- math.inf)
        else:
            self.elements[self.size] = - math.inf

        self.size += 1
        self.increase_key(self.size - 1, elt)

    def increase_key(self, i, v):
        self.elements[i] = v
        self.adjust(i)
        

    def adjust(self, i):
        elt = self.get_key(i)
        i = self.size - 1

        while (elt > self.elements[self.parent(i)] and i > 0):
            self.elements[i] = self.get_key(self.parent(i))
            i = self.parent(i)
        
        self.elements[i] = elt

    def build_max_heap(self):
        i = self.size // 2 - 1
        while (i >= 0):
            self.max_heapify(i)
            i -= 1
        
    def max_heapify(self, i):
        l = self.get_key(self.left(i))
        r = self.get_key(self.right(i))
        t = self.get_key(i)

        if (t < l or t < r):
            if (l > r):
                self.elements[i] = l
                self.elements[self.left(i)] = t

                self.max_heapify(self.left(i))
            else:
                self.elements[i] = r
                self.elements[self.right(i)] = t

                self.max_heapify(self.right(i))

    def left(self, i):
        return 2 * (i + 1) - 1

    def right(self, i):
        return 2 * (i + 1)

    def parent(self, i):
        return (i + 1) // 2 - 1

    def get_key(self, i):
        if i >= self.size:
            return - math.inf
        return self.elements[i]

    def __str__(self):
        result = ""
        i = 0
        l = 1
        j = 0
        while (i < self.size):
            line1 = ""
            while(i < self.size and j < l):
                line1 += str(self.elements[i]) + " "
                i += 1
                j += 1

            result += line1 + "\n\n"
            l *= 2
            j = 0

        return result

print(heap_sort([6, 4, 2, 7, 18, 54, 23, 10, 3]))