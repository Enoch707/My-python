# #the function would be used here
# #function was made in script2
# print(dir())#this is fora special type of variable 
# print(__name__)#what ever name is given here is the name you would compare tho is always_main_
# #hence
# if __name__=='__main__':
#     pass
#lets import script2
import script2 as sc #am renaming it sc for this file
#if i didnt write if__name__=__main__ it willrun main() automatically
#soi can just
def favdrink(drink):
    return f'I also i prefer {drink} to coke '
print ('This is script 1!')
print(sc.favfood('RICE'))
print(favdrink('Pepsi'))
print('Goodbye')
#NOTE if in script2.py i wanted to run main() there but i  will put main() anywhere i want to call it write
#But doing so means that if i import the file here it will run main() right here unless i cover the function in __name__=__main__
#try removing it and adding it back
#this is very useful if i want to borrow a set of code from another program but i dont want to run whats in it 