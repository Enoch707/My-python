#lets create a shoping cart program
#the reason why we are using lists and i really concetrated on lists is because if we want to manipulate data
# we use lists
foods=[]
prices=[]
total=0
while True:
    try:
        food = input ('Enter a food to buy (q to quit): ').lower() .strip()
    except ValueError:
        print('INVALID INPUT')
    if food =='q':
        break
    else:
        try:
            price= float(input(f'Enter the price of {food}: $'))
        except ValueError:
            print('Invalid input')
            continue
        foods.append(food)
        prices.append(price)
print('='*10,'Shoping cart','='*10)
for i in foods:
    print(i)
for i in prices:
    total+=i
print(f'Your total was ${total}')
