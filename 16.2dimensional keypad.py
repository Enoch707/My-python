#a keypad on phone to dial a number has to be ordered, unchangable and fast
#normally using a list is the best but if u have the chance just because of share speed u should us tuple
numpad=((1,2,3),
        (4,5,6),
        (7,8,9),
        ("*",(0),"#"))
print('='*9)
for i in numpad:
    print("|",end=' ')
    for i2 in i:
        print(i2,end=' ')
    print('|')
print('='*9)
