
class Rectangle:
    def __init__(self,width,height):
        self._width=width
        self._height=height#._ tells you or other devs that you should try to access hor modify  the width and height directly
#---------------------------------------getter method------------------------------------------------    
#aka what happens when u try to get them
    @property
    def width(self):
        return f'{self._width:.1f}cm' #when accessing the string add cm to it

    @property
    def height(self):
        return f'{self._height:.1f}cm' #when accessing the string add cm to it
#--------------------------------------setter method-------------------------------------------------    
#aka when u write them out
#this are the set of rules u give it when u try to modify the class from outside 
    @width.setter
    def width(self,new_width):
        if new_width> 0:
            self._width = new_width
        else:
            print('Width should be greater than 0')
    @height.setter  
    def height(self,new_height):
        if new_height> 0:
            self._width = new_height
        else:
            print('Height should be greater than 0')
#_________________________---------------deleter method-------------------_____________________________
#self explained
    @width.deleter
    def width(self):
        del self._width
        print('Success')
rec1=Rectangle(3,4)
rec1.width=5#example of setter method in use
del rec1.width
print(rec1.height)
#if i access self._width it would be just the raw value and inside the class u can decorate it with @property