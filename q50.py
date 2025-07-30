# find square ,qube and square root using class
class calculator:
    def __init__(self,n):
        self.n= n
    def square(self):
        print(f"The square of {self.n} is {self.n*self.n}")
    def cube(self):
        print(f"The cube of {self.n} is {self.n*self.n*self.n}")
    def squareRoot(self):
        print(f"The square root of {self.n} is {self.n**1/2}")

n=int(input("Type the number:"))
a= calculator(n)
a.square()
a.cube()
a.squareRoot()