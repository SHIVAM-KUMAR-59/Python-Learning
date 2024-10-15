# Defining the Number class
class Number:
    def __init__(self, n):
        """Constructor to initialize the instance attribute 'n'.
        
        Args:
            n (int): The number to be stored in the instance.
        """
        self.n = n  # Initialize the instance variable 'n' with the provided value

    def __add__(self, num):
        """Overloading the '+' operator to add two Number objects.
        
        Args:
            num (Number): The other Number object to add to the current object.

        Returns:
            int: The sum of the two Number objects.
        """
        return self.n + num.n  # Return the sum of the instance's 'n' and the other object's 'n'

# Creating an instance of Number with value 1
n = Number(1)

# Creating another instance of Number with value 2
m = Number(2)

# Using the overloaded '+' operator to add two Number instances
print(n + m)  # Output: 3 (1 + 2)
