#a variable can save only one value but thats impratical soo 
#let me explain how we can shove multiple data in one variable
#variable
fruit= 'apple'
print(fruit)
#lets add more
fruits=['apples','Orange','Banana','Cocunut']#for multiple choices that u can manipulate even after putting it is[]
print(fruits)
print(fruits[2])#remeber string formating
print(fruits[0:2])
print(fruits[:2])
print(fruits[::2])#same thing as fruits[0:0:2]i would like every second element
print(fruits[::-1])#backwards or reversed fruits
for i in fruits:
    print(i)#u can count them 1 by one
#a little fun yh?
for i in fruits:
    if i != 'Banana':
        print (i)
    else:
        print ('Damn why them banana so big like')
        continue
#In lists you can access the data in them isnt that cool
#if u need help 
print (dir(fruits))
#more details 
# print(help(fruits))
#the amount of data in ur list
print(len(fruits))
#if i add pineapple
fruits.append('Pineapple')#to add an element in to the end of a list
#it changes
print(fruits)
print(len(fruits))
#lets ask python some questions
print('apple'in fruits)
print('apples'in fruits)
#lets manipulate some of the data
fruits[0]='APPAS'
print(fruits)
#lets remove banana
fruits.remove('Banana')
#lets put banana to where we want
fruits.insert(1,'Banana')
#to arrange them
fruits.sort()
#to reverse
fruits.reverse()
#to find the index of a particular fruit
print(fruits.index('Orange'))
#to find the amount of a data
fruit.count('Coconut')
#to clear it 
fruits.clear()
#