# #we have done positional,default arguements now its keyword
# #lets maake a greeting function
# def hello(greeting,first,last,tittle='Dr.'):#defaut goes to the back
#     greeting=greeting.title()
#     tittle=tittle.title()
#     first=first.title()
#     last=last.title()
#     print(f'{greeting} {tittle}{first} {last}')
#     return
# hello ('hello','spongebob','squarepants')
# #these are positional cause their position matters
# #am going to make tittle a default cause maybe they are all doctors
#nice recap lets go
#lets tell ur laptop to count 1 to 10
for i in range (1,11):
    print(i,end=' ')#end here serves has a keyword argument this means u are assigning something to something
#unless u are someone who rlly knows python u wont get it yet let me rlly break it down
#lets create a phone num generator
def phonenum(countrycode,areacode,first3dig,llast2dig):
    return f'{countrycode}-{areacode}-{first3dig}-{llast2dig}'
num=phonenum(countrycode=234,areacode=913,first3dig=319,llast2dig=1340)
print(num)
#keyword argument is like key value code because when using default arguments it gets complex 
#just directly giving it a value makes it easier