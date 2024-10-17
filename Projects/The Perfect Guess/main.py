import random

# Generate a random number between 1 and 100
n = random.randint(1, 101)

# Initialize 'a' with a dummy value, and 'guesses' to keep track of the number of attempts
a = -1
guesses = 0

# Loop until the user guesses the correct number
while a != n:
    # Increment guess counter
    guesses += 1
    
    # Get the user's guess as an integer
    a = int(input("Take a guess: "))
    
    # Check if the guess is greater than the random number
    if a > n:
        print("Too high! Try a smaller number.")  # Improved message for guessing lower
    elif a < n:
        print("Too low! Try a bigger number.")   # Improved message for guessing higher

# Once the correct number is guessed, print the success message with the total guesses
print(f"🎉 Congratulations! You've guessed the correct number {n} in {guesses} attempts.")
