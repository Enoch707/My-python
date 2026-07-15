#u know try and except we know valueerror but remaining zerodivision or typeerror
# number = int (input ('Enter a number: '))#if number is 0 its zerodiv  if num is a string its value 
# print (1/number)
try:
    number =int (input ('Enter a number: '))
    print(1/number)
except ZeroDivisionError:
    print('You cant divide by zero DUMBASS!')
#You can chain except blocks 
except ValueError:
    print('Enter only numbers pls')
# except Exception:
#     print('Invalid input')#this will catch all exceptions just that users wont know what went wrong
finally:#this happens exception or no exceptions basically a clean up
    print('REDO!')