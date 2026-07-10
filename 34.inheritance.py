#a class can carry traits from another class to mass reuse
class Animal:
    def __init__(self,name):
        self.name = name
        self.is_alive=True
    def eat(self):
        print(f'{self.name} is eating')
    def sleep(self):
        print(f'{self.name} is sleeping!')
#child
class dog(Animal):
    def speak(self):
        print(f'{dog.name}')
    pass
class cat (Animal):
    pass
class mouse (Animal):
    pass
Dog = dog('Scobby')
Cat= cat('Grafield')
Mouse = mouse('Mickey')
print(Mouse.name)
print(Mouse.is_alive)
Dog.sleep()
Cat.eat()
#This is convenient so u dont copy and paste