#if-else is literally the embodiment of if something is something do something 
#else do something else
while True: #NOT NECCESARY BUT ITS TO LOOP IT
    age=int( input('Enter ur age: '))
    if age>=18: #literary saying if age is greater than 18 do
        print ('WELCOME')#this says if u are 18 or greater right welcom also 
        #leave space 4 to be easier
    elif age <=0: #self explanatory if the first one is invalid it move here 
        #see the diffrence bt/w else and elif is that elif is saying OR DO THIS rather than OTHERWISE
        print('You havent being born yet')
    elif age >=100:
        print('Too old to sign up')
    else :#IF NOT PRINT THIS ELSE IS BASICALLY OTHERWISE
        print('Sorry u must be 18+ to sign up')
        break#TO BREAK OUT OF THE LOOP
        #if age is not above or equal to 18 write this
#THERE IS AN ERROR IN LINE 11 AND LINE 5 FIGURE IT OUT AND THERE ARE TWO SOLUTIONS
#check ifelse2