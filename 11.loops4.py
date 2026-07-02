#a compound interest calculator
#compound interest is the 'added bonus'of the cash you are given to them
#Formula is A=P(1+r/n)^t 
while True:
    time=0#(t)
    principal=0#p
    rate=0#r
#if i where to use the while true attribute here it would restart the loop here but the values of the variable is not reset hence will just repeat ANSWER
    while principal <=0:
        principal= float(input('Enter the principle amount: '))
        if principal <=0:
            print ('Principle cant be less than zero!')

    while rate<=0:
        rate= float(input('Enter the interest rate: '))
        if rate <=0:
            print ('The rate cant be less than zero!')

    while time <=0:
        time= float(input('Enter the time in years: '))
        if time <=0:
            print ('A date cant be less than zero!')
    #this is to account for users putting an invalid p r or t
    total =principal*((1+(rate/100)))**time
    print(f'The balance after dropping ${principal} in {time}years is ${round(total,3)}')
    continue


