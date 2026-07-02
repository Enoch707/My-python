#lets make a rectangle
breath=int(input('Give me the breath: '))
lenght=int(input('Give me the lenght: '))
for i in range(breath):
    print('|',end="")
    for i in range (lenght):
        print('=',end="")
    print('|')
#or😂😂
symbol=input('Input a symbol')
for i in range(breath):
    for i in range(lenght):
        print(symbol,end="")