#This topic will move u from i can create a program in python to I CAN MAKE A PROGRAM IN PYTHON
#cause u can create ur own function frm existing ones like if u want to make a log fuction or a light function u can
#lets sing happy birthday 3 times
# print('Happy birthday')
# print('You are getting old')
# print('Happy birthday')
# print('Hmm hmmm hmmm')
# print()
#if we want to repeat this u can print a)

# print('Happy birthday')
# print('You are getting old')
# print('Happy birthday')
# print('Hmm hmmm hmmm')
#print()


# print('Happy birthday')
# print('You are getting old')
# print('Happy birthday')
# print('Hmm hmmm hmmm')
# print()
#or b 
# for i in range(3):
    # print('Happy birthday')
    # print('You are getting old')
    # print('Happy birthday')
    # print('Hmm hmmm hmmm')
    #print()
#but these are all too impratical so lets just make a function that prints it
#we use the DEFINE function meaning give meanin to this word
def bdaysong():
    print('Happy birthday')
    print('You are getting old')
    print('Happy birthday')
    print('Hmm hmmm hmmm')
    print()
#You gave bdaysong a meaning a purpose making it a function so if u can call it any time
bdaysong()
bdaysong()
bdaysong()
#lets improve it a bit
#lets give it an argument
def bdsong(a,b):#it doesnt matter what i put here what matters is what u do with what u put
    print(f'Happy birthday {a}')
    print('You are getting old')
    print(f'{b} years old')
    print(f'Happy birthday {a}')
    print('Hmm hmmm hmmm')
    print()
name=input ('Whats your name bday boy/girl: ')
age= int (input('AGE: '))
bdsong(name,age)#the a in line 44 is now name in line 51 because it could be anything
bdsong(name,age)#notice b in line 44 is now age 
#which takes us back to what i said in line 44 its how its being used
#NOTE DEF is to make your code cleaner and more readable