#check if a number is prime or nnot

n  = int(input("Type your number:"))

for i in range(2, n):
    if (n%i ==0):
        print("Number is not Prime")
        break
else:
    print("Number is Prime")

