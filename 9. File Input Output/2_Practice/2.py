# The game() function in a program lets the user play a gamend returns the score as an integer. You need to read a file named 'Hi-score.txt' hich is either black or contains the previous high score  You need to WAP which updates the high score whenever the game() function breaks the previous high score

import random

def game(): 
    print("You are playing the game..")
    score = random.randint(1, 62)
    # Fetch the hiscore
    with open("hiscore.txt") as f:
        hiscore = f.read()
        if(hiscore!=""):
            hiscore = int(hiscore)
        else:
            hiscore = 0

    print(f"Your score: {score}")
    if(score>hiscore):
        # write this hiscore to the file
        with open("hiscore.txt", "w") as f:
            f.write(str(score))

    return score

game()
