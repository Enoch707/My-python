

def menu():
    menu1=input('''1)Hint
                2)Current score
                3)Add to current hint
                4)Exit ''')  

print('Welcome kindly select ur game')
select=int (input('Number of players: '))
while True:
    choice1=(input('''1)The guess game
2)Math game
3)Number game
4)Exit\n: ''')) 
    if choice1=='1':
        word=input("Player 1 whats the word: ")
        hint1=input('Welcome to the guess game\n Input ur hint:  ')
        print('''Rules
1)The first player types a word and a clue
2)A countdown starts and after its stop the next player is to input his guess
3)3 Attempts is given to the user then the current player sees the answer and add his own hint
4)The game goes on until the last person cant guess''')
    for i in range(select):
        counter =1
        x=False
        print(f'Its Player {i+1} turn')
        while counter<=3:
                attempt=input(f'ATTEMPT {counter}:')
                if counter==2 :
                      print(hint1)
                if attempt==word:
                     print(f'Congrats player {i+1}')
                     break
                     exit
                else :
                    if word!=attempt :
                     print('WRONG!')
                    counter+=1
        if not x :
            print(f'Player {i+1} lost')
             
             
