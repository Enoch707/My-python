#these are alternative to using elif statement
#do something if something matches something
def day(day):
    if day== 1:
        print('ITS SUNDAY')    
    elif day== 2:
        print('ITS MONDAY')
    elif day== 3:
        print('ITS TUESDAY')
    elif day== 4:
        print('ITS WEDNESDAY')
    elif day== 5:
        print('ITS THURSDAY')
    elif day== 6:
        print('ITS FRIDAY')
    elif day== 7:
        return 'ITS SATURDAY'
    else:
        return 'Input a valid number'
#leaarn the habit of using return
#this is too long lets be more efficient

def day1(day):
    match day:#match day with 
        case 1:# instead of if day == 1 this means if match == case 
            return 'ITS SUNDAY'    
        case 2:
            return 'ITS MONDAY'
        case 3:
            return 'ITS TUESDAY'
        case 4:
            return'ITS WEDNESDAY'
        case 5:
            return 'ITS THURSDAY'
        case 6:
            return 'ITS FRIDAY'
        case 7:
            return 'ITS SATURDAY'
        case _ :#_underscore means if there are no matching cases execute my code
            return 'Input a valid number'
number=int(input('Number of the week: '))
print(day1(number))
#IT MAKES UR CODE NEATER
#LETS REVERSE IT AND MAKE IT STRINGS INSTEAD
def WEEK(day):
    match day:#match day with 
        case 'Sunday':# instead of if day == 1 this means if match == case 
            return 'Code 1'    
        case 'Monday':
            return 'Code 2'
        case 'Tuesday':
            return 'Code 3'
        case 'Wednesday':
            return'Code 4'
        case 'Thursday':
            return 'Code 5'
        case 'Friday':
            return 'Code 6'
        case 'Saturday':
            return 'Code 7'
        case _ :#_underscore means if there are no matching cases execute my code
            return 'Input a valid day of the week'
week_=input('Day of the week: ').title()
print(WEEK(week_))
#Lets do one that checks whether what u put is a weekend day or not
def WEEKEND(day):
    match day:#match day with 
        case 'Sunday'|'Saturday':# if day is sunday OR saturday do this | means or
            return 'Its is a weekend'    
        case _ :#_underscore means if there are no matching cases execute my code
            return f'HOW IS {day} A WEEKEND!'
week_=input('Day of the week: ').title()
print(WEEKEND(week_))
