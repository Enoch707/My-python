#this on is a bit tricky
capitals={'usa':'Washington d.c.',
          'india':'New delhi',
          'china':'Beijing',
          'russia':'Moscow'}
items=capitals.items()
for i in items:
    for i2 in i:
        print(i2)
    print()
    #it basicals turns your dictionaries to a 2d list
for key,value in capitals.items:
    print(f'{key}:{value}')
#NOTE This is advanced we will touch these for our gaming programs later