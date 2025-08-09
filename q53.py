#Create a class 2D vector and use it to create a 3D vector
class TwoDVector:
    def __init__(self, i, j):
        self.i= i
        self.j= j
    def show(self):
        print(f"The 2D vector form is {self.i}i + {self.j}j")

class ThreeDVector(TwoDVector):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.k = k
    def show(self):
        print(f"The 3D vector form is {self.i}i + {self.j}j + {self.k}k")

a= TwoDVector(2,3)
a.show()
b= ThreeDVector(5, 7,3)
b.show()