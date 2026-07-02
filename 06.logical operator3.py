#not: Its a little bit complex asd it invert the situation
while True:
    temp=int(input('Temperature: ')) #
    is_sunny=input('Is it sunny outside(yes/no): ').lower()=='yes'
    #.lower means turn any txt to lower case . upper same thing but uppercase
    #The trick i use to ake a use change its boolean mark study line 4 
    if temp >= 28 and is_sunny:#note putting is sunny is marked as true 
        #what this says is if temperature is greater than 35 or less than zero OR its raining say that
        print('It is HOT and SUNNY outside ♨♨')
    elif temp >= 28 and not is_sunny:
        print('It is HOT,CLOUDY and DARK outside ☁☁🌃')
    elif temp<=0 and is_sunny:
        print ('It is cold and sunny outside 🥶')
    elif 28> temp >0 and is_sunny:
        print ('It is warm and sunny outside 👌')
    elif temp<=0 and not is_sunny:
        print ('It is cold and cloudy DARK outside ☁🌃')
    elif 28> temp >0 and not is_sunny:
        #basically saying its not sunny since adding is sunny is automatically true then not makes it false
        print ('It is warm and cloudy DARK outside ☁🌃')

    else:#if none of them are  like that print this
        print('its night❄')

