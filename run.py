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
    print("To win your score needs to be exactly 21!")
    print("You will be facing off against a fierce opponent of your choosing!")
    print("Good luck!\n")

game_description()


def random_number(min_value = 1, max_value = 10):
    """
    This function will generate a random number
    between 1 - 10 which the player will use for
    the game.
    """
    number = random.randint(min_value, max_value)

    return number

def new_game():
    """
    This function will allow the user to input their name,
    will also allow the user to input a name for the computer player
    they will be playing against.
    This function will also create the ability for the player to roll
    their dice which will also add their total rolls together and within
    the if/else statements will display the result of the winner / loser
    to the terminal once the player has had their 3 rolls.
    """
    print("Starting a new game...\n")
    input_name = input("Who is playing today?: ")
    input_cpu_name = input("Name your challenger!: ")
    if input_name and input_cpu_name.isalpha():
        print(f'Players name is {input_name}!')
        print(f'Challengers name is {input_cpu_name}!')
        print("Good luck competitors!\n")
    else:
        print("Invalid input, exiting the game...")
        return
               
    current_score = 0
    user_rolls = ["first", "second", "third"]

    for description in user_rolls:
        while True:
            try:
                user_input = input("Type 'roll' to roll the dice!: ")
                if user_input.lower() != 'roll':
                    raise ValueError("Invalid input, please type 'roll'")
                break
            except ValueError as e:
                print(e)

        roll = random_number()
        current_score += roll
        print(f'Your {description} roll of the dice lands on {roll}')
        print(f'Your new total is {current_score}')
        print("\n")            
    """
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
    """
    total_score = current_score 
    cpu_score = random_number(15, 21)

    if total_score and cpu_score == 21:
        print(f"Congratulations! {input_name}, {input_cpu_name}!")
        print("You are both winners!")
        print(f"{input_name} scored... {total_score}!")
        print(f"{input_cpu_name} scored... {cpu_score}!") 
    elif total_score == 21:
        print(f"Congratulations {input_name}. You are the winner!")
        print(f"{input_name} scored... {total_score}")
        print(f"{input_cpu_name} lost with a score of... {cpu_score}")
    elif cpu_score == 21:
        print(f"Congratulations {input_cpu_name}! You are the winner!")
        print(f"{input_cpu_name} scored... {cpu_score}")
        print(f"{input_name} lost with a score of... {total_score}")    
    else:
        print(f"Neither player managed to score 21!")
        print(f"{input_name} scored... {total_score}")
        print(f"{input_cpu_name} scored... {cpu_score}")
        print("Better luck next time!")    
    return
        
new_game()
