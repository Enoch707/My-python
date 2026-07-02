#nested loop is basically loop inside loop which is why note 11.1 thru to 12.2 is cruical 
#THIS IS WHAT I CALL AN HEAVY HITTER
for i in range(1,10):
    #Oh i havent touched Print functions have i well 😂😂
    #There are two things 1 is end and the other is sep i will teach it in an incoming lesson but for now 
    print(i,end=",")#means at the next sentence below me cut the spaces and add what is in the ""
    print()
#what if i want to do this 3 time loop the loop 3 times welll
for i in range (3):#whatever is in this code repeat it 3 times
    for i in range(1,10):
        print(i,end=",")#if u stop here it woud print all in this line
    print()#by doing this u are saying each time u get out of the inner loop talk to print()