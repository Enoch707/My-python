#very compex but essentially takes a long if else statement an cramps to  1 line
#you dont have to know it but this is cruical when writing longer code
import random
num0= random.randint(1,100) #just having fun but random helps python to randomly pick between 1 to 100 in this case
counter=0
while True:
    num= int(input('NUMBER: '))
    print(f'nice guess after {counter}times'if num==num0  else 'Its higher than guess' if num<num0 else 'its lower than guess')
    counter+=1
    #this if else statement is like writing normal if else but straight line but its more confusing with elif
    #check 7 part 2