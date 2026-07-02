questions=(('WHAT IS THE EASIEST PROGRAMING LANGUAGE: '),
           ('WHAT TYPE OF CIVILIZATION ARE WE?: '),
           ('WHICH CAR HAS A LOGO WITH 3 SPEARHEADS: '),
           ('WHO IS STRONGER BETWEEN GOJO AND SUKUNA: '),
           ('DOES FAT&OIL PRODUCE MORE ENERGY THAN RICE (SAME WEIGHT): '))
options=(('A. JAVA','B. PYTHON','C. C++','D. ASSEMBLY'),
         ('A. TYPE1','B. TYPE2','C. BELOW TYPE1','D. ALMOST TYPE3'),
         ('A.MERCEDES ','B. DODGE','C. TOYOTA','D. BUGGATTI'),
         ('A. GOJO','B, SUKUNA','C. DEPENDS WITH MAHO','D. DABURA'),
         ('A. YES','B, MAYBE','C. NO','D. DOGS'))
answers=('B','D','A','C','D')
guess=[]
score=0
question_number=0
for i in questions:
    print('='*30)
    print(i)
    for i2 in options[question_number]:
        print(i2)
    guesss= input('Enter (A,B,C,D): ').upper() .strip()
    guess.append(guesss)
    if guesss == answers [question_number]:
        print('CORRECT ')
        score+=1
    else:
        print('Incorrect')
        print(f'The answer is {answers [question_number]}')

    question_number+=1
print("========================= ")
print("          RESULTS         ")
print("========================= ")
print('Guesses are: ',end='')
for i in guess:
    print(i)

print('Answers are: ',end='')
for i in answers:
    print(i)
print('Your total score: ',(score/len(questions))*100,'%')


