# Exception Handling - Handling errors in Python programs by using try, except, else, and finally statements.

# Types of Exceptions:
# 1. Syntax errors: These are typically caught by the interpreter, so they aren't handled with try-except.
# 2. Run-time errors: Occur during the execution of the program.
# 3. Logical errors: These don't cause exceptions; they produce incorrect results.
# 4. User-defined errors: You can create custom exceptions.
# 5. System errors: Raised by the system, such as OS or file-related errors.

"""
Syntax:
try:
    # Code that might raise an exception
except ExceptionType:
    # Code to handle the exception
else:
    # Code that executes if there is no exception
finally:
    # Code that always executes
"""

# Handling various types of exceptions:

try:
    # Taking two inputs from the user
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    
    # Runtime Error: Division by zero
    result = a / b
    print(f"Result of division: {result}")
    
    # Example of a system-related error (FileNotFoundError)
    with open("non_existent_file.txt", "r") as file:
        data = file.read()

except ValueError as v:
    # Catches value-related errors, such as entering a non-integer
    print("ValueError: Invalid input, please enter integers only.")
    print(f"Error message: {v}")
    
except ZeroDivisionError as z:
    # Catches division by zero errors
    print("ZeroDivisionError: You can't divide by zero!")
    print(f"Error message: {z}")

except FileNotFoundError as f:
    # Catches system-related file not found error
    print("FileNotFoundError: The file you're trying to open doesn't exist.")
    print(f"Error message: {f}")

except Exception as e:
    # Catches any other unhandled exceptions
    print("An unexpected error occurred.")
    print(f"Error message: {e}")

else:
    # Executes if no exception occurred
    print("The operation was successful without any errors!")

finally:
    # This block will always execute, regardless of whether an exception occurred or not
    print("Execution complete. This block runs no matter what!")
