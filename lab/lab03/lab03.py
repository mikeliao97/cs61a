# Q1
def skip_add(n):
    """ Takes a number x and returns x + x-2 + x-4 + x-6 + ... + 0.

    >>> skip_add(5)  # 5 + 3 + 1 + 0
    9
    >>> skip_add(10) # 10 + 8 + 6 + 4 + 2 + 0
    30
    """
    "*** YOUR CODE HERE ***"
    total = 0
    while n >= 0:
        total += n
        n -= 2
    return total



# Q6
def gcd(a, b):
    """Returns the greatest common divisor of a and b.
    Should be implemented using recursion.

    >>> gcd(34, 19)
    1
    >>> gcd(39, 91)
    13
    >>> gcd(20, 30)
    10
    >>> gcd(40, 40)
    40
    """
    "*** YOUR CODE HERE ***"
    if(a % b == 0 or b % a == 0):
        return min(a,b)
    else:
        return gcd(min(a,b), max(a,b) % min(a,b))


# Q7
def hailstone(n):
    """Print out the hailstone sequence starting at n, and return the
    number of elements in the sequence.

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
    if(n == 1):
        print(n)
        return 1
    if(n % 2 == 0):
        print(n)
        return 1 + hailstone(n // 2)
    else:
        print(n)
        return 1 + hailstone(n * 3 + 1)



# Q8
def is_palindrome(n):
    """
    Fill in the blanks '_____' to check if a number
    is a palindrome.

    >>> is_palindrome(12321)
    True
    >>> is_palindrome(42)
    False
    >>> is_palindrome(2015)
    False
    >>> is_palindrome(55)
    True
    """
    x, y = n, 0
    f = lambda: y * 10 + x % 10 
    while x > 0:
        x, y = x // 10, f()
    return y == n

