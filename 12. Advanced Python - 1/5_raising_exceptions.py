# Exception Handling Example - Handling runtime errors and raising exceptions manually

# Taking user input
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# Example 1: Raising a ZeroDivisionError when trying to divide by zero
try:
    if b == 0:
        # Manually raising a ZeroDivisionError with a custom message
        raise ZeroDivisionError("You cannot divide numbers by 0")
    else:
        print(f"Result of division: {a} / {b} = {a/b}")
except ZeroDivisionError as e:
    print(f"Error: {e}")
finally:
    print("Example 1: Division operation complete.")

# Example 2: Raising ValueError if input is not a number
try:
    x = input("Enter an integer: ")
    if not x.isdigit():
        # Manually raising a ValueError if input is not an integer
        raise ValueError(f"'{x}' is not a valid integer!")
    else:
        print(f"Valid input! You entered the number: {x}")
except ValueError as v:
    print(f"Error: {v}")
finally:
    print("Example 2: Input validation complete.")

# Example 3: Raising a custom exception for age validation
class AgeTooLowError(Exception):
    """Custom exception for age too low"""
    pass

try:
    age = int(input("Enter your age: "))
    if age < 18:
        # Manually raising a custom exception if age is below 18
        raise AgeTooLowError("Age too low! You must be at least 18 years old.")
    else:
        print("You are eligible!")
except AgeTooLowError as age_err:
    print(f"Error: {age_err}")
finally:
    print("Example 3: Age validation complete.")

# Example 4: KeyError handling in a dictionary
try:
    data = {'name': 'John', 'age': 25}
    print(f"Name: {data['name']}")
    
    # Attempting to access a non-existent key to raise KeyError
    print(f"Address: {data['address']}")
except KeyError as k:
    print(f"KeyError: {k} - The key does not exist in the dictionary.")
finally:
    print("Example 4: Dictionary key access complete.")
