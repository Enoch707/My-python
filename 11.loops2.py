age=int (input('What\'s your age: '))
while age<0 :
    print('Age has to be above 0')#RUN THIS CODE UNLESS THE AGE IS POSITIVE OR ABOVE 0
    age=int (input('What\'s your age: '))
else:
    print(f'YOU ARE {age}years old')
#EXAMPLE 4
#LETS PLAY WITH LOGIGAL OPERATORS
food=input('Enter a food u like')
while not food=='q':
    print(f'You like {food}')#there are numerous ways to get this approach look at loops3.py
    food=input('Enter a food u like(or q to quit): ').lower()
print('bye')
#example 5
#LETS PLAY WITH LOGIGAL OPERATORS 0r
num=int(input('Enter a number between 1 and 10: '))
while num<1 or num>10:#while num is btw 1 to 10 do this u can also say 1<num<10z
    print('Number has to be between 1 and 10')
    num=int(input('Enter a number between 1 and 10: '))
else:
    print(f'You entered {num}')