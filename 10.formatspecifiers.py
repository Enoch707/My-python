#format specifiers =:{:FLAGS} format a value based on what flags are inserted
#let me show u lets create 3 variale
price1=3.14159
price2=-987.65
price3=12.3
price4=12000000
print(f'The first price is {price1:.2f}')#its saying round to 2 decimal places f being float

print(f'The second price is {price2: 10}')#meaning eat up 10 places meaning 10 max spaces for this case its 3 space case the number takes up 7

print(f'The third price is {price3:010}')#if i precede with 0 it would fill up the said spaces with 0

print(f'The first price is {price1:<10}')#creates 10 possible space then shifts it to the first 7 spaces but not neccesary 

print(f'The first price is {price1:^10}')#Most important for me this is to center align

print(f'The second price is {price2:>10}')#creates 10 possible space then shifts it to the last 7 spaces

print(f'The third price is {price3:+}')#to makes positiv numbers have plus in front or just a space

print(f'The fourth price is {price4:,}')#another important code cause u cant tell python int(1,000)comma is not a number b

print(f'The fourth  price is {price4:+,.2f}')#you can mix them