import random

# Define a class 'Train' to handle ticket booking, status checking, and fare information.
class Train:

    # Constructor to initialize the train number when an object of this class is created.
    def __init__(self, trainNo):
        self.trainNo = trainNo

    # Method to book a ticket with the starting point (fro) and destination (to).
    def book(self, fro, to):
        print(f"Ticket is booked in train number {self.trainNo} from {fro} to {to}.")

    # Method to get the current status of the train (e.g., whether it's running on time).
    def getStatus(self):
        print(f"Train number: {self.trainNo} is running on time.")

    # Method to get the fare information for a journey from 'fro' to 'to'.
    def getFare(self, fro, to):
        # The fare is randomly generated between 222 and 5555.
        fare = random.randint(222, 5555)
        print(f"Ticket fare in train number {self.trainNo} from {fro} to {to} is: ₹{fare}")

# Creating an instance (object) of the Train class with train number 12345.
myTrain = Train(12345)

# Calling the methods with sample input.
myTrain.getStatus()                # Check the current status of the train.
myTrain.getFare("Delhi", "Mumbai") # Get the fare for the journey from Delhi to Mumbai.
myTrain.book("Delhi", "Mumbai")    # Example booking from Delhi to Mumbai.

