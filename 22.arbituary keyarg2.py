#do u remeber keyword arg on no 21
#You can essentially use multiple keyword argument not only normal arguements
#these is called kwargs lets make some that prints out ur address
def printadd(**kwargs):#NOTE double asterisks
    for key,value in kwargs.items():
        print(f'{key:5} : {value}')
printadd(str="314 Python st.",
         city="Detroit",
         apt=10,
         state="Amazon",)#lets add apt=houseapartment
#you can add more and more dictionaries 
#this is all overwhelming so lets start a project