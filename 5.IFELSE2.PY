while True:
    age=int( input('Enter ur age: '))
    if age >=100:
        print('Too old to sign up')
    elif age>=18: 
        print ('WELCOME')
    elif age <=0: 
        print('You havent being born yet')
    else :
        print('Sorry u must be 18+ to sign up')
        break
    #MOVE LINE 11 TO THE FIRST IF SO THAT IT CHECKS THAT FIRST BEFORE THE REST