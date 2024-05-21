![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome James Priestley,

This is the Code Institute student template for deploying your third portfolio project, the Python command-line project. The last update to this file was: **August 17, 2021**

## Reminders

* Your code must be placed in the `run.py` file
* Your dependencies must be placed in the `requirements.txt` file
* Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

-----
Happy coding!

Game of 21

README.md

###########################################

## GAME OF 21

Game of 21 is a python terminal based game, which users can run through Heroku.

The aim of the user is to have the total of 21 by the end of their 3 rolls. Thus, making them the winner.

## How To Play

Game of 21 is a game based off of the gambling game 'blackjack' except instead of playing cards.
The user is given 3 rolls of a 10 sided dice and to win the game the user needs to roll a total
of 21 with their 3 rolls. Any other number is considered a loss for the user.

## Features

Random number generator

 [Provide image of random number once user has rolled the dice]

Takes users name as input

[Provide image of program taking users name]

Takes user input and validates whether input is valid or not and gives response if invalid.

[Provide image of invalid input]

Adds the users results from each individual roll of the dice

[Provide image of the users first, second and third roll]

Program tells user whether they are winner or not and shows their total.

[Provide image of end result]

## Future Features

Allow player to play against a bot.
Add a counter of how many wins/losses the user has gotten.

## Testing

I have manually tested this project by doing the following:

    Tested each individual function with a print statement to ensure each function works
    Tested the code in the Heroku app to ensure, once deployed the program functions as intended
    Entered invalid inputs to test the validation checks inside the code.
    Ran code through pep8 to ensure no faults or errors with code.



## Bugs

    Solved bugs

   --------------

## Validator Testing

    Pep8

[Provide image of pep8 results]    