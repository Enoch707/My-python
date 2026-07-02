#shopping cart program
while True:
    item=input('What would want to buy: ')
    price=float(input('At what price: '))
    quantity=float(input('How many would u like: '))
    total=(price*quantity)
    quantity=int (quantity)
    print(f'The amount for {quantity} {item} is {total}')