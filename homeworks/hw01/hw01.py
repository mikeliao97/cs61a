from operator import add, sub


def a_plus_abs_b(a, b):
    """Return a+abs(b), but without calling abs.

    >>> a_plus_abs_b(2, 3)
    5
    >>> a_plus_abs_b(2, -3)
    5
    """
    if b < 0:
        f = sub
    else:
        f = add

    return f(a, b)


def two_of_three(a, b, c):
    """Return x*x + y*y, where x and y are the two largest members of the
    positive numbers a, b, and c.

    >>> two_of_three(1, 2, 3)
    13
    >>> two_of_three(5, 3, 1)
    34
    >>> two_of_three(10, 2, 8)
    164
    >>> two_of_three(5, 5, 5)
    50
    """
    "*** YOUR CODE HERE ***"
    return pow(a, 2) + pow(b,2) + pow(c,2) - pow(min(a,b,c),2)


def largest_factor(n):
    """Return the largest factor of n*n-1 that is smaller than n.

    >>> largest_factor(4) # n*n-1 is 15; factors are 1, 3, 5, 15
    3
    >>> largest_factor(9) # n*n-1 is 80; factors are 1, 2, 4, 5, 8, 10, ...
    8
    """
    "*** YOUR CODE HERE ***"
    if(n > 1):
        target = n * n - 1
        for i in range(n - 1, 1, -1):
            if(target % i == 0):
                return i



def if_function(condition, true_result, false_result):
    """Return true_result if condition is a true value, and
    false_result otherwise.

    >>> if_function(True, 2, 3)
    2
    >>> if_function(False, 2, 3)
    3
    >>> if_function(3==2, 3+2, 3-2)
    1
    >>> if_function(3>2, 3+2, 3-2)
    5
    """
    if condition:
        return true_result
    else:
        return false_result

#with if statment returns 1
def with_if_statement():
    """
    >>> with_if_statement()
    1
    """
    if c():
        return t()
    else:
        return f()
#with if_function does not it can do anything else
#My Thinking
#with_if_statement calls the functions directly because the functions are global.
#with_if_function passess the functions to if_function(...,...,...), and then
#sees what happen
def with_if_function():
    return if_function(c(), t(), f())

def c():
    "*** YOUR CODE HERE ***"
    return False 

def t():
    "*** YOUR CODE HERE ***"
    raise ArgumentError

def f():
    "*** YOUR CODE HERE ***"
    return 1


def hailstone(n):
    """Print the hailstone sequence starting at n and return its
    length.

    >>> a = hailstone(10)
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    "*** YOUR CODE HERE ***"
    length = 1 
    while(n != 1):
        if(n % 2 == 0):
            print(int(n))
            n = n /2
            length = length + 1
        else:
            print(int(n))
            n = n * 3 + 1
            length = length + 1
    print(1)
    return int(length)


challenge_question_program = """
"*** YOUR CODE HERE ***"
"""


