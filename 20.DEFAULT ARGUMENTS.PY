#basically the DEFAULT argument are the defaults u give an argument 😂😂 but rlly it is 
# first in no 19 we used positional where its position matters
#now we can examine default arguments
#to calculate the actual money u have to soend to buy say a product
def netprice(listprice,discount,tax):
    tax=tax/100
    return listprice*(1-discount)*(1+tax)


# a=int(input('What is the price of the product: '))
# b=int(input('ANY DISCOUNT: '))
# c=float(input('VALUE TAX: '))
# #print(netprice(a,b,c))

#lets say the Your store doesnt give coupons and tax is always 5%
#We can make discount and tax have a DEFAULT VALUE check line 17 to see it
def netprice1(listprice,discount=0,tax=5):#i gave discount a value of 0 and tax too
    discount=discount/100
    tax=tax/100
    return listprice*(1-discount)*(1+tax)
a=int(input('What is the price of the product: '))
b=int(input('ANY DISCOUNT: '))#now if u set this to 0 it would stil act as 0 cause we gave it its default but now
#if u set it to 5 it would ignore the default and hand it to u
print(netprice1(a))
print(netprice1(a,b))

