#example of a zero division error
try:
    a=int(input("Type first number: "))
    b=int(input("type second number: "))
    print(a/b)
except ZeroDivisionError as z:
    print("INFINITE")