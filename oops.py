# class programmer to store information

class programmer:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary
    def getProgrammerData(self):
        print(f"Name: {self.name} Age: {self.age} Salary: {self.salary}")
    
p1 = programmer("Fiza", 21, 50000)
p2 = programmer("Ana", 21, 70000)
p3 = programmer("Izza", 21, 60000)

p1.getProgrammerData()
p2.getProgrammerData()
p3.getProgrammerData()

# classs calculator to find square, cube, and squareroot
class Calculator:
    def __init__(self, num):
        self.num = num
    def getSquare(self):
        number = self.num
        square = number * number
        print(f"Square of {number} is {square}")
    def getCube(self):
        number = self.num
        cube = number * number * number
        print(f"Cube of {number} is {cube}")
    def getSqrt(self):
        number = self.num
        sqrt = (number)**(1/2)
        print(f"Square root of {number} is {sqrt}")

    @staticmethod
    def greet():
        print("Hello world number")

num = Calculator(9)
num.getSquare()
num.getCube()
num.getSqrt()
num.greet()

#program to take train name, fare and seats, and calculate seat num after it is booked and method calls
class Train:
    def __init__(self, train_name, fare, seats):
        self.train_name = train_name
        self.fare = fare
        self.seats = seats

    def book_ticket(self):
        if self.seats > 0:
            print(f"Your ticket has been booked! Your seat number is {self.seats}.")
            self.seats = self.seats - 1 # Decrease the number of available seats
        else:
            print("Sorry, this train is full.")

    def get_status(self):
        print(f"The number of available seats on {self.train_name} is: {self.seats}")

    def get_fare(self):
        print(f"The fare for a ticket on {self.train_name} is: Rs.{self.fare}")

# Create a train object
intercity_express = Train("Intercity Express", 1500, 2)

intercity_express.get_status()
intercity_express.get_fare()

print("\n--- Booking a ticket ---")
intercity_express.book_ticket()

print("\n--- Checking status after booking ---")
intercity_express.get_status()

# Try to book another ticket
print("\n--- Booking a second ticket ---")
intercity_express.book_ticket()

print("\n--- Booking a third ticket ---")
intercity_express.book_ticket()


print("\n--- Create another train to show different objects ---")
karachi_express = Train("Karachi Express", 3500, 10)

karachi_express.get_status()