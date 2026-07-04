#Variable scope is where a variable is visibleand accessable
#scope resolution =(legb)Local->Enclosed->Global->Built-in
#LET ME EXPLAIN BETTER ;Here are two functions
#local
def func1():
    a=1
    return a
def func2():
    b=2
    return b

print(func1(),func2())#variable a local to func1, same as b to func2
#functions cant see another function thinkof functions as a house i can see whats going on in func1
#and func2 my neigbour cant see what is going on in my house(func A)
#disclosed when a function is in another function
def func3():
    c=1#disclosed tofunc4
    def func4():
        c=2#local to func4 NOTE local gets solved before disclosed
        return c #but this is way advanced for now
    return func4()
print(func3())
#if line 20  was deleted it will chose c=1 cause now in this case my neigbour can see my house
#so if my neigbour cant find his/her C they would use my C 
#the function say if the user uses func3 calculate whats in func4 and when u are done return the value back to me
#global scope
def func5():
    return x
def func6():
    return x
x=3#thisis the global version
print(func5())
print(func6())#this will print 3 twice x=3 is the global version cause its a universal for 
#nthat said function
#dont worry you would get this instinctively
