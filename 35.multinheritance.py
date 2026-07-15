#inheritance for more than 1 class:
    #grandpa
class Animal:
    def __init__(self,name):
        self.name=name       
    def eat(self):
        print(f'{self.name} is eating')
    def sleep(self):
        print(f'{self.name} am sleeping')

#parents
class Prey (Animal):
    
    def flee(self):
        print('Call me barry cause am out')


class Predator(Animal):
    def hunt(self):
        print('😂see barry! Hunt time !')

#children
class Rabbit (Prey):
    pass

class Hawk(Predator):
    pass

class Fish(Prey,Predator):
    pass

wabbit=Rabbit('bugs-bunny')
hawk=Hawk('HAW')
fish=Fish('FIS')

wabbit.eat()
wabbit.flee()
fish.flee()
fish.hunt()
wabbit.sleep()