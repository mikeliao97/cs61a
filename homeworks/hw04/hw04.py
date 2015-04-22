
def deep_len(lst):
    """Returns the deep length of the list.

    >>> deep_len([1, 2, 3])     # normal list
    3
    >>> x = [1, [2, 3], 4]      # deep list
    >>> deep_len(x)
    4
    >>> x = [[1, [1, 1]], 1, [1, 1]] # deep list
    >>> deep_len(x)
    6
    """
    "*** YOUR CODE HERE ***"
    def inner(lst):
        if(len(lst) == 0):
            return 0 
        elif(type(lst[0]) == list):
            return 0 + inner(lst[0]) + inner(lst[1:])
        else:
            return 1 + inner(lst[1:])
    return inner(lst)

def interval(a, b):
    """Construct an interval from a to b."""
    "*** YOUR CODE HERE ***"
    return [a, b]

def lower_bound(x):
    """Return the lower bound of interval x."""
    "*** YOUR CODE HERE ***"
    return x[0]

def upper_bound(x):
    """Return the upper bound of interval x."""
    "*** YOUR CODE HERE ***"
    return x[1]

def str_interval(x):
    """Return a string representation of interval x.

    >>> str_interval(interval(-1, 2))
    '-1 to 2'
    """
    return '{0} to {1}'.format(lower_bound(x), upper_bound(x))

def add_interval(x, y):
    """Return an interval that contains the sum of any value in interval x and
    any value in interval y.

    >>> str_interval(add_interval(interval(-1, 2), interval(4, 8)))
    '3 to 10'
    """
    lower = lower_bound(x) + lower_bound(y)
    upper = upper_bound(x) + upper_bound(y)
    return interval(lower, upper)

def mul_interval(x, y):
    """Return the interval that contains the product of any value in x and any
    value in y.

    >>> str_interval(mul_interval(interval(-1, 2), interval(4, 8)))
    '-8 to 16'
    """
    p1 = lower_bound(x) * lower_bound(y)
    p2 = lower_bound(x) * upper_bound(y)
    p3 = upper_bound(x) * lower_bound(y)
    p4 = upper_bound(x) * upper_bound(y)
    return interval(min(p1, p2, p3, p4), max(p1, p2, p3, p4))

def div_interval(x, y):
    """Return the interval that contains the quotient of any value in x divided by any value in y.

    Division is implemented as the multiplication of x by the reciprocal of y.

    >>> str_interval(div_interval(interval(-1, 2), interval(4, 8)))
    '-0.25 to 0.5'
    >>> str_interval(div_interval(interval(4, 8), interval(-1, 2)))
    AssertionError
    """
    "*** YOUR CODE HERE ***"
    #assert that y cannot span over zero
    assert lower_bound(y) > 0 and upper_bound(y) > 0 or lower_bound(y) < 0 and upper_bound(y) < 0 
    reciprocal_y = interval(1/upper_bound(y), 1/lower_bound(y))
    return mul_interval(x, reciprocal_y)

def sub_interval(x, y):
    """Return the interval that contains the difference between any value in x
    and any value in y.

    >>> str_interval(sub_interval(interval(-1, 2), interval(4, 8)))
    '-9 to -2'
    """
    "*** YOUR CODE HERE ***"
    p1 = lower_bound(x) - lower_bound(y)
    p2 = lower_bound(x) - upper_bound(y)
    p3 = upper_bound(x) - lower_bound(y)
    p4 = upper_bound(x) - upper_bound(y)
    return interval(min(p1, p2), max(p3, p4))

def par1(r1, r2):
    return div_interval(mul_interval(r1, r2), add_interval(r1, r2))

def par2(r1, r2):
    one = interval(1, 1)
    rep_r1 = div_interval(one, r1)
    rep_r2 = div_interval(one, r2)
    return div_interval(one, add_interval(rep_r1, rep_r2))

# These two intervals give different results for parallel resistors:
"*** YOUR CODE HERE ***"
r1 = [1, 3]
r2 = [1, 5]
"""
for these values
par1 range: [0.125, 7.5]
par2 range: [0.5, 1.875]
This is due to different tolerance ranges
"""

def multiple_references_explanation():
    return """The mulitple reference is true
    in my testing. par1 created a range of [0.125, 7.5]
    while par2 range created a ranged of [0.5, 1.875]. par 2 created a
    range that is much tighter. This is because par1 referred to same (r1, r2)
    many more times. In par1, the calculations have to first
    mul_interval(r1, r2), add_interval(r1,r2), and then divide
    the intervals. Each time r1, r2 is passed into these functions
    the interval becomes larger and larger(mul, divide takes the largest
    interval possible). Thus the interval becomes huge. 
    
    On the other hand, the arguments in par2 are separated--meaning r1,r2
    are not passed in at the same time. When they are passed in at the same
    time, the function usually returns the max of the range. In par2 r1,
    r2 are merely divided by 1, which doesn't have the same expanding effect.
    """

def quadratic(x, a, b, c):
    """Return the interval that is the range of the quadratic defined by
    coefficients a, b, and c, for domain interval x.

    >>> str_interval(quadratic(interval(0, 2), -2, 3, -1))
    '-3 to 0.125'
    >>> str_interval(quadratic(interval(1, 3), 2, -3, 1))
    '0 to 10'
    """
    "*** YOUR CODE HERE ***"
    def q_func(value):
        return a * (value * value) + b * value + c
    
    lower = min(q_func(lower_bound(x)), q_func(upper_bound(x)))
    upper = max(q_func(lower_bound(x)), q_func(upper_bound(x)))

    #This is the extreme point 
    extreme_point = -b / (2 * a)
    extreme_value = False #sentinel

    #if the extreme point is given in the value caluclate the extreme value
    if(extreme_point < upper_bound(x) and extreme_point > lower_bound(x)):
        extreme_value = q_func(extreme_point)
    if(extreme_value and extreme_value < lower):
        lower = extreme_value
    if(extreme_value and extreme_value > upper):
        upper = extreme_value

    return interval(lower, upper)





def polynomial(x, c):
    """Return the interval that is the range of the polynomial defined by
    coefficients c, for domain interval x.

    >>> str_interval(polynomial(interval(0, 2), [-1, 3, -2]))
    '-3 to 0.125'
    >>> str_interval(polynomial(interval(1, 3), [1, -3, 2]))
    '0 to 10'
    >>> str_interval(polynomial(interval(0.5, 2.25), [10, 24, -6, -8, 3]))
    '18.0 to 23.0'
    """
    "*** YOUR CODE HERE ***"


