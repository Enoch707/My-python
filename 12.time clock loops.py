#lets create a time/clock in python
import time #to import means to bring a library of some new codes time has a very important code we need which is
#time.sleep(3) this says sleep for some seconds (3 in this case)and execute said code 
#IF you are sharp enough you would understand what am about to do
time1=int(input('Enter time in seconds: '))
# for i in reversed(range (time1)):#to count backwards u can also do (time1,0,-1)
#     time.sleep(1)
#     print (i+1)#for a nice countdown
#     print('Happy new year 🎉🎉')
#the code on top is a new year countdown its a little bit boring lets make a clock
for i in reversed(range (time1)):#to count backwards u can also do (time1,0,-1)
    #lets say the user types in 3601 seconds right
    hours= (i//3600)#when i is 3601 divide completely and return the value with no remainder
    #3601//3600=1
    minutes=(i%3600)//60 #So if its 3600 divided it by 3600 and give the remainder which is 0
    #then 0 divided(floored)by 60 is 0 so python will give it as zero
    #then when i is 3599 then 3599%3600 gives 3599 then 3599//60 is 59
    seconds= i%60
    time.sleep(1)
    print (f'{hours:02}:{minutes:02}:{seconds:02}')#read note 10 for the :02
    #ITS MATHS WHICH IS WHY MATH IS ESSENTIAL FOR CODING
    #NOTE: THIS POINT IS IMPORTANT IF U START WITH 3601 THE CODE STARTS WITH 3600 CAUSE LIKE I SAID PYTHON STARTS WWITH ZERO
    #NOTE: EMPHASIS ON LINE 22 WHEN REVERSING IT WILL COUNT FROM 0 1 2 3 SO IF U PUT 4 SEC IT WIIL START FROM 3
    #NOTE: I CANT STRESS THIS POINT ENOUGH IT COUNTS FROM 0 NOT 1 BE VERY CAREFUL .
#thats clock for u in python

