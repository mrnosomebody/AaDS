class Iterator:
    def __init__(self, data):
        self.data = data
        self.it = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.it + 1 == len(self.data):
            raise StopIteration
        self.it += 1
        return self.data[self.it] * 10


class Seq:
    def __init__(self, data):
        self.data = data

    def __iter__(self):
        return Iterator(self.data)


sequence = Seq([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
for i in sequence:
    print(i)

for i in sequence:
    print(i)
