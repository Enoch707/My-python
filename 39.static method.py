#you know how when u want to create a method u have to put def method(SELF) in the parenthesis to access the object data
#if u dont want to do that u can perfom it statically this is a method used when u dont need it to access the object class
#best for utility method
class Employee:
    
    def __init__(self,name,position):
        self.name=name
        self.position=position
    def get_info(self):
        return f'{self.name} = {self.position}'
    @staticmethod #to indicate that it is a static mth 
    def is_valid_position(position):#because of the static mth this position is not for the employee class
        valid_pos=['Manager','Cook','Cashier','Janitor']
        return position in valid_pos
employee1=Employee('Eugene ','Manager')
employee2=Employee('Squidward ','Cashier')
employee3=Employee('Spongebob ','Cook')

print(Employee.is_valid_position('Devil Hunter'))#i dont need to call an object like employee1 or 2 to access it
print(employee1.get_info())
print(employee2.get_info())
#IT ESSENTIALLY MAKES THE CLASS A NORMAL FUNCTION INCASE U WANT TO USE IT LATER