#super is a function the parent class is the super class and the sub class is the child class
class Shape:
    def __init__(self,color,filled):
        self.color=color
        self.filled=filled
    def describe(self):
        return f'I am color {self.color} and i am {self.filled} with that color'        
    
class Circle(Shape):
    def __init__(self,radius,color,filled):
        super().__init__(color,filled)#this imports self.color and self.filled
        self.radius=radius
    def area(self):
        return (self.radius**2)*3.14

class Square (Shape):
    def __init__(self,lenght,breadth,color,filled):
        super().__init__(color,filled)
        self.lenght=lenght
        self.breadth=breadth
    def describe(self):
        return (f'I love the fact that i can cover {self.lenght*self.breadth}cm2 of space even tho am {self.color} and {self.filled}ly filled')
    def des(self):
         return  super().describe()#meaning the describe of shape when i use des bring it here
class Triangle(Shape):
    def __init__(self,base,height,color,filled):
        super().__init__(color,filled)
        self.base=base
        self.height=height
circle=Circle(100,'red',filled=True)
print(circle.color)
print(circle.filled)
square=Square(4,5,'Blue',False)
triangle=Triangle(12,1,'RED',True)
print(triangle.color)
print(circle.radius)
print(circle.area())
print(triangle.describe())
print(square.describe())#notice that the child class can completely override the parent (shape.describe) own unless u use the super()
#super() is use when the child and parent have an indentical function and yes __init__ is a function
print(square.des())#this is the use of me using the super method to override it