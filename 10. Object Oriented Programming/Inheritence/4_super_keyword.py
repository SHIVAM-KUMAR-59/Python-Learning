
# 'super' Keyword - The super keyword is used to access the parent class's methods and attributes.

# Base class (Parent class)
class Employee:
    def __init__(self):
        """Constructor for Employee class"""
        print("Constructor for Employee class")

    a = 1  # Attribute 'a' defined in the Employee class


# Derived class (inherits from Employee class)
class Programmer(Employee):
    def __init__(self):
        """Constructor for Programmer class, overrides Employee's constructor"""
        # You can call the Employee constructor here using super() if needed
        super().__init__()  # Calling the constructor of the Employee class
        print("Constructor for Programmer class")

    a = 2  # Attribute 'a' defined in the Programmer class (overrides Employee's 'a')


# Another derived class (inherits from Programmer class)
class Coder(Programmer):
    def __init__(self):
        """Constructor for Coder class, overrides Programmer's constructor"""
        # Call the parent class (Programmer) constructor
        super().__init__()  # Correct use of super() to call the Programmer constructor
        print("Constructor for Coder class")

    a = 3  # Attribute 'a' defined in the Coder class (overrides Programmer's 'a')


# Creating an instance of the Coder class
c = Coder()  # This will trigger the constructors in the inheritance chain
print(c.a)   # Output: 3 (because 'a' in Coder overrides other 'a' attributes)

# Creating an instance of the Programmer class
p = Programmer()  # This will trigger the constructors of Programmer and Employee
print(p.a)        # Output: 2 (because 'a' in Programmer overrides Employee's 'a')

# Creating an instance of the Employee class
e = Employee()  # This will trigger only the constructor of Employee
print(e.a)      # Output: 1 (because 'a' is from Employee)
