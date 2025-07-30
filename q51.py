#adding a static method in question n no 50
class calculator:
    def __init__(self,n):
        self.n= n
    def square(self):
        print(f"The square of {self.n} is {self.n*self.n}")
    def cube(self):
        print(f"The cube of {self.n} is {self.n*self.n*self.n}")
    def squareRoot(self):
        print(f"The square root of {self.n} is {self.n**1/2}")
    @staticmethod
    def greet():
        print("Hope You Got THe Answer")

n=int(input("Type the number:"))
a= calculator(n)
a.square()
a.cube()
a.squareRoot()
a.greet()