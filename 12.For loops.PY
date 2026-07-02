#for loops unlike while(repeats until its true) means repeat the loop for this amount of times
#for loops helps alot when u want to do something over and over for a particular time
# lets try to count to ten shall we
for i in range(10):
    print(i+1)
#The i there is technically a counter if u run the code were it is written 1 it means i=1 same as 2 same as 10
#range means range like for that instance it means 0-9 since computers count from 0 
#infact lets play a little please count from 1 to 10 with ur fingers but start with 0 thats why i put i+1
#also u can do range(1,11) this means start at 1 but take 1 as 0 and count to 11 so the outcome would be 1-10
#in that case i would do print (i)instead
#ALSO BIGGEST MISCONCEPTION IT DOESNT HAVE TO BE I IT COULD BE LITERALY ANY THING 
for i in reversed(range(10)):#reversed to count backwards
    print(i+1)
print('Happy new year')#once this prints out something it means u are outside the loop
#if u want to count by twos
for i in reversed(range(1,11,2)):#reversed to count backwards
    print(i+1)
print('Happy new year')#this is exactly like 9.string indexing master that and u will get the hang of range