#implementation of linked list not using classes
empty = 'empty'

def link(first, rest):
    return [first, rest]


def first(s):
    return s[0]

def rest(s):
    return s[1]

def len_link(s):
    x = 0
    while s!= empty:
        s, x = rest(s), x + 1
    return x

def getitem_link(s, i):
    while i > 0:
        s, i = rest(s), i - 1
    return first(s)

def extend(s, t):
    assert is_link(s) and is_link(t)
    if s == empty:
        return t
    else:
        return link(first(s), extend(rest(s), t))

def apply_to_all_link(f,s):
    if s == empty:
        return s
    else:
        return link(f(first(s)), apply_to_all_link(f, rest(s)))
























#where s is the list, and i is the element
def get_item_link(s,i):
    if i == 0:
        return first(s)
    else:
        return get_item_link(rest(s), i - 1)

def getitem_link(s,i):
    while i > 0:
        s, i = rest(s), i - 1
    return first(s)

#you want to add t next to s
def extend(s,t):
    if(s == empty):
        return t
    else:
        return link(first(s), extend(rest(s), t))
def apply_to_all_link(f,s):
    if(s == empty):
        return s
    else:
        return link(f(first(s)), apply_to_all_link(f, rest(s)))

#Memoization
def memo(f):
    cache = {}
    def memoized(n):
        if n not in cache:
            cache[n] = f(n)
        return cache[n]
    return memoized



class Link:
    empty = ()
    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest
    def __getitem__(self, i):
        if(i == 0):
            return self.first
        else:
            return self.rest[i - 1]
    def __len__(self):
        return 1 + len(self.rest)

def link_expression(s):
    """Return a string that would evaluate to s."""
    if s.rest is Link.empty:
        rest = ""
    else:
        rest = ", " + link_expression(s.rest)
    return 'Link{0}{1}'.format(s.first, rest)

def partitions(n, m):
    if n == 0:
        return Link(Link.empty)
    elif n < 0 or m == 0:
        return Link.empty
    else:
        using_m = partitions(n - m , m)
        with_m = map_link(lambda s: Link(m, s), using_m)
        without_m = partitions(n, m - 1)
        return with_m + without_m 


