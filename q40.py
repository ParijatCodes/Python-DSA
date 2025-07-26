#A random score generator game
import random
def game():
    print("You Are Playing The Game \nYou will get a score between 1 to 100")
    score = random.randint(1,100)

    with open("q40_hiscore.txt") as h:
        hiscore = h.read()
        if(hiscore != ""):
            hiscore= int(hiscore)
        else:
            hiscore= 0
    print(f"Your score is {score}")
    if(score>hiscore):
        print(f"New HI-SCORE is {score}")
        with open("q40_hiscore.txt", "w") as h:
            h.write(str(score))
    return score

game()