#write a function to find greatest of three numbers

def great():
    a=int(input("Write first number(a): "))
    b=int(input("Write second number(b): "))
    c=int(input("Write third number(c): "))

    if(a>b and a>c):
        print(f"a ={a} is the greatest number. ")
    elif(b>a and b>c):
        print(f"b ={b} is the greatest number. ")
    else:
        print(f"c ={c} is the greatest number. ")

great()