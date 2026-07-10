#python slot machine
import random
import time
def spin_row():
    symbol=['🍒' ,'🍉', '🍋','🔔', '⭐']

    # result=[]
    # for sym in range (3):
    #     result.append(random.choice(symbol))
    # return result
    #or
    result=[random.choice(symbol) for sym in range(3) ]
    return result

def print_row(row):
    time.sleep(1)

    print('*************')
    print(' | '.join(row) )#meaning join the emojis with| sep works for strings .join works for lists
    print('*************')
    
def payout(row,bet):
    if row[0]==row[1]==row[2]:
        if row[0]== '🍒':
            return bet*3
        elif row[0]== '🍉':
            return bet*4
        elif row[0]== '⭐':
            return bet*10
        else:
            return bet*2
    else:
        return 0


def main():
    balance=int (input('AMOUNT TO DEPOSIT: '))
    print('**********PYSLOT**********')
    print('Symbols: 🍒 🍉 🍋 🔔 ⭐')
    print('*************************')
    while balance > 0:
        print(f'Current balance ${balance}')
        try:
            bet=int(input('Stake: '))
        except ValueError:
            print('Invalid input!')
            continue
        if bet > balance:
            print ('Insuffient funds')
            continue
        if bet <= 0:
            print ('Bet must be greater than 0')
            continue
        balance-=bet
        row=spin_row()
        print('Spinning.....')
        print_row(row)
        balance+=payout(row,bet)

if __name__  == '__main__':
    main()