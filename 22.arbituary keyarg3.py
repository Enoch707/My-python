#lets use both  arg and kwars together
def shippinglabel(*args ,**kwargs):
    print('Welcome',end=' ')
    for arg in args:
        print(arg,end=' ')
    print()
    print('===========ADDRESS===========')
    for key,value in kwargs.items():
        print(f'{key:8} : {value}')
    print('=============================')
    print(kwargs.get("St"))
shippinglabel('Dr.','Spongebob','Squarepants','III',
              St='123 Py str.',
              city='Amazion',
              State='Amazan',
              country='Amazon rainforest')
#to check whether a dictionary is present like city say you would say if city in kwargs:
#these ar arbituary agrument in python#3#