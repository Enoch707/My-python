#another fun project try to read it like english once again no explanation just code
while True:    
    weight=float(input('What is the weight: '))
    unit= input('What is the unit of your weight\nKilogram(k) or Pounds(p)\n:')
    if unit == "k":
        print(f'{weight}kgs = {weight*2.205}lbs')
    elif unit == "p":
        print(f'{weight}lbs = {round(weight/2.205,3)}kgs')
    else:
        print(f'Invalid unit {unit}')
    #now try temperature converter 