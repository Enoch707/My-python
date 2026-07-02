x=[]
while True:
    food = input ('What is your favorite food(q to quit): ')
    while food != 'q':
        print(food)
        x.append(food)
        food = input ('What is your favorite food(q to quit): ')
    else:
        quest= input('Would you like to veiw your food items(Y/N): ').upper() .strip()
        if quest== 'Y':
            print(x)
        else:
            print('Have A Nice Day')
