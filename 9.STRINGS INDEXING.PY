#Indexing probably niche but it might be needed 
#This is to find,hmm not find more like access a certain character using[]and numbers aka position
phoneno='1234-5678-9012-3456'
print(phoneno[7])# u need to understand than computers dont count from 1 like decimals they count from 0 
#so 1 is position 0 and 6 is position7
print(phoneno[0:4])#colon in python is like to basically saying from first position to fourth postion
#WE CAN ADD ONE MORE 
#So i can tell python how many numbers to jump before printing like
print(phoneno[0:4:2])#2 meaning jump 2 before the next count like 1,4,6,- like that
#also to list character from a character to the end id
print(phoneno[3:])#this is from third pos down
print(phoneno[:3])#this is from third pos up
print(phoneno[-4])#negative means start from the back and starts to counts with -1
print(phoneno[:])#means everything
print(phoneno[::3])#means starting jumping by 3 character
print(phoneno[::-1])#to reverse the characters
#format [start:end:step]
