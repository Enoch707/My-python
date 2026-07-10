#object oreinted programing welcome to advanced python
#an object is a bundle of methods
#like lets say a phone it can have many functions like is it on what os is it using and all that
#method is the ability for an object to do things (functions that belong to an object 
#to utlize this u need a "class" to create many object
#a class is a blueprint used to design the  structure and layout of an object
#lets create an object a car
# class car:
#     #this is to construct an object
#     def __init__(self,model,year,color,for_sale):#self means the subject u are creating (car in this case) and everything else means information you are giving the car
#         self.model= model#when we recieve the name of the model we assign it to self.model
#         self.year = year
#         self.color = color
#         self.for_sale = for_sale
from Car import car

car1 = car('MERCEDEZ', 2026, 'black' , False)
print (car1.for_sale)#.is an attribute access operator
car2=car('Dodge',2019,'red','True')
print(car2.year)
car3=car('Tesla' ,2026,'blue',True)
print(car3.color)
#classes can take up space soo check Car.py where i saved it
car2.drive()
car3.stop()
car1.describe()