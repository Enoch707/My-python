#project time
#validate a username
#1. username is no more than 12 characters
#2. username must not contain SPACES
#3. username must not contain digits
#PLS HAVE NOT TAUGHT LOOPS YET SO BEAR WITH ME AND TRY URSELF BEFORE LOOKING AT MY CODE
while True:    
    username=input('Input username: ')
    if len(username)>12:#1
        print('Character must be less than 12 characters!')
    elif username.count(' ')>1:#2
        print('Username must not include spaces')
    elif not username.isalpha():#NOTE ANYTIME I ADD A BOOLEAN LIKE VARIABLE IN AN IF STATEMENT IT CHECK IF ITS TRUE ONLY IF I ADD NOT
        print('Username must not include digits')#3
    else:
        print('VALID USERNAME!')
