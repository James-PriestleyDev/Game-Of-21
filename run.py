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

#menu options , add elif to total.. elif = score beats CPU score. 

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
    will also allow the user to input a name for the CPU/Bot
    they will be playing against.
    This function will include the main bulk of the game
    including the users roll and adding up their end total
    after the user has had their 3 rolls and pitching it 
    against the CPU/Bots roll.
    """
    current_score = 0
    input_name = input("Who is playing today?: ")
    input_cpu_name = input("Name your challenger!: ")
    if input_name and input_cpu_name.isalpha():
        print(f'Players name is {input_name}!')
        print(f'Challengers name is {input_cpu_name}!')
        print("Good luck competitors!\n")
    else:
        print("Invalid input, please enter a name")
        new_game()
        
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
        
        total_score = current_score 
        cpu_score = random_number(15, 21)

        if current_score and cpu_score != 21:
            print(f"Neither player managed to reach the score!")
            print(f"{input_name} rolled {total_score}")
            print(f"{input_cpu_name} rolled {cpu_score})
            print("Better luck next time!)
        elif:
            print(f"Sorry {input_name}. You lost the game with a score of {total_score}!")
            print("Good luck next time!")
            print(f"The bot rolled a {cpu_score}") 

        break    
        """
new_game()
