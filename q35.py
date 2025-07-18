#recursive function to calculate the sum of first n natural numbers
def sum(n):
    if(n==1):
        return 1
    
    return sum(n-1) +n
n= int(input("Sum of how many numbers?  "))
print(f"Sum of {n} number is {sum(n)}")