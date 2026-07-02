#A 2d lists is kind of like a lists for lists
#like an excel spreadsheet
fruits=    ['apples','Orange','Banana','Cocunut']
vegetables=['celery','carrot','potatoes']
protein=   ['chicken','fish','turkey']
#this is a 1 dimensional list 
#time for 2d
groceries=[fruits,vegetables,protein]
#NOTE YOU CAN ALSO DO THIS groceries=[['apples','Orange','Banana','Cocunut']
                          #          ['celery','carrot','potatoes']
#                                    ['chicken','fish','turkey']]
print(fruits)
print(vegetables)
print(protein)
#to access say orange
print(fruits[1])
#for 2d tho
print(groceries)
#look at how i arranged the list on top if i want to access fruits
print(groceries[0])
#if i want to access that same orange
print(groceries[0][1])
#fish
print(groceries[2][1])
#NOTE I HAVE SAID IT OVER AND OVER COMPUTERS COUNT FROM O SO APPLES IS 00 NOT 11
print('='*32)
for i in groceries:
    print('|',end=' ')
    for i2 in i:
        print(i2,end=" ",)
    print('|')
print('='*32)