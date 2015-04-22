def g(n):
    """Return the value of G(n), computed recursively.

    >>> g(1)
    1
    >>> g(2)
    2
    >>> g(3)
    3
    >>> g(4)
    10
    >>> g(5)
    22
    """
    "*** YOUR CODE HERE ***"
    if(n <= 3):
        return n
    else:
        return g(n - 1) + 2 * g(n - 2) + 3 *  g(n - 3)

def g_iter(n):
    """Return the value of G(n), computed iteratively.

    >>> g_iter(1)
    1
    >>> g_iter(2)
    2
    >>> g_iter(3)
    3
    >>> g_iter(4)
    10
    >>> g_iter(5)
    22
    """
    "*** YOUR CODE HERE ***"
    #I realized the iterative version is equal to 3 + 2 * g(n - 2) + 3 g(n - 3) 
    # the second and third terms are multiplied n - 3 times, and it decrements in the while loop
    second_term, third_term = 0, 0 
    if(n <= 3):
        return n
    else:
        while(n > 3):
            second_term += 2 * (n - 2)
            third_term += 3 * (n - 3)
            n -= 1

    return second_term + third_term + 3




def pingpong(n):
    """Return the nth element of the ping-pong sequence.

    >>> pingpong(7)
    7
    >>> pingpong(8)
    6
    >>> pingpong(15)
    1
    >>> pingpong(21)
    -1
    >>> pingpong(22)
    0
    >>> pingpong(30)
    6
    >>> pingpong(68)
    2
    >>> pingpong(69)
    1
    >>> pingpong(70)
    0
    >>> pingpong(71)
    1
    >>> pingpong(72)
    0
    >>> pingpong(100)
    2
    """
    "*** YOUR CODE HERE ***"
    #1 means the direction is going up
    #-1 means the direction is going down
    def inner(i, direction, value):
        if(i == n):
            return value
        elif(has_seven(i) or i % 7 == 0):
            direction = -1 * direction
            return inner(i + 1, direction, value + direction)
        else:
            return inner(i + 1, direction, value + direction)

    return inner(1, 1, 1)


def has_seven(k):
    """Returns True if at least one of the digits of k is a 7, False otherwise.

    >>> has_seven(3)
    False
    >>> has_seven(7)
    True
    >>> has_seven(2734)
    True
    >>> has_seven(2634)
    False
    >>> has_seven(734)
    True
    >>> has_seven(7777)
    True
    """
    if k % 10 == 7:
        return True
    elif k < 10:
        return False
    else:
        return has_seven(k // 10)


def count_change(amount):
    """Return the number of ways to make change for amount.

    >>> count_change(7)
    6
    >>> count_change(10)
    14
    >>> count_change(20)
    60
    >>> count_change(100)
    9828
    """
    "*** YOUR CODE HERE ***"
    #The coins can't be bigger than the recent_big_coin passed in
    def inner(amount, recent_big_coin):
        total = 0 #total tracks the number of combinations

        #the biggest coin is based off the recent_big_coin that is passed in, we don't want duplicate combinations
        #one way of eliminating duplicates is making sure that the biggest coin can't be bigger than the previous big coin
        biggest_coin = recent_big_coin 
                
        if(amount == 0): #we have a combination
            return 1
        if(amount < 0): #missed the combination
            return 0
        else:
            while(biggest_coin >= 1):
                total += inner(amount - biggest_coin, biggest_coin) #aggregates the different types of coin combinations
                biggest_coin = biggest_coin // 2 #divides biggest coins by two. for example 8, 4, 2, 1... until 0 stops the while loop
        return total

    biggest_coin = find_biggest_coin(amount) #finds the biggest coin based off the initial amount
    return inner(amount, biggest_coin)
#this function returns the biggest coin that is power of two
def find_biggest_coin(amount):
    biggest_coin =1
    while(biggest_coin <= amount):
        biggest_coin = biggest_coin * 2
    return biggest_coin // 2

def print_move(origin, destination):
    """Print instructions to move a disk."""
    print("Move the top disk from rod", origin, "to rod", destination)

def move_stack(n, start, end):
    """Print the moves required to move n disks on the start pole to the end
    pole without violating the rules of Towers of Hanoi.

    n -- number of disks
    start -- a pole position, either 1, 2, or 3
    end -- a pole position, either 1, 2, or 3

    There are exactly three poles, and start and end must be different. Assume
    that the start pole has at least n disks of increasing size, and the end
    pole is either empty or has a top disk larger than the top n start disks.

    >>> move_stack(1, 1, 3)
    Move the top disk from rod 1 to rod 3
    >>> move_stack(2, 1, 3)
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 3
    >>> move_stack(3, 1, 3)
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 1 to rod 2
    Move the top disk from rod 3 to rod 2
    Move the top disk from rod 1 to rod 3
    Move the top disk from rod 2 to rod 1
    Move the top disk from rod 2 to rod 3
    Move the top disk from rod 1 to rod 3
    """
    assert 1 <= start <= 3 and 1 <= end <= 3 and start != end, "Bad start/end"
    "*** YOUR CODE HERE ***"
    if(n == 1):
        print_move(start, end)
    elif(n < 1):
        return 
    else:
        move_stack(n - 1, start, 6 - end - start) 
        print_move(start, end)
        move_stack(n - 1, 6 - end - start, end )

from operator import sub, mul

def make_anonymous_factorial():
    """Return the value of an expression that computes factorial.

    >>> make_anonymous_factorial()(5)
    120
    """
    return 'YOUR_EXPRESSION_HERE'

