#lets learn how to generate random numbers
import random#Unlocks varieties of codes for random if u need help finding a code use
#print (help(random))
#lets say we want to roll a dice
dice=random.randint(1,6)#You are telling python guess a number from 1 to 6
#lets see it in action and let it roll 3 times
for i in range(3):
    dice=random.randint(1,6)
    print(dice)
#lets say 1 to 20
for i in range(5):
    dice2=random.randint(1,20)
    print(dice2)
#U CAN PRE SET THEM
low=int (input('THE LOWEST NUMBER: '))
high=int (input('THE HIGHESST NUMBER: '))
for i in range(10):
    dice2=random.randint(low,high)
    print(dice2)
#as far as it is a number aka an interger
#if u want a float
low1=float(input('THE LOWEST NUMBER: '))
high1=float(input('THE HIGHESST NUMBER: '))
for i in range(10):
    dice3=random.uniform(low1,high1)#there is a special one for this and its random.random from 0 to 1
    print(dice3)

