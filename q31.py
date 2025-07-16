#pattern printing
n = int(input("No of lines: "))
i=1

for i in range(i, (n+1)):
    if(i==1 or i==n):
        print("*"* n,end="")
    else:
        print("*",end="")
        print(" "*(n-2), end="")
        print("*",end="")
    print()