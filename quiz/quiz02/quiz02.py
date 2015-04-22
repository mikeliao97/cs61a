from tree import *

x = tree(-1, [tree(1),
              tree(-2),
              tree(3, [tree(-4),
                       tree(-5)])])
y = tree(1, [tree(-1, [tree(2)]),
             tree( 8, [tree(-7)]),
             tree(-3, [tree(-3)]),
             tree(-4, [tree(3),
                       tree(-5),
                       tree(7, [tree(-4),
                                tree(-2)])])])

def subtreesum(t):
    """Return the maximum sum of any tree-consistent subset of nodes in t.

    >>> subtreesum(tree(5))
    5
    >>> subtreesum(tree(-5, [tree(6)]))
    6
    >>> subtreesum(tree(-5, [tree(6, [tree(-2)])]))
    4
    >>> subtreesum(tree(-2))
    0

    >>> subtreesum(x)
    1
    >>> subtreesum(y)
    7
    >>> subtreesum(tree(20, branches(y))) # Max sum includes all nodes
    11
    """
    "*** YOUR CODE HERE ***"
#for each tree's subbranches check if each subbranch is worth
#if its worth return the node elsejust return some of the subbranches

#if t is a leaf

#if t has one branch, check if the branches(root) + t(root) > 0. return that
#if t has multiple branches, check if t(root) + branches(root) > 0, return t(root)


    if(is_leaf(t) and treesum(t) < 0):
        return 0
    elif(is_leaf(t) and treesum(t) > 0):
        return treesum(t)
    else:
        branchez = branches(t)
        sum_branches = sum([treesum(b) for b in branchez])
        if(root(t) + sum_branches > sum_branches and root(t) + sum_branches > 0):
            return root(t) + sum_branches
        else:
            return sum([subtreesum(b) for b in branchez])



def treesum(t):
    """Return the sum of all node values in t."""
    return root(t) + sum([treesum(b) for b in branches(t)])


class Mint:
    """A mint creates coins by stamping on years.

    The update method sets the mint's stamp to Mint.current_year.

    >>> mint = Mint()
    >>> mint.year
    2015
    >>> dime = mint.create(Dime)
    >>> dime.year
    2015
    >>> Mint.current_year = 2100  # Time passes
    >>> nickel = mint.create(Nickel)
    >>> nickel.year     # The mint has not updated its stamp yet
    2015
    >>> nickel.worth()  # 5 cents + (85 - 50 years)
    40
    >>> mint.update()   # The mint's year is updated to 2100
    >>> Mint.current_year = 2175     # More time passes
    >>> mint.create(Dime).worth()    # 10 cents + (75 - 50 years)
    35
    >>> Mint().create(Dime).worth()  # A new mint has the current year
    10
    >>> dime.worth()     # 10 cents + (160 - 50 years)
    120
    >>> Dime.cents = 20  # Upgrade all dimes!
    >>> dime.worth()     # 20 cents + (160 - 50 years)
    130
    """
    current_year = 2015

    def __init__(self):
        self.minted = []
        self.update()

    def create(self, kind):
        "*** YOUR CODE HERE ***"
        #calls the coin init method
        coin = kind(self.year)
        return coin

    def update(self):
        "*** YOUR CODE HERE ***"
        self.year = self.current_year
class Coin:
    def __init__(self, year):
        self.year = year

    def worth(self):
        "The worth is a coin's face value + 1 cent for each year over age 50."
        "*** YOUR CODE HERE ***"
        year_gap = Mint.current_year - self.year
        if(year_gap > 50):
            return self.cents + (year_gap - 50)
        else:
            return self.cents

class Nickel(Coin):
    cents = 5

class Dime(Coin):
    cents = 10

