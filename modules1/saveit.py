# ================================
# saveit.py
# Mark Balagtas
# 6/4/2021
# Saving funcs
# =================================

# ======== imports

import time as t

# ========== funcs

def savescore(score):
    name = input('What is your name? ')
    with open ('highscores2.txt', 'a') as f: #writes scores in txtfile plus name
        f.write('\n'+str(score))
        f.write(' '+name)
        print('Score Saved')
        
def showscores(): # shows things on list
    with open ('highscores2.txt', 'r') as f:
        highscores = f.readlines() # makes list
        n = 0
        if len(highscores) == 0:
            print("You have no saved scores.")
        else:
            for i in range(len(highscores)):
                scores = (highscores[n])
                print(scores)
                t.sleep(1)
                n+=1
