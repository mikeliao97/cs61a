##############################################################
# An alternative implementation of the tree data abstraction #
##############################################################

def tree(root, branches=[]):
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'
    return {'<root>': root, '<branches>': branches}

def root(tree):
    return tree['<root>']

def branches(tree):
    return tree['<branches>']

def is_tree(tree):
    if type(tree) != dict or '<root>' not in tree or '<branches>' not in tree:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    return not branches(tree)

def print_tree(t, indent=0):
    """Print a representation of this tree in which each node is
    indented by two spaces times its depth from the root.

    >>> print_tree(tree(1))
    1
    >>> print_tree(tree(1, [tree(2)]))
    1
      2
    >>> print_tree(numbers)
    1
      2
      3
        4
        5
      6
        7
    """
    print('  ' * indent + str(root(t)))
    for branch in branches(t):
        print_tree(branch, indent + 1)

###########
# Mobiles #
###########

def mobile(left, right):
    """Construct a mobile from a left side and a right side."""
    return tree(None, [left, right])

def sides(m):
    """Select the sides of a mobile."""
    return branches(m)

def side(length, mobile_or_weight):
    """Construct a side: a length of rod with a mobile or weight at the end."""
    return tree(length, [mobile_or_weight])

def length(s):
    """Select the length of a side."""
    return root(s)

def end(s):
    """Select the mobile or weight hanging at the end of a side."""
    return branches(s)[0]

def weight(size):
    """Construct a weight of some size."""
    assert size > 0
    "*** YOUR CODE HERE ***"
    return tree(size) 

def size(w):
    """Select the size of a weight."""
    "*** YOUR CODE HERE ***"
    return root(w) 

def is_weight(w):
    """Whether w is a weight, not a mobile."""
    "*** YOUR CODE HERE ***"
    return not sides(w) 

def examples():
    t = mobile(side(1, weight(2)),
               side(2, weight(1)))
    u = mobile(side(5, weight(1)),
               side(1, mobile(side(2, weight(3)),
                              side(3, weight(2)))))
    v = mobile(side(4, t), side(2, u))
    return (t, u, v)


def total_weight(m):
    """Return the total weight of m, a weight or mobile.

    >>> t, u, v = examples()
    >>> total_weight(t)
    3
    >>> total_weight(u)
    6
    >>> total_weight(v)
    9
    """
    if is_weight(m):
        return size(m)
    else:
        return sum([total_weight(end(s)) for s in sides(m)])

def with_totals(m):
    """Return a mobile with total weights stored as the root of each mobile.

    >>> t, u, v = examples()
    >>> print_tree(t)
    None
      1
        2
      2
        1
    >>> print_tree(with_totals(t))
    3
      1
        2
      2
        1
    >>> print_tree(t)  # t should not change
    None
      1
        2
      2
        1
    >>> print_tree(with_totals(v))
    9
      4
        3
          1
            2
          2
            1
      2
        6
          5
            1
          1
            5
              2
                3
              3
                2
    >>> print_tree(v)  # v should not change
    None
      4
        None
          1
            2
          2
            1
      2
        None
          5
            1
          1
            None
              2
                3
              3
                2
    """
    "*** YOUR CODE HERE ***"
    #okay so you have to return the whole tree but call total_weight for mobile
    #if there are no more branches and its a weight return itj
    if is_weight(m): 
        return m
    else:
        side_branches = sides(m)
        #mobiles have two side branches
        if(len(side_branches) == 2): #if b has sides that means its not a weight
             return tree(total_weight(m), [with_totals(s) for s in sides(m)])
        else:
             return tree(length(m), [with_totals(s) for s in sides(m)])

    """
     t = mobile(side(1, weight(2)),
               side(2, weight(1)))
    """

def balanced(m):
    """Return whether m is balanced.

    >>> t, u, v = examples()
    >>> balanced(t)
    True
    >>> balanced(v)
    True
    >>> w = mobile(side(3, t), side(2, u))
    >>> balanced(w)
    False
    >>> balanced(mobile(side(1, v), side(1, w)))
    False
    >>> balanced(mobile(side(1, w), side(1, v)))
    False
    """
    "*** YOUR CODE HERE ***"
    #if its a weight then stop
    if(is_weight(m)):
        return True
    else:
        side_b = sides(m) #this gets the sides
        if(len(side_b) == 2): #this means that its a mobile
            if(collect_weights(side_b[0]) * length(side_b[0]) != collect_weights(side_b[1]) * length(side_b[1])):
                return False
            return balanced(side_b[0]) and balanced(side_b[1])
        else: #this means that its a length
            return balanced(side_b[0])
    


def collect_weights(m):
    if(is_weight(m)):
        return size(m)
    else:
        return sum([collect_weights(b) for b in sides(m)])



############
# Mutation #
############

def make_withdraw(balance, password):
    """Return a password-protected withdraw function.

    >>> w = make_withdraw(100, 'hax0r')
    >>> w(25, 'hax0r')
    75
    >>> w(90, 'hax0r')
    'Insufficient funds'
    >>> w(25, 'hwat')
    'Incorrect password'
    >>> w(25, 'hax0r')
    50
    >>> w(75, 'a')
    'Incorrect password'
    >>> w(10, 'hax0r')
    40
    >>> w(20, 'n00b')
    'Incorrect password'
    >>> w(10, 'hax0r')
    "Your account is locked. Attempts: ['hwat', 'a', 'n00b']"
    >>> w(10, 'l33t')
    "Your account is locked. Attempts: ['hwat', 'a', 'n00b']"
    """
    "*** YOUR CODE HERE ***"
    incorrect_attempts = []
    def withdraw(amount, open_sesame):
        nonlocal incorrect_attempts
        nonlocal balance
        if(len(incorrect_attempts) == 3):
            error_message = "Your account is locked. Attempts: " + str(incorrect_attempts) 
            return error_message 
        elif(open_sesame != password):
            incorrect_attempts.append(open_sesame)
            return 'Incorrect password'
        else:
            if amount > balance:
                return 'Insufficient funds'
            balance = balance - amount
            return balance
    return withdraw


def make_joint(withdraw, old_password, new_password):
    """Return a password-protected withdraw function that has joint access to
    the balance of withdraw.

    >>> w = make_withdraw(100, 'hax0r')
    >>> w(25, 'hax0r')
    75
    >>> make_joint(w, 'my', 'secret')
    'Incorrect password'
    >>> j = make_joint(w, 'hax0r', 'secret')
    >>> w(25, 'secret')
    'Incorrect password'
    >>> j(25, 'secret')
    50
    >>> j(25, 'hax0r')
    25
    >>> j(100, 'secret')
    'Insufficient funds'

    >>> j2 = make_joint(j, 'secret', 'code')
    >>> j2(5, 'code')
    20
    >>> j2(5, 'secret')
    15
    >>> j2(5, 'hax0r')
    10

    >>> j2(25, 'password')
    'Incorrect password'
    >>> j2(5, 'secret')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    >>> j(5, 'secret')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    >>> w(5, 'hax0r')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    >>> make_joint(w, 'hax0r', 'hello')
    "Your account is locked. Attempts: ['my', 'secret', 'password']"
    """
    "*** YOUR CODE HERE ***"
    #this function returns a withdraw account
    password_set = [old_password]
    def joint_account(balance, password):
        if(password in password_set):
            return withdraw(balance, password_set[0])
        else:
            return withdraw(balance, password) 
    
    response = withdraw(0, old_password)
    if(type(response) != str): #if it is successful
       password_set.append(new_password) #append a new password
       return joint_account 
    else:
        return response 

###########
# Objects #
###########

class VendingMachine:
    """A vending machine that vends some product for some price.

    >>> v = VendingMachine('candy', 10)
    >>> v.vend()
    'Machine is out of stock.'
    >>> v.restock(2)
    'Current candy stock: 2'
    >>> v.vend()
    'You must deposit $10 more.'
    >>> v.deposit(7)
    'Current balance: $7'
    >>> v.vend()
    'You must deposit $3 more.'
    >>> v.deposit(5)
    'Current balance: $12'
    >>> v.vend()
    'Here is your candy and $2 change.'
    >>> v.deposit(10)
    'Current balance: $10'
    >>> v.vend()
    'Here is your candy.'
    >>> v.deposit(15)
    'Machine is out of stock. Here is your $15.'
    """
    "*** YOUR CODE HERE ***"
    current_balance = 0
    current_stock = 0
    def __init__(self, item, price):
        self.item = item 
        self.price = price

    def vend(self):
        if(self.current_stock == 0):
            return "Machine is out of stock."
        elif(self.price > self.current_balance):
            return "You must deposit $" + str(self.price - self.current_balance) + " more."
        elif(self.price == self.current_balance):
            self.current_balance = 0
            self.current_stock -= 1
            return "Here is your " + str(self.item) + "."
        elif(self.price < self.current_balance):
            temp = self.current_balance
            self.current_balance = 0
            self.current_stock -= 1
            return "Here is your " + str(self.item) + " and $" + str(temp - self.price) + " change."
    
    def restock(self, num):
        self.current_stock += num
        return "Current " + str(self.item) + " stock: " + str(self.current_stock)

    def deposit(self, dollars):
        if(self.current_stock == 0):
            return "Machine is out of stock. Here is your $" + str(dollars) + "."
        else:
            self.current_balance += dollars
            return "Current balance: $" + str(self.current_balance)



class MissManners:
    """A container class that only forward messages that say please.

    >>> v = VendingMachine('teaspoon', 10)
    >>> v.restock(2)
    'Current teaspoon stock: 2'

    >>> m = MissManners(v)
    >>> m.ask('vend')
    'You must learn to say please first.'
    >>> m.ask('please vend')
    'You must deposit $10 more.'
    >>> m.ask('please deposit', 20)
    'Current balance: $20'
    >>> m.ask('now will you vend?')
    'You must learn to say please first.'
    >>> m.ask('please hand over a teaspoon')
    'Thanks for asking, but I know not how to hand over a teaspoon.'
    >>> m.ask('please vend')
    'Here is your teaspoon and $10 change.'

    >>> really_fussy = MissManners(m)
    >>> really_fussy.ask('deposit', 10)
    'You must learn to say please first.'
    >>> really_fussy.ask('please deposit', 10)
    'Thanks for asking, but I know not how to deposit.'
    >>> really_fussy.ask('please please deposit', 10)
    'Thanks for asking, but I know not how to please deposit.'
    >>> really_fussy.ask('please ask', 'please deposit', 10)
    'Current balance: $10'
    """
    "*** YOUR CODE HERE ***"
    
    def __init__(self, obj):
        self.obj = obj
    
    def ask(self, *args):
        #the first argument is *args is a string. name this string the command
        #there are three cases
        #1. command doesnt have please, so return 'You must learn to say please first'
        #2. command has 'please'. Then check if hasattr(obj, otherpartcommand)
            #1. if hasattr == true, then return obj.otherpartcommand(args[1]))
            #2. if hasattr == False, then return 'Thanks for asking, but I know not how to "otherpartcommand")
        command = args[0]
        if("please" not in command):
            return "You must learn to say please first."
        else:
            real_command = command[7::] #this gets rid of please
            if(hasattr(self.obj, real_command)):
                if(len(args) == 2): #if args is multiple arguments then deal with it
                    return getattr(self.obj, real_command)(args[1])
                elif(len(args) == 3):
                    return getattr(self.obj, real_command)(args[1], args[2])
                else:
                    return getattr(self.obj, real_command)()
            else:
                return 'Thanks for asking, but I know not how to ' + str(real_command) + "."
    
    def get_command(str):
        return str[7::]



#############
# Challenge #
#############


