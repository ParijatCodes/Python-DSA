#train status and booking program using class functions
from random import randint

class Train:

    def __init__(self, trainNo):
        self.trainNo= trainNo
    
    def book(self, fro, to):
        print(f"Ticket is booked in Train No: {self.trainNo} ,from {fro} to {to}")

    def getStatus(self):
        print(f"Train No :{self.trainNo} is running on time")
    
    def getFare(self, fro,to):
        print(f"Ticket fare for train no {self.trainNo} ,from {fro}to {to} is {randint(120, 550)}")

t= Train(55034)
t.book("Shalimar", "Kashmir")
t.getStatus()
t.getFare("Shalimar", "Kashmir")