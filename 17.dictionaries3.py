menu={'Bread':1100.0,
      'Spaghetti':950.0,
      'Honey Beans':2200.0,#NOTE: this is the perfect use of dictionaries
      'Oil':150,
      'Milo':170,
      'Milk':180,}
cart=[]#to add more items ssince lists are extremely flexible and also ordered
total=0#setting this to 0 to keep adding just read the code to get why
print('       |Menus|        ')
print('-====================-')
for key,value in menu.items() :
    print(f'{key:11}:${value:.2f}')
print('-====================-')
while True:
    items=input('What would you like to add to cart: ').title()
    
    if items=='Q':
        print('OK PLEASE CHECKOUT')
        break
    elif items=='V':
        print(cart)
    else:
        if menu.get(items):
            cart.append(items)
            total+=menu.get(items)
        else:
            print('Invalid order')
print(f'Total is ${total}')
print('-====================-')
#ALL OF THESE ARE TAUGHT BUT IF U DONT UNDERSTAND PLEASE DM
