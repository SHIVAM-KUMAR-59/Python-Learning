# Defining a class Employee
class Employee:
    a = 1  # Class attribute 'a', shared among all instances of Employee

    @classmethod
    def show(cls):
        """Class method to print the value of the class attribute 'a'."""
        print(f"The class attribute of a is {cls.a}")

    @property 
    def name(self):
        """Property getter for the full name of the employee."""
        # Combines the first name and last name into a single string
        return f"{self.fname} {self.lname}"
    
    @name.setter
    def name(self, value):
        """Property setter for the full name of the employee."""
        # Splits the input value (full name) into first and last names
        self.fname = value.split(" ")[0]  # Assigns the first name
        self.lname = value.split(" ")[1]  # Assigns the last name

# Creating an instance of Employee
e = Employee()

# Overriding the class attribute 'a' by setting an instance attribute 'a'
e.a = 45  # This creates an instance attribute 'a' that shadows the class attribute

# Using the setter to assign a full name to the property 'name'
e.name = "Harry Khan"

# Accessing the instance attributes 'fname' and 'lname' to print them
print(e.fname, e.lname)  # Output: Harry Khan

# Calling the class method to display the class attribute 'a'
e.show()  # Output: The class attribute of a is 1
