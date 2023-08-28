from collections.abc import Collection


class HashTable(Collection):
    def __init__(self, capacity=10):
        self.items = [...] * capacity
        self.size = 0

    def __contains__(self, item):
        return item in self.items

    def __len__(self):
        return len(self.items)

    def __iter__(self):
        for i in range(len(self.items)):
            if self.items[i] is Ellipsis:
                continue

            for j in range(len(self.items[i])):
                yield self.items[i][j]

    def add(self, value):
        index = abs(hash(value) % len(self.items))
        if self.items[index] is not Ellipsis:
            self.items[index].append(value)

        else:
            self.items[index] = [value]

        self.size += 1


a = HashTable(5)
a.add(2)
a.add(4)
a.add(-5)
a.add(10)
print(a.items, a.size)
b = iter(a)
print(b.__next__())
print(b.__next__())
print(b.__next__())
print(b.__next__())
