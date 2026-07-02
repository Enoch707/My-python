#LOGICAL OPERATORS EG OR,AND,NOT
#OR it needs one of them to be true
temp=25 #
is_raining=False
if temp > 35 or temp<0 or is_raining:#note putting is raining is marked as true 
    #what this says is if temperature is greater than 35 or less than zero OR its raining say that
    print('The outdoor event is cancelled')
else:#if none of them are  like that print this
    print('The outdoor event is still scheduled')

