# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import random

def random_number():
    """
    This function will generate a random number
    between 1 - 10 which the player will use for
    the game.
    """
    min_value = 1
    max_value = 10
    number = random.randint(min_value, max_value)

    return number

value = random_number()
print(value)