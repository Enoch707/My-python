#lets make a dice roller program in python
import random
#lets use a udicode character depends on the operating system i will teach this later
# print('\u25CF \u250C \u2500 \u2510 \u2502 \u2514 \u2518') WHEN YOU OUTPUT IT CPOY AND PASTE IT TO UR CODE
#● ┌ ─ ┐ │ └ ┘ 
'┌─────────┐'
'│         │'
'│         │'
'│         │'
'└─────────┘'
#finally a box
#lets create a dictionary
diceart={
    1:('┌─────────┐',
       '│         │',
       '│    ●    │',
       '│         │',
       '└─────────┘'),
    2:('┌─────────┐',
       '│ ●       │',
       '│         │',
       '│       ● │',
       '└─────────┘'),
    3:('┌─────────┐',
       '│ ●       │',
       '│    ●    │',
       '│       ● │',
       '└─────────┘'),
    4:('┌─────────┐',
       '│ ●     ● │',
       '│         │',
       '│ ●     ● │',
       '└─────────┘'),
    5:('┌─────────┐',
       '│ ●     ● │',
       '│    ●    │',
       '│ ●     ● │',
       '└─────────┘'),
    6:('┌─────────┐',
       '│ ●     ● │',
       '│ ●     ● │',
       '│ ●     ● │',
       '└─────────┘'),
}
dice=[]
total=0
dicenum=int (input('How many dice: '))
for i in range(dicenum):
   num=random.randint(1,6)
   dice.append(num)
   total+=num
#    for i2 in diceart.get(dice[i]):
#       print(i2)
# print(total)
#lets go crazier
for line in range (5):
    for die in dice:
        print(diceart.get(die)[line],end="")
    print()
        