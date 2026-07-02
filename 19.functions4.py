#Do you see the beauty of function making u can make anything u want
#lets make a full name generator
def name(first,last):
    first=first.title()
    last=last.title()
    return first + ' ' + last
#i know i know you can just say print(f'{FIRST} {LAST}')
#The reason why this is impratical is because return finishes a funtion like it ends it 
#2.Its just more easier to manipulate
a=input('Whats your first name: ')
b=input('How about your last name: ')
print(name(a,b))
#WELL THATS ALL FOR FUNCTIONS WE WILL BE USING THIS ALOT
#FUNCTION IS A REUSABLE CODE!