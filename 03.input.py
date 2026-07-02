#Very important topic and argueably one of the most used command 
#It helps a user to actually interacts with the code
input()#Like a type box for users to put in data 
input('What is your name?: ')#gives u a question to type in ur name 
#its a little bit useless as its stands cause its not interacting with the code
#instead
name=input('What is your name?: ')
print(f"Hello {name}")#see the difference,Giving that data to the word name 
#The computer now knows that anything u put inside that question is 'NAME'
age= int (input('How old were u last year: '))
age+=1
print('Happy birthday')
print(f'You are {age} years old now')
#ERROR ITS IS A STRING NOT A NUMBER if it was this
#age= input('How old were u last year: ')
#Instead add int to the front
