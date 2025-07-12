#greatest among four numbers given by user
a=int(input("Type your first number:"))
b=int(input("Type your second number:"))
c=int(input("Type your third number:"))
d=int(input("Type your fourth number:"))

if(a>b and a>c and a>d):
    print( "The greatest number is a =", a)
elif(b>a and b>c and b>d):
    print("The greatest number is b =", b)
elif(c>a and c>b and c>d):
    print("The greatest number is c =",c)
else:
    print("The greatest number is d =", d)