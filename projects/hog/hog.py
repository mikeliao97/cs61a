"""The Game of Hog."""

from dice import four_sided, six_sided, make_test_dice
from ucb import main, trace, log_current_line, interact

GOAL_SCORE = 100  # The goal of Hog is to score 100 points.


######################
# Phase 1: Simulator #
######################

def is_prime(n):
    """ Returns whether the number n is a prime number
    >>> is_prime(2)
    True
    >>> is_prime(5)
    True
    >>> is_prime(10)
    False
    >>> is_prime(17)
    True
    >>> is_prime(8)
    False
    >>> is_prime(9)
    False
    >>> is_prime(15)
    False
    """
    if(n == 1 or n == 0):
        return False

    i = 2
    while(i <= pow(n, 1/2)): 
        if(n % i == 0):
            return False
        i += 1
    return True

def next_prime(n):
    num = n + 1
    while(True): #just keep running the loop
        if(is_prime(num)):
            return num 
        else:
            num += 1



def roll_dice(num_rolls, dice=six_sided):
    """Simulate rolling the DICE exactly NUM_ROLLS times. Return the sum of
    the outcomes unless any of the outcomes is 1. In that case, return 0.
    """
    # These assert statements ensure that num_rolls is a positive integer.
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls > 0, 'Must roll at least once.'
    # BEGIN Question 1
    "*** REPLACE THIS LINE ***"
    # END Question 1
    number_ones = 0
    sum = 0
    while(num_rolls > 0):
        roll = dice()
        if(roll == 1):
            number_ones += 1
        else:
            sum += roll 
        num_rolls -= 1
   
    #if the number of ones is bigger than 0 then return 0
    if(number_ones > 0):
        return 0
    else:
        return sum
        



def take_turn(num_rolls, opponent_score, dice=six_sided):
    """Simulate a turn rolling NUM_ROLLS dice, which may be 0 (Free bacon).

    num_rolls:       The number of dice rolls that will be made.
    opponent_score:  The total score of the opponent.
    dice:            A function of no args that returns an integer outcome.
    """
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls >= 0, 'Cannot roll a negative number of dice.'
    assert num_rolls <= 10, 'Cannot roll more than 10 dice.'
    assert opponent_score < 100, 'The game should be over.'
    # BEGIN Question 2
    "*** REPLACE THIS LINE ***"
    # END Question 2

    #need to implement the free bacon rule
    #if the current player rolls zero, or num_rolls == 0, then add opponent's max score

    sum = 0 #sum has to go through the function next_prime

    if(num_rolls == 0):
        #assumng the opponent has less than 100, this return s the biggest digit
        sum = max(opponent_score % 10, int((opponent_score / 10)) % 10) + 1
    else:
        sum = roll_dice(num_rolls, dice)

    #have the sum go through the next prime
    if(is_prime(sum)):
        return int(next_prime(sum))
    else:
        return int(sum)





def select_dice(score, opponent_score):
    """Select six-sided dice unless the sum of SCORE and OPPONENT_SCORE is a
    multiple of 7, in which case select four-sided dice (Hog wild).
    """
    # BEGIN Question 3
    "*** REPLACE THIS LINE ***"
    sum = score + opponent_score
    if(sum % 7 == 0 or sum == 0): #if the sum is divisible by 7 or equals 0
        return four_sided
    else:
        return six_sided
    # END Question 3


def is_swap(score0, score1):
    """Returns whether the last two digits of SCORE0 and SCORE1 are reversed
    versions of each other, such as 19 and 91.
    """
    # BEGIN Question 4
    "*** REPLACE THIS LINE ***"
    #this line uses modulus and divisor to check whether digits are inverse of each other
    return ((int(score0/10) % 10)  == (score1 % 10) and (score0 %10) == (int(score1/10) %10))
    # END Question 4


def other(who):
    """Return the other player, for a player WHO numbered 0 or 1.

    >>> other(0)
    1
    >>> other(1)
    0
    """
    return 1 - who


def play(strategy0, strategy1, score0=0, score1=0, goal=GOAL_SCORE):
    """Simulate a game and return the final scores of both players, with
    Player 0's score first, and Player 1's score second.

    A strategy is a function that takes two total scores as arguments
    (the current player's score, and the opponent's score), and returns a
    number of dice that the current player will roll this turn.

    strategy0:  The strategy function for Player 0, who plays first
    strategy1:  The strategy function for Player 1, who plays second
    score0   :  The starting score for Player 0
    score1   :  The starting score for Player 1
    """
    who = 0  # Which player is about to take a turn, 0 (first) or 1 (second)
    # BEGIN Question 5
    "*** REPLACE THIS LINE ***"
    #Piggy Back: When the current player scores 0, the opponent player recieves points
    #equal to the number of dice rolled that turn 
    #piggy back solution: if the result of take_turn == 0, then the other player gets
    #score in the the number of rolls that take_turn went for

    #Hog Wild: If the sum of both players' total scores is the multiple of seven
    #then the current player rolls four-sided dice instead of the usual six
    #sided dice
    #hog wild solution: Before rolling, check the sum of the scores using 
    #select dice

    #swine swap
    #after adding score to the current player, run is_swap
    
    #test case
    # 0, 0 , Goal = 10
    while score0 < goal and score1 < goal:
       #get the current player
       if(who == 0):
           num_rolls = strategy0(score0, score1) #pick the number of rolls
           current_dice = select_dice(score0, score1) #pick the current dice by checking the sum
           sum = take_turn(num_rolls, score1, current_dice) 
           if(sum == 0): #if the sum equals 0
               score1 += num_rolls #score 1 gets the number of rolls
           else:
               score0 += sum
           who = other(who)
           
       elif(who == 1):
           num_rolls = strategy1(score1, score0) #pick the number of rolls
           current_dice = select_dice(score1, score0) #pick the current dice by checking the sum
           sum = take_turn(num_rolls, score0, current_dice) 
           if(sum == 0): #if the sum equals 0
               score0 += num_rolls #score 1 gets the number of rolls
           else:
               score1 += sum #else add that to the sum
           who = other(who)
       if(is_swap(score0, score1)):
            temp = score0 
            score0 = score1
            score1 = temp

    # END Question 5
    return score0, score1


#######################
# Phase 2: Strategies #
#######################

def get_biggest_digit(opponent_score):
    return max(opponent_score % 10, int(opponent_score/10) % 10) + 1

def always_roll(n):
    """Return a strategy that always rolls N dice.

    A strategy is a function that takes two total scores as arguments
    (the current player's score, and the opponent's score), and returns a
    number of dice that the current player will roll this turn.

    >>> strategy = always_roll(5)
    >>> strategy(0, 0)
    5
    >>> strategy(99, 99)
    5
    """
    def strategy(score, opponent_score):
        return n

    return strategy


# Experiments

def make_averaged(fn, num_samples=1000):
    """Return a function that returns the average_value of FN when called.

    To implement this function, you will have to use *args syntax, a new Python
    feature introduced in this project.  See the project description.

    >>> dice = make_test_dice(3, 1, 5, 6)
    >>> averaged_dice = make_averaged(dice, 1000)
    >>> averaged_dice()
    3.75
    >>> make_averaged(roll_dice, 1000)(2, dice)
    5.5

    In this last example, two different turn scenarios are averaged.
    - In the first, the player rolls a 3 then a 1, receiving a score of 0.
    - In the other, the player rolls a 5 and 6, scoring 11.
    Thus, the average value is 5.5.
    Note that the last example uses roll_dice so the hogtimus prime rule does
    not apply.
    """
    # BEGIN Question 6
    "*** REPLACE THIS LINE ***"
    #make an inner function that calls the fn 
    def inner(*args): #args means whatever fn takes
        sum = 0
        i = 0
        while(i < num_samples):
            sum += fn(*args)
            i += 1
        return (sum / num_samples)
    return inner
    # END Question 6


def max_scoring_num_rolls(dice=six_sided, num_samples=1000):
    """Return the number of dice (1 to 10) that gives the highest average turn
    score by calling roll_dice with the provided DICE over NUM_SAMPLES times.
    Assume that dice always return positive outcomes.

    >>> dice = make_test_dice(3)
    >>> max_scoring_num_rolls(dice)
    10
    """
    # BEGIN Question 7
    "*** REPLACE THIS LINE ***"
    max_average = 0
    max = 0
    i = 10 
    averaged = make_averaged(roll_dice, num_samples)
    while(i >= 1):
        average = averaged(i, dice)
        if(average >= max_average):
            max_average = average 
            max = i
        i -= 1
    return max

    # END Question 7


def winner(strategy0, strategy1):
    """Return 0 if strategy0 wins against strategy1, and 1 otherwise."""
    score0, score1 = play(strategy0, strategy1)
    if score0 > score1:
        return 0
    else:
        return 1


def average_win_rate(strategy, baseline=always_roll(5)):
    """Return the average win rate of STRATEGY against BASELINE. Averages the
    winrate when starting the game as player 0 and as player 1.
    """
    win_rate_as_player_0 = 1 - make_averaged(winner)(strategy, baseline)
    win_rate_as_player_1 = make_averaged(winner)(baseline, strategy)

    return (win_rate_as_player_0 + win_rate_as_player_1) / 2


def run_experiments():
    """Run a series of strategy experiments and report results."""
    if True:  # Change to False when done finding max_scoring_num_rolls
        six_sided_max = max_scoring_num_rolls(six_sided)
        print('Max scoring num rolls for six-sided dice:', six_sided_max)
        four_sided_max = max_scoring_num_rolls(four_sided)
        print('Max scoring num rolls for four-sided dice:', four_sided_max)

    if True:  # Change to True to test always_roll(8)
        print('always_roll(8) win rate:', average_win_rate(always_roll(8)))

    if True:  # Change to True to test bacon_strategy
        print('bacon_strategy win rate:', average_win_rate(bacon_strategy))

    if True:  # Change to True to test swap_strategy
        print('swap_strategy win rate:', average_win_rate(swap_strategy))

    "*** You may add additional experiments as you wish ***"


# Strategies

def bacon_strategy(score, opponent_score, margin=6, num_rolls=4):
    """This strategy rolls 0 dice if that gives at least MARGIN points,
    and rolls NUM_ROLLS otherwise.
    """
    # BEGIN Question 8
    "*** REPLACE THIS LINE ***"
    #the potential score of rolling 0
    rolling_0_score = get_biggest_digit(opponent_score)

    #if rolling_0 gets you a prime number, set rolling_0_score to the next prime number
    if(is_prime(rolling_0_score)):
        rolling_0_score = next_prime(rolling_0_score)
    else:
        rolling_0_score = rolling_0_score

    #if rolling 0 is bigger than the margin, make sure the opponent doesnt swap
    #if rolling 0 results in unbeneficial swap or is smaller than margin, just return num_rolls
    if(rolling_0_score >= margin):
        if(is_swap(score + rolling_0_score, opponent_score) == False):
            return 0
        else:
            return num_rolls
    else:
        return num_rolls
    # END Question 8


def swap_strategy(score, opponent_score, num_rolls=5):
    """This strategy rolls 0 dice when it results in a beneficial swap and
    rolls NUM_ROLLS otherwise.
    """
    # BEGIN Question 9
    "*** REPLACE THIS LINE ***"
    
    #find the score of rolling 0 and get the next prime if rolling_0_score is prime
    rolling_0_score = get_biggest_digit(opponent_score)

    if(is_prime(rolling_0_score)):
        rolling_0_score = next_prime(rolling_0_score)

    #only swap if opponent_score is bigger than score, and if the swap is non-neutral 
    if(opponent_score > score and is_swap((score + rolling_0_score), opponent_score) and 
       score + rolling_0_score != opponent_score):
        return 0
    else:
        return num_rolls 

def final_strategy(score, opponent_score):
    """Write a brief description of your final strategy.
    -Combine the ideas of swap_strategy and bacon_strategy 
    -Choose the num_rolls and margin arguments carefully
    -Don't swap scores when you're winning
    -There's no point in scoring more than 100. Check for chances to win
    - Max scoring for 6 sided-die is 5
    - Max scoring for 4 sided-die is 4
    - If you can score at least 8 points, then roll 0 because thats 
    - best you can do

    *** YOUR DESCRIPTION HERE ***
    My Strategy consists of a mix of bacon_strategy and swap_strategy. My final_strategy consists of
    several if statements, the higher-priority moves happen earlier in the function. For example,
    the first if statement checks if rolling 0 will win the game without the opponent swapping, if it does, 
    return an 0! The second if-statement implements the swap_strategy. Inside swap_strategy, only
    if the swap results in a beneficial swap will swap_strategy return an 0. I was stuck on this project
    for a fairly long time at 76.6%, and one interesting strategy I implemented was forcing the opponent 
    to roll 4-sided dices which is far more in-efficient that 6-sided dices. My last if-statement uses
    bacon strategy of margin=6 and num_rolls=4, which I found was the most effective combination
    """
    # BEGIN Question 10
    "*** REPLACE THIS LINE ***"
    rolling_0_score = get_biggest_digit(opponent_score)
    if(is_prime(rolling_0_score)): #check if rolling 0 would produce a prime
        #if it's a prime set the rolling_0_score to the next prime  
        rolling_0_score = next_prime(rolling_0_score)
    
    #Check if you can win, and then swapping doesn't make you lose then swap
    if(rolling_0_score + score >= 100):
        if(is_swap(rolling_0_score + score, opponent_score) == False):
            return 0

    #Check if rolling 0 would be beneficial
    #Check if rolling 0 would unbeneficial(don't swap just roll)
    if(swap_strategy(score, opponent_score) == 0):
        return 0

    #try to make the opponent roll four-sided dice rather than the six-sided dice
    if((rolling_0_score + score + opponent_score) % 7 == 0 and score < 95):
        return 0

    #default to bacon strategy with margins=6, num_rolls=4
    return bacon_strategy(score, opponent_score)


    # END Question 10


##########################
# Command Line Interface #
##########################


# Note: Functions in this section do not need to be changed. They use features
#       of Python not yet covered in the course.


@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions.

    This function uses Python syntax/techniques not yet covered in this course.
    """
    import argparse
    parser = argparse.ArgumentParser(description="Play Hog")
    parser.add_argument('--run_experiments', '-r', action='store_true',
                        help='Runs strategy experiments')

    args = parser.parse_args()

    if args.run_experiments:
        run_experiments()
