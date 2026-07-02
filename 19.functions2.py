#lets create a function that displays an invoice 
def invoice(username,amount,duedate):
    print(f'Hello {username}')
    print(f'Your bill of ${amount:.2f} is due on {duedate}')
while True:
    a=input('Input username: ').title()#turns every first letter to capital letters
    b=float(input('How much: '))
    duedate=input('Date: ').replace(' ','-')#Replaces every space with dashes
    invoice(a,b,duedate)
        