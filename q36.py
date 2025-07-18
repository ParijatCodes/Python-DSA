#pattern printing using recursion

def pattern(n):
    if(n==0):
        return
    print("*"* n)
    pattern(n-1)

n= int(input("Type number of Rows:"))
print("\t")

pattern(n)