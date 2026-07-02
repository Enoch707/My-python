#this is the last one and its complex one this would be essential when build a web application
#this means varying argument to allow u the user to input multiple argument
def add(a,b):
    return(a+b)
print(add(1,2))#this works but
#print(add(1,2,3))#would it work without tweaking the function answer is no ofcourse not instead
def add1(*args):#WE ARE GOING TO NAME EVERY POSSIBLE ARGUMENT AND NAME IT ARG (we can name it anything)
    total=0#WE CREATE THIS AS A BASELINE
    for arg in args:#AND TELL IT TO ADD EVERY NUMBER IN ARGS TO 0 
        total+=arg
    return total#RETURN A VALUE
print(add1(1,2,3,4))
#Example 2
#lets make one to display name
def displayname(*args):
    for arg in args:
        arg=arg.title()
        print(arg,end=" ")
displayname('banjoko','goriola','enoch')


