#this explains the best way to use list comprehension in python. 
# List comprehension is a concise way to create lists in Python.
#  It allows you to generate a new list by applying an expression to each item in an existing iterable (like a list, tuple, or string) and optionally filtering items based on a condition.
#[expression for value in iterable if condition]this is the formula
doubles=[]
for i in range(10):
    i+=1
    doubles.append(i*2)
print(doubles)
#if i want to do the same thing using list comprehension i can do it like this
doubles2=[i*2 for i in range(1,11)]
print(doubles2)
#u first write down what u want it to do like for i in range(1,11) then u say i*2 what to do after the loop
#sample
doubles3=[i*2 for i in range(1,11)]
triples=[y*3 for y in range (1,11)]
square=[i**2 for i in range (1,11)]
print(doubles3,triples,square)
#lets go with strings
fruits=['apple','orange','banana','coconut']
fruit=[fruit.title() for fruit in fruits ]#meaning at everyloop make the first letters of the string capital
f=[firstletters[0] for firstletters in fruits]
print(fruit)
print(f)
#conditions
numbers=[1,-2,3,-4,-5,6]
#lets catch the positive ones them positive
posinum=[posnum for posnum in numbers if posnum>=0] #this is saying for each of the numbers here return the ones greater than 0
#Mind u there is no else we cant add else see the formula in line 4
neganum=[negnum for negnum in numbers if negnum<=0] #this is saying for each of the numbers here return the ones less than 0
#even numbers
evennum=[ evennum for evennum in numbers if evennum%2 ==  0]#regardles of whether its positve or negative if the number when divided by 0 doesnt give a remainder return it
#odd num
oddnum=[ oddnum for oddnum in numbers if oddnum%2 ==  1]#if the number when divided by 2 gives a remainder of 1 return it
print(posinum)
print(neganum)
print(evennum)
print(oddnum)

