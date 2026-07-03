capitals={'usa':'Washington d.c.',
          'india':'New delhi',
          'china':'Beijing',
          'russia':'Moscow'}
#lets learn how to update
while True:
    states=input('What state: ')
    if capitals.get(states):
        print(f'The capital is: {capitals.get(states)}')
    else:
        print ('ITS CURRENTLY NOT IN THE DICTIONARY')
        #THIS MEANS TO REMOVE A KEY VALUE PAIR
        user_input=input('Would u like to update it(Y/N/R/C): ').upper() .strip()
        if user_input=='R':
            state=input('Input state: ')
            capital.pop(state)
            print(f'Successfully updated ✔')
#to clear everthing
        if user_input=='C':
            capitals.clear()
            print(f'Successfully cleared ✔')
#THIS MEANS TO ADD A KEY VALUE PAIR
        if user_input=='Y':
            state=input('Input state: ')
            capital=input('Input capitals: ')
            capitals.update({state:capital})#.update is to update also u can change a value like  capitals.update({USA:detriot})
            print(f'Successfully updated ✔')
        else:
            print('Sorry for the inconvience')
            break
#to select only the keys
# key=capitals.keys()#not important right now
# print(key)
# for i in key:
#     print(i)
#SAME FOR VALUES TOO
