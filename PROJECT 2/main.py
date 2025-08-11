'''
Number Guessing Game in PYTHON
'''
import random
n= random.randint(1,100)
a=-1
guesses=0
while(a!=n):
    a= int(input("Guess Your Number: "))
    if(a<n):
        print ("Guess Higher")
        guesses+=1
    elif(a>n):
        print("Guess Lower")
        guesses+=1
print(f"You have guessed the correct number {n} in {guesses} attempts !")