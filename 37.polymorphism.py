#its means an objects getting so many forms
#there are 2 approaches
#1 inheritance
#2 duck typing
#----------------------------------------------------------inheritance----------------------------------------------------------------------
from abc import ABC ,abstractmethod
class Shape(ABC):#this means if u ever use me as a parent u must have the area class unless i will throw that object
    @abstractmethod
    def area(self):#this is an abstract method
        pass
class  Circle(Shape):#meaning it is a circle and a shape
   def __init__(self,radius):
       self.radius = radius
   def area(self):
        return 3.14*(self.radius**2)
class  Triangle(Shape):
    def __init__(self,base,height):
        self.base= base
        self.height=height
    def area(self):
        return self.base*self.height*0.5
class Square(Shape):
    def __init__(self,side):
        self.side= side
    def area(self):
        return self.side**2
# class pentagon(Shape):#wont work cause there is no area mth
#     def __init__(self,side):
#         self.side=side
class Pizza (Circle):
    def __init__(self,topping,radius):
        super().__init__(radius)#or self.radius=radius still works regardless
        self.topping=topping
        
        
    
# circle=Circle(Shape)#its is also a shape but not a traingle
shapes=[Circle(4),Square(5),Triangle(6,7),Pizza('pepperoni',15)]
for shape in shapes:
    print(f'My area is {shape.area()}')
# p= pentagon(5)
# print(p.side)