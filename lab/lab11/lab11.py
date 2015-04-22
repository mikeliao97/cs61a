#= ############
# Iterators #
#############

# Q2
class IteratorRestart:
    """
    >>> iterator = IteratorRestart(2, 7)
    >>> for num in iterator:
    ...     print(num)
    2
    3
    4
    5
    6
    7
    >>> for num in iterator:
    ...     print(num)
    2
    3
    4
    5
    6
    7
    """
    def __init__(self, start, end):
        "*** YOUR CODE HERE ***"
        self.start = start - 1
        self.end = end
        self.permanent_start = start - 1


    def __next__(self):
        if self.start >= self.end:
            self.start = self.permanent_start
            raise StopIteration
        self.start += 1
        return self.start

    def __iter__(self):
        return self


# Q3
class Str:
    """
    >>> s = Str("hello")
    >>> for char in s:
    ...     print(char)
    ...
    h
    e
    l
    l
    o
    >>> for char in s:    # a standard iterator does not restart
    ...     print(char)
    """
    "*** YOUR CODE HERE ***"
    def __init__(self, str):
        self.start = -1
        self.end = len(str) - 1
        self.str = str

    def __next__(self):
        if self.start >= self.end:
            raise StopIteration
        self.start += 1
        return self.str[self.start]

    def __iter__(self):
        return self


##############
# Generators #
##############

# Q4
def countdown(n):
    """
    >>> from types import GeneratorType
    >>> type(countdown(0)) is GeneratorType # countdown is a generator
    True
    >>> for number in countdown(5):
    ...     print(number)
    ...
    5
    4
    3
    2
    1
    0
    """
    "*** YOUR CODE HERE ***"
    while n >= 0:
        yield n
        n = n - 1 

class Countdown:
    """
    >>> from types import GeneratorType
    >>> type(Countdown(0)) is GeneratorType # Countdown is an iterator
    False
    >>> for number in Countdown(5):
    ...     print(number)
    ...
    5
    4
    3
    2
    1
    0
    """
    "*** YOUR CODE HERE ***"
    def __init__(self, start):
        self.start = start + 1

    def __next__(self):
        if(self.start <= 0):
            raise StopIteration
        self.start -= 1
        return self.start

    def __iter__(self):
        return self

# Q5
def hailstone(n):
    """
    >>> for num in hailstone(10):
    ...     print(num)
    ...
    10
    5
    16
    8
    4
    2
    1
    """
    "*** YOUR CODE HERE ***"
    while n != 1:
        yield int(n)
        if(n % 2 == 0):
            n = n / 2
        else:
            n = n * 3 + 1
    yield int(n)


