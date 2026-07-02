import math
#Yayyyy u are now able to create ur very own calculator look at u
# with what we learnt so far lets make one
# This time i wont help i will just write the code its up to u to read that in plain english
while True:
    num1=float(input('Enter the first number: ')) 
    operator=input('Select an operator (+,-,*,/,f,m,p,r)\np=power,r=squart\nf=floor,m=modulo:')
    num2=float(input('Enter the second number: '))
    if operator=="":
        print('Operator not defined')
    elif operator=='+':
        print (f'{num1}+{num2}={round(num1+num2,3)}')
    elif operator=='-':
        print (f'{num1}-{num2}= {round(num1-num2,3)}')
    elif operator=='*':
        print (f'{num1}*{num2}= {round(num1*num2,3)}')
    elif operator=='/':
        print (f'{num1}-{num2}= {round(num1/num2,3)}')
    elif operator=='m':
        print (f'{num1}modulo{num2}= {round(num1%num2,3)}')
    elif operator=='f':
        print (f'{num1}floor{num2}= {round(num1//num2,3)}')
    elif operator=='p':
        print (f'{num1} raised to the power of {num2}= {math.pow(num1,num2)}') 
    elif operator=='r':
        print (f'{num1} root {num2}= {math.sqrt(num1)}')
    else:
        print('Invalid input')
#Now if i truly wanted to i could do sooo much more 
#like perform more and more operations until the user wants a stop
#a full calculator with orginal functions like root,quadratic equation and binary operation
#ONCE AGAIN WELCOME TO PYTHON U CAN RLLY DO SOO MUCH MORE





