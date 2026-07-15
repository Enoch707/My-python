#a function that extends the behavior of another function without modifying it
#lets say u create a function that is say ice cream in this case
#a decorator is like toppings or flavors like sprinkles some people like sprinkles and others like lemons whoever that is 
#the base function is ice cream while others are additions think of it like methods in a class
#formula to make a decorator
#create a normal function
def add_sprinkles(func):
#2.Create a function under it (this helps so that u have to call the function before u execute it aka line 16)
    def wrapper(*args,**kwargs):
#3.Call the variable made in step 1
        print('lets add sprinkels🎊🎊')
        func(*args,**kwargs)# p.s this function means the function of the actual function u made aka line 16 in this case
#return the second function 
    return wrapper
def add_fudge(func):
    def wrap(*args,**kwargs):
        print('Lets add fudge')
        func(*args,**kwargs)#to accept any number of argument
    return wrap
@add_fudge
@add_sprinkles
def get_ice_cream(flavor):
    print(f'This is ur {flavor} icecream🍦🍦')

get_ice_cream('Vanilla')

#look at line 11&12|17&18 this all means that before the main func print this function this whole thing is quite complex
# a make the decorator name 
#b another function so as to not call it when u use it 
#c make the func of the decorator aka what the decorator will do 
#d but the main function in (func)
#e return the second function to the decorator so that decorator can have a value