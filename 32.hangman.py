#hangman in python
import random
from words import words
word= words
random.choice(word)
#so this will pick these word at random so if u pick the wrong one 6 times ufail
#dictionary of key:()
hangman_art={0:('        ',
                '        ',
                '        '),
             1:('        o ',
                '          ',
                '          '),
             2:('        o  ',
                '        | ',
                '          '),
             3:('        o ',
                '       /| ',
                '          '),
             4:('        o ',
                '       /|\\',
                '           '),
             5:('        o ',
                '       /|\\',
                '       / '),
             6:('        o ',
                '       /|\\',
                '       / \\')}
# art1=hangman_art.get(6)
# for art in art1:
#     print (art) to check whether the dictionary is working
def display(wrong_choice):
    print('******************')
    art1=hangman_art.get(wrong_choice)
    for art in art1:
        print (art)
    print('******************')
def display_hint(hint):
    print(' '.join(hint))
def display_answer(answer):
    print(' '.join(answer)) 
def main():#to maintain the main body of the code
    answer = random.choice(word)
    hint=['_']*len(answer)
    wrong_choice=0
    guessed_ans=set()
    is_running=True

    while is_running:
        display(wrong_choice)
        display_hint(hint)
        guess = input('Enter a letter: ').lower()
        if len(guess)!=1 or not guess.isalpha:
            print('Invalid! ')
            continue
        if guess in guessed_ans:
            print('Already added')
            continue
        guessed_ans.add(guess)
            
        if guess in answer:
            for i in range (len(answer)):
                if answer[i] == guess:
                    hint[i]=guess
        else:
            wrong_choice+=1
        if'_' not in hint :
            display(wrong_choice)
            display_hint(answer)
            print('Congrats YOU WON🎉🎉')
            is_running = False
        elif wrong_choice>= 6:
            display(wrong_choice)
            print('You lost 👎👎🏽')
            print(answer)
            is_running = False
if __name__ == '__main__':
    main()
