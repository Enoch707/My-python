#There are time you want to check whether something is somewhere(collections like list) hence this topic
#this include in or not in 
#lets create a secret word and lets play a game
#lets go for example b
#lets use tuple
students=('Spongebob','Patrick','Sandy')
student=input('Enter your name: ').title()
if student in students:
    print('You are admitted')
elif student not in students:
    print(f'Sorry {student} is not admitted')
#tuple,lists and set behave the same tuple is the fastest
#Dictionary
grades={'Sandy':'A',
        'Spongebob':'B-',
        'Patrick':'F+',
        'larry':'A+'
        }
student=input('Enter your name: ').title()
if student in grades:
    print(grades.get(student))
else:#also if student not in grades works here
    print('No such student here')
    #so thats all in using not in and in (in python)
