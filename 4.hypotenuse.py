import math
while True :
    a= float (input('Input side a: '))
    b= float (input('Input side b: '))
    s= (a**2 + b**2)
    c=round(math.sqrt(s),4)
    print(f'For a right angle triangle with side {a} and side {b} is {c}')