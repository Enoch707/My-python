capitals={'usa':'Washington d.c.',
          'india':'New delhi',
          'china':'Beijing',
          'russia':'Moscow'}
while True:
    states=input('What state: ')
    if capitals.get(states):
        print(f'The capital is: {capitals.get(states)}')
    else:
        print ('ITS CURRENTLY NOT IN THE DICTIONARY')
        #lets learn how to update it
        user_input=input('Would u like to update it(Y/N/R/C): ').upper() .strip()
        if user_input=='R':
            state=input('Input state: ')
            capital.pop(state)
            print(f'Successfully updated ✔')
#THIS MEANS TO REMOVE A KEY VALUE PAIR
        if user_input=='C':
            capitals.clear()
            print(f'Successfully cleared ✔')
#to clear everthing
        if user_input=='Y':
            state=input('Input state: ')
            capital=input('Input capitals: ')
            capitals.update({state:capital})#.update is to update also u can change a value like  capitals.update({USA:detriot})
            print(f'Successfully updated ✔')
#THIS MEANS TO ADD A KEY VALUE PAIR
        else:
            print('Sorry for the inconvience')
            break
#to select only the keys
# key=capitals.keys()#not important right now
# print(key)
# for i in key:
#     print(i)
#SAME FOR VALUES TOO
