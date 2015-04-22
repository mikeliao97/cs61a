class Multiples:
    def __init__(self, num):
        self.num = num

    def __iter__(self):
        return MultiplesIterator(self.num)

class MultiplesIterator:
    def __init__(self, num):
        self.num = num
        self.curr = num

    def __iter__(self):
        return self

    def __next__(self):
        if self.curr >= 1000:
            raise StopIteration
        val = self.curr
        self.curr = self.curr + self.num
        return val

