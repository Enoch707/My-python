#let play a game with the computer 
#task is simple make the computer guess a lot of numbers until it gets pie or the number u want 
import random
while True:
    low1=float(input('THE LOWEST NUMBER: '))
    high1=float(input('THE HIGHEST NUMBER: '))
    number=float(input('WHAT NUMBER: '))
    digits=int(input('How many demical places: '))
    counter=0
    dice3=random.uniform(low1,high1)
    while dice3!=number:
        dice3=round(random.uniform(low1,high1),(digits))
        print(dice3)
        counter+=1
    else:
        print(f'COMPUTER: IT TOOK ME APROXIMATELY {counter} TRIES TO ACHIEVE {number}')