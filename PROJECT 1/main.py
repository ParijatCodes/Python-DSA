''' 
    A STONE-PAPER-SCISSOR GAME
'''
import random
print(" Type S to Choose stone \n Type P to Choose Paper\n Type SC to Choose Scissor \n")

computer=random.choice([0,1,-1])
youstr=input("TYPE YOUR CHOICE: ")
youDict= { "S":0, "P": 1, "SC":-1 }
reDict={0 :"Stone", 1: "Paper", -1: "Scissor"}

you= youDict[youstr]
print(f" You Chose {reDict[you]} \n & Computer chose {reDict[computer]}")

if(computer == you):
    print("Its a draw")

else:
    if(computer ==-1 and you == 0): 
        print("You win!")

    elif(computer ==-1 and you == 1):
        print("You Lose!")

    elif(computer == 1 and you == 0):
        print("You lose!")

    elif(computer ==1 and you == -1):
        print("You Win!")

    elif(computer ==0 and you == 1):
        print("You Win!")

    elif(computer == 0 and you == -1):
        print("You Lose!")

    else:
        print("Something went wrong!")