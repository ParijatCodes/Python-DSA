#pattern printing 

n = int(input("No of lines: "))
i=1

for i in range(i, (n+1)):
    print(" "*(n-i), end="")
    print("*"*(2*i-1), end="")
    print()