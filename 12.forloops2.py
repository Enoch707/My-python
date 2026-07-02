#lets practice with strings
phone_num='234-915-365-7190'
for i in reversed(phone_num):#AGAIN I PREFER USING i MUST PEOPLE USE X BUT PLS USE THE ONE U  FEEL LIKE USING
    print(i)
print('='*50)

for i in range(1,11):
     if i=='7':
        continue
     print(i)#lets skip the first number 7
print('='*50)

for i in range(1,11):
     if i==7:
        break
     print(i)#lets stop after number 7
     #indentation is so scary that it can mess up ur code
print('='*10)