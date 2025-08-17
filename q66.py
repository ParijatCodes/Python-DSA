#a function to check if a number is divisible by 5
def divisible(n):
    if(n%5==0):
        return True
    else:
        return False
l=[2,44,35,5,55,245,34325,5554]
f=list(filter(divisible,l))
print(f)