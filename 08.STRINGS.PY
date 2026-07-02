name= input('Enter your full name: ').upper()
phone_number=input('Enter your phone number: ')
# print(len(name)) #len means to count the amount of character 
print(name.find('A'))#the position of the letter the first time u find th letter inside the bracket
print(name.rfind('A'))#look from the back
#-1 no result
print (name.capitalize())#VERY OBVIOUS
print(name.upper())#to capitalize it
print(name.isdigit())#its boolean saying whether the name is only digits
print(name.isalpha())#Only alphabetical character
print(phone_number.count('-'))#literarly to count the character in the bracket
print(phone_number.replace('-', ' '))#to replace the something with something
print(help(str))