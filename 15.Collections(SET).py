#sets are{} unlike lists these guys are not ordered(We cant arrange them) and no duplcates
fruits={'apples','Orange','Banana','Cocunut'}
#to show u how unordered they are
print(fruits) 
#RUN IT 3 TIMES
#u can look for help and ask it questions but
#print (fruits[0]) is not possible
#but we an add something
fruits.add('something')
#we can remove apples
fruits.remove('apples')
print(fruits)
#removing the first element tho it is random
fruits.pop()
print(fruits)
#u can remove all of it
fruits.clear()
print(fruits)