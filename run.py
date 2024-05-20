# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high

import random

def game_description():
    """
    This function will give the user a brief
    description of the rules when the app starts.
    """
    print("Welcome to the Game of 21!")
    print("You will be given 3 rolls of a 10 sided dice")
    print("To win your rolls need to total exactly 21!")
    print("Good luck!\n")

game_description()

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

def new_game():
    """
    This function will create the users name
    and will be the main function which runs the 
    game.
    """
    current_score = 0
    input_name = input("Who is playing today?: ")
    if input_name.isalpha():
        print(f'Players name is {input_name} and their current score is {current_score}')
    else:
        print("Invalid input, please enter a name")

    while True:
        input("Type 'roll' to roll the dice!: ")
        roll = random_number()
        current_score += roll
        print(f'Your first roll of the dice lands on {roll}')
        print(f'Your new total is {current_score}')
        print("\n")

        roll = random_number()
        current_score += roll
        input("Type 'roll' to roll the dice!: ")
        print(f'Your second roll of the dice lands on {roll}')
        print(f'Your new total is {current_score}')
        print("\n")

        roll = random_number()
        current_score += roll
        input("Type 'roll' to roll the dice!: ")
        print(f'Your third roll of the dice lands on {roll}')
        print(f'Your new total is {current_score}')
        print("\n")
        
        total_score = current_score 

        if current_score == 21:
            print(f"Congratulations {input_name} you've won the game! with {total_score}")
        else:
            print(f"Sorry {input_name}. You lost the game with a score of {total_score}!")
            print("Good luck next time!") 

        break
    
new_game()
