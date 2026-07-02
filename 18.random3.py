#we could also guess strings like rock paper python
import time
import random
hands=('rock','paper','python')#u can absolutely use[lists]format here infact i recommend it if u are going to change some things in it
#if not its better to use tuple cause its faster
rounds=int(input('HOW MANY ROUNDS: '))
timer=int(input('Set timer for each round: '))
for i in range(rounds):
    time.sleep(timer)
    options= random.choice(hands)#random.choice for strings
    print(options)
   
#you are basically playing with ur cpu
#if u want to shuffle ur cards
#import random
# cards=['A',2,3,4,5,6,7,8,9,'J','Q','K']
# #lists cause we want to manipulate the data u can also use sets
# random.shuffle(cards)
# print(cards)
# #soon we would make black jack