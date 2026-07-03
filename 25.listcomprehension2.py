#lets do one where we list a bunch of grades and the one that passes gets shown

passsys={}
while True:
  
    op=input('Database Update(D)\nAdmission Status(A)\n: ').upper()
    if op=='D':
        student=input('Whats your name: ')
        grade=int(input('What did you score'))
        passsys.update({student:grade})
    elif op=='A':
        name=input('Student name: ')
        stud=passsys.get(name)
        if stud is None:
            student=input('Whats your name: ')
            grade=int(input('What did you score'))
            passsys.update({student:grade})
        if stud<60:
            print(f'{name.title()} is unable for admission this year')
        else:
            print(f'{name.title()} is admitted this year!')
    elif op=='E':
        print('Have a nice day!')
        break
            

