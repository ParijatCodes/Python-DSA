#a function to print multiplication table
def multi(n):
    for i in range(1,11):
        print(f"{n}x{i}= {n*i}")
n= int(input("Write the number:"))
multi(n)