#lets play a little 
#lets make a default argument
#but the user wants to begin at zero all the time
import time
def count(end,start=0):#DEFAULT ARGUMENTS ARE ALWAYS AFTER POSITONAL ARGUMENT ITS CONVIENT THAT WAY
    for i in range (start,end+1):
        print(i)
        time.sleep(1)
    print('Times up!')
d=int (input ('Dtime: '))
count(d)
#PLAY WITH IT TWEAK IT DO WHAT EVER JUST MAKE SURE IT STICKS
