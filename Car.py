class car:
    #this is to construct an object
    def __init__(self,model,year,color,for_sale):#self means the subject u are creating (car in this case) and everything else means information you are giving the car
        self.model= model#when we recieve the name of the model we assign it to self.model
        self.year = year
        self.color = color
        self.for_sale = for_sale
#methods 
    def drive(self):
        print(f'You drive the {self.color} {self.model}')
    def stop(self):
        print (f'You stop the {self.color} {self.model}')
    def describe(self):
        print(f'{self.year} {self.color} {self.model}')