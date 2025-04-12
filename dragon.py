'''
    How to play Dragon Realm

    ########################

    In this game, the player is in a land full of dragons. The dragons all live in caves with their large piles of collected treasure.
    Some dragons are friendly and share their treasure. Other dragons are hungry and eat anyone who enters their cave.
    The player approaches two caves, one with a friendly dragon and the other with a hungry dragon, but doesn't know
    which dragon is in which cave. The player must choose between the two caves.

    ########################
'''

import random
import time

def displayIntro():
    print('''
    You are in a land full of dragons. In front of you,
    you see two caves. In one cave, the dragon is friendly
    and will share is treasure with you. In the other cave
    the dragon is greedy and hungry, and will eat you on sight.
    
    Choose your destiny
    \n''')

def chooseCave():
    cave = ''
    while cave != '1' and cave != '2':
        cave = input('Which cave will you go into? (1 or 2) ')

    return cave

def checkCave(chosenCave):
    print('You approach the cave...')
    time.sleep(2)
    print('It is dark and spooky...')
    time.sleep(2)
    print('A large dragon jump out in front of you! He opens his jaws and...')
    print()
    time.sleep(2)

    friendlyCave = random.randint(1, 2)

    if chosenCave == str(friendlyCave):
        print('Gives you his treasure!')
    else:
        print('Goobles you down in one bite!')


playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y':
    displayIntro()
    caveNumber = chooseCave()
    checkCave(caveNumber)

    playAgain = input('Do you want to play again? (yes or no) ')