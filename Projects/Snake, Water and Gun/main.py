import random

# Define the rules of the game
"""
Game Rules:
- 1 for Snake
- -1 for Water
- 0 for Gun

The rules of the game are as follows:
- Snake beats Water (Snake wins)
- Water beats Gun (Water wins)
- Gun beats Snake (Gun wins)

You can enter one of the following choices:
- 'snake' to play as Snake
- 'water' to play as Water
- 'gun' to play as Gun

Type 'exit' at any time to quit the game.
"""

# Dictionary to map choices to numbers
ruleDictionary = {"snake": 1, "water": -1, "gun": 0}

# Infinite loop for the game
while True:
    # Get the user's choice and map it to the corresponding value
    you = input("Enter your choice (snake/water/gun) or 'exit' to quit: ").lower()  # Convert input to lowercase

    # Check if the user wants to exit
    if you == 'exit':
        print("Thanks for playing! Goodbye!")
        break

    youInput = ruleDictionary.get(you)  # Use get to avoid KeyError

    # Check if the user's input is valid
    if youInput is None:
        print("Invalid choice! Please enter 'snake', 'water', or 'gun'.")
        continue  # Skip to the next iteration of the loop

    # Get the computer's choice randomly from the keys of the dictionary
    computerChoice = random.choice(list(ruleDictionary.keys()))
    computerInput = ruleDictionary[computerChoice]

    print(f"\nYou chose: {you} (input value: {youInput})")
    print(f"Computer chose: {computerChoice} (input value: {computerInput})")

    # Determine the outcome of the game
    if youInput == computerInput:
        print("It's a tie!")
    elif (youInput == 1 and computerInput == -1) or (youInput == -1 and computerInput == 0) or (youInput == 0 and computerInput == 1):
        print("You win!")
    else:
        print("You lose!")

    print()  # Print a newline for better readability
