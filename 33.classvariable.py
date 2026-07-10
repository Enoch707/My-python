#class varibles = shared thru all objects that talks to that class
#                  dallowing you to share data among all objects created from that class
class Student:
    #Class variable every object will share this same information
    class_year=2024
    num_OF_STUD=0

    def __init__(self,name,age):
        self.name = name
        self.age = age
        Student.num_OF_STUD+=1 
        #This means whenever an object is called thru student access the class variable numofstud and add 1 to it
stud1=Student('Spongebob',30)
print(stud1.name)
stud2=Student('Patrick',32)
print(stud2.age)
print(stud1.class_year)
print(stud2.class_year)
#but its good practice to acess the class variable by the class name itself
print(Student.class_year)
print(Student.num_OF_STUD)
print(f'My grad class {Student.class_year} graduated with {Student.num_OF_STUD}students name {stud1.name} and {stud2.name} with ages {stud1.age},{stud2.age}' )
