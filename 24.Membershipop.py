#There are time you want to check whether something is somewhere(collections like list) hence this topic
#this include in or not in 
#lets create a secret word and lets play a game
word ='annaitesia'
trial=[]
counter=0
while True:
    letter=input('Guess a letter in the secret word: ')
    if letter== 'hint':
        print(trial)
    if letter== word:
        print('You won!')
        break
    if letter in word:#if what the user types is IN the word 
        print("Alright its there!")#SAY THIS
        counter+=1
        trial.append(letter)
    elif letter not in word:#IF U DONT SEE IT
        print('LETTER WASNT FOUND')#SAY THIS
        counter+=1
    else:
        print('Invalid')
print(f'At the {counter+1}th trail!')
#i got carried away but not in and in are literally what they mean
#NOTE this code is used for like password check or email check or validation super useful code