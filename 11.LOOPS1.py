#The legend and the myth is here there are 3 major ways to loop but first lets teach the easiest one
#while loop means keep doing it if its true (This mean if the code works ) unless being told not to(break)
#examples
x=1#we gave x the value of 1
while x!=4:#when x is NOT != 4 
    print ('STILL NOT 4')#say this
    x+=1#increases x by 1 
else:#when its now 4 say its 4
    print('Its 4')
    #I would advice u study this well cause i will be explaining loops in details now and i want you guys to follow
#example 2
name =input('Input name: ')#input name
if name== '':#if the user did not add anything say this
    print('No name was included')
else :#else(if the user included something) print this
    print(f'Welcome {name}')
#note the top one does the command ones but what if u want to keep doing it until u include a name
name =input('Input name: ')#input name
while name== '':#while the user did not add anything say this
    print('No name was included')
    name =input('Input name: ')#and ask the user to input it again
    #the reason why line 21 is sooo important is that while loops need something to break it if not it would loop it forever
    #look at line 5 u gave it a limit hence no need to 'BREAK' the loop
else :#else(if the user included something) print this
    print(f'Welcome {name}')


