from rich import print

def hard_game(number):
    print("Great! You have selected the [orange_red1]Hard[/orange_red1] difficulty level.")
    print("[steel_blue1]Let's start the game![/steel_blue1]")
    flag = 0
    min_score = 3
    for i in range(0,3):
        guess = input("Enter your guess: ")
        intguess = int(guess)
        if intguess == number:
            print(f"[bold green]Congratulations![/bold green] You guessed the correct number in {i+1} attempts")
            current_score = i+1
            min_score = min(min_score, current_score)
            print(f"Your current high score in Hard Mode is {min_score}")
            flag = 1
            print("If you want to stop playing, press 4 to [bold magenta]exit[/bold magenta]. Otherwise press 1 for [orange1]easy[/orange1], 2 for [bold yellow]medium[/bold yellow] and 3 for [bold magenta]hard[/bold magenta] mode and let's get guessing again!")
            break
        elif intguess < number:
            print(f"[bold red]Incorrect![/bold red] The number is [aquamarine1]greater[/aquamarine1] than {intguess}")
        else:
            print(f"[bold red]Incorrect![/bold red] The number is [violet]smaller[/violet] than {intguess}")
    if flag == 0:    
        print(f"Looks like you were not able to guess the number, the number was {number}")
        print("If you want to stop playing, press 4 to [bold magenta]exit[/bold magenta]. Otherwise press 1 for [orange1]easy[/orange1], 2 for [bold yellow]medium[/bold yellow] and 3 for [bold magenta]hard[/bold magenta] mode and let's get guessing again!")