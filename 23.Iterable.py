#basicaly anyting that can give out values one by one and can be used for loops
#forexample lists
nums=[1,2,3,4,5,]#lists are iterable,can be used in a for loop
for num in nums :
    print(num,end='-')#it can give out a value 1 by 1 and each value can be targeted
print()
#TUPLES CAN ALSO BE ITERABLE
numbers=(1,2,3,4,5)
for num in numbers:
    print (num)
#also sets
fruits={'apple','banana','coconut','orange'}
for fruit in fruits:
    print(fruit)#remember u cant reverse sets
#strings
name='ENOCH'
for letters in name:
    print(letters)
print()
#lastly dictionaries
dictionaries={'A':1,
              'B':2,
              'C':3}
for key in dictionaries:#this would print the keys not values unless u say dictionaries.value()
    print(key,end=',')
print()
for value in dictionaries.values():#these prints the value
    print(value,end='-')
print()
for key,value in dictionaries.items():#these prints everything
    print(f'{key:2} : {value}')
    #just a quick refresh