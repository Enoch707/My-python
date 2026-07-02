#ahh we are not finished what makes def cool is its ability to return 😁
#What i mean is when creating proper functions u would need to RETURN the last value so it wont return as NONE
#Might sound confusing but let me demonstrate
# z=add(1,2) lets say we create a function add if we create that function u expect it to be 3 and give it to z right
#well its not given it to z it is RETURNING the value of add(1,2)to z
#lets make it
def add(x,y):
    return x+y#NOTE TO RETURN WHAT U ADDED
def sub(x,y):
    return x-y
def mult(x,y):
    return x*y
def div(x,y):
    return x/y
while True:
    x=int(input('NO1: '))
    y=int(input('NO2: '))
    op=input('A,S,M,D: ').upper()
    if op =='A':
        print(add(x,y))
    elif op =='S':
        print(sub(x,y))
    elif op =='M':
        print(mult(x,y))
    elif op =='D':
        print(div(x,y))
    else :
        print('Invalid input')
#I want u to go to 5.calulator.py and see the diffrences on how clean it is