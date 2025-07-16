#multiplication table in reverse
n= int(input("Type the Number:"))

for i in range (1,11):
    print(f"{n}x{11-i} = {n*(11-i)}")