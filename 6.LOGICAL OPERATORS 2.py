#and all the events have to be true for it to work 
while True:
    temp=int(input('Temperature: ')) #
    is_sunny=True
    if temp >= 28 and is_sunny:#note putting is sunny is marked as true 
        #what this says is if temperature is greater than 35 or less than zero OR its raining say that
        print('It is HOT and SUNNY outside ♨♨')
    elif temp<=0 and is_sunny:
        print ('It is cold and sunny outside 🥶')
    elif 28> temp >0 and is_sunny:
        print ('It is warm and sunny outside 👌')

    else:#if none of them are  like that print this
        print('its night❄')

