#polymorphism part 2
#'If it looks like a duck and quacks like a duck , It must be a duck.'
#as far as it has that attribute or method it has that method python doesnt care where it got it
#-------------------------------------------------------duck typing------------------------------------------------------------------------
class Animal:
    is_alive=True

class Dog(Animal):
    def speak(self):
        return 'WOOF!'

class Cat(Animal):
    def speak(self):
        return 'MEOW!'

class Car():
    is_alive=False
    def speak (self):#even tho i didnt inherit from animal or am not an animal as far as i have a method name speak line 18 works
        return 'honk'
animal = [Cat(),Dog(),Car()]#DUCK TYPING! Car in this case quacks like a duck hence its a duck in other words car is also an animal cause it can SPEAK
for voices in animal:

    print(f'I always {voices.speak()}')
    print(voices.is_alive)
#my car can speak and i can check whether its alive hence its no diffrent from dog and animal