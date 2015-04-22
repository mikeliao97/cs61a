def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n - 2) + fib(n - 1)

def count(f):
    def counted(n):
        counted.call_count += 1
        return f(n)
    counted.call_count  = 0
    return counted

def memo(f):
    cache = {}
    def memoized(n):
        if n not in cache:
            cache[n] = f(n)
        return cache[n]
    return memoized

class Tree:
    def __init__(self, entry, branches = ()):
        self.entry = entry #root value
        for b in branches:
            assert isinstance(b, Tree)
        self.branches = list(branches)

    def __repr__(self):
        if not self.branches:
            branches_repr = ""
        else:
            branches_repr = ', ' + repr(self.branches)
        return 'Tree({0}{1})'.format(self.entry, branches_repr)

