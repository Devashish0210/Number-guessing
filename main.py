import random
from levels.easy import easy_game
from levels.medium import medium_game
from levels.hard import hard_game
from rich import print

print("Welcome to [bold purple]the Number Guessing Game![/bold purple]")
print("I'm thinking of a number between 1 and 100.")
print("[bold yellow]Please select the difficulty level:[/bold yellow].")
print("1. Easy (10 chances)")
print("2. Medium (5 chances)")
print("3. Hard (3 chances)")

cont = True
while cont:
    user_input = input("Enter your choice: ")
    actual_number = random.randint(1,100)
    user_int_input = int(user_input)
    if user_int_input == 1:
        easy_game(actual_number)
    elif user_int_input == 2:
        medium_game(actual_number)
    elif user_int_input == 3:
        hard_game(actual_number)
    elif user_int_input == 4:
        print("Thanks for playing :smiley:")
        exit(1)
    else:
        print("[bold red]Invalid input![/bold red] Please try again :thumbs_down:")
        exit(1)
