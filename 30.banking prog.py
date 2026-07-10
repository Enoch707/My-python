#this will utilise 27 to 29 codes also script 2 and circle
#this is a banking program 
#one that will show account balance, withdraw and deposit
#when making projects call every functions and put pass to hold it until u start to code something like line5
# def balance():
#     pass
def balance(accbal):
    return f'---> {accbal:.2f}$'
def withdraw(accbal):
        while True:
            try:
                amount =float(input('Enter an amount to be withdrawn\n--> '))
                if amount > accbal:
                    print('Insuffient funds')
                    return 0
                    
                if amount<0:
                    print ('Invalid input')
                else:
                    return amount
                break
            except ValueError:
             print('Invalid input')
def deposit():
        while True:
            try:
                amount =float(input('Enter an amount to be deposit\n--> '))
                if amount<0:
                    print ('Invalid input')
                else:
                    return amount
            except ValueError:
                print('Invalid input')
def main():
    accbal=0
    sys=True
    while sys:
        print('***Interface***')
        choice=input('''1)SHOW BALANCE
2)DEPOSIT
3)WITHDRAW
4)Exit\n:''')
        if choice=='1':
           print(balance(accbal))   
        elif choice=='2':
         accbal+=deposit()
         continue
        elif choice=='3':
            accbal-=withdraw(accbal)
        elif choice=='4':
          sys=False
        else:
           print('Invalid input')
    print('Thank you for choosing us!')
if __name__ == '__main__':
    main()