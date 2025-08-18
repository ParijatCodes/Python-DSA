#a function to get the greatest number
from functools import reduce
l= [111, 22,56,77,65,34,89,88]
def greater(a,b):
    if (a>b):
        return a
    else:
        return b
print(reduce(greater,l))