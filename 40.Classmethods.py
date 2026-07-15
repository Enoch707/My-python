# u know how self is for objects under it well cls is for the class itself

class Students :

    count=0#cls
    avg=0

    def __init__(self,name,gpa):
        self.name=name
        self.gpa=gpa
        Students.count+=1#anytime i create objects under student class we increases it by  1
        Students.avg+=self.gpa
        
    def get_info (self):
        return f'{self.name} : {self.gpa}'#this is an instance mth
    @classmethod #to indicate that its a class mth
    def get_count(cls):
        return f'Total number of students : {cls.count}'
    @classmethod #to show that i am making a function that doesnt need data from the class
    def av(cls):
        if cls.count<=0:
            return f'Total number of students : {cls.count}'
        else:
            return f'Average gpa this year is {cls.avg/cls.count}'#cls.avg means take the global variable of avg and count and let me use it
stud=Students('Enoch', 3.8)
paul=Students('Paul',2.9)
rudeus=Students('Rudy',5.0)
print (Students.get_count())#runs the get_count function
print(Students.av())
#this is to run function for the class not the objects
#NOTE class mtd is for the class in this case students
# and static methods are not for the class or object at all it is independent  