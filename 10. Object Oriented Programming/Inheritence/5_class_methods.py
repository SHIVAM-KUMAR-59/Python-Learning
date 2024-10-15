
# Class Methods - Convert a function to be a class method. A class method receives the class as implicit first argument, just like an instance method receives the instance. To declare a class method, use this idiom:

# Defining a class Employee
class Employee:
    a = 1  # Class-level attribute, shared across all instances

    # Instance method, operates on the instance (object) of the class
    def show(self):
        # Accessing the instance attribute 'a' (or class attribute if instance attribute is not set)
        print(f"The value of a is {self.a}")

    # Class method, operates on the class itself, not on an instance
    @classmethod
    def show2(cls):
        # Accessing the class-level attribute 'a' using cls (class reference)
        print(f"The value of a is {cls.a}")

# Creating an instance of Employee
e = Employee()

# Overriding the class attribute 'a' by setting an instance attribute 'a'
e.a = 45

# Calling instance method, 'show' will use the instance attribute 'a'
e.show()  # Output: The value of a is 45

# Calling class method, 'show2' will use the class attribute 'a', not the instance attribute
e.show2()  # Output: The value of a is 1
