#a dictionary is a collection(lists,set,tuples) with a key:value pair
#                                    ordered and changable but no duplicates
capitals={'usa':'Washington d.c.',
          'india':'New delhi',
          'china':'Beijing',
          'russia':'Moscow'}
while True:
    states=input('What state: ')
    #for help
    # print(dir(capitals))
    caps=capitals.get(states)#this means any key i type in(USA,INDIA...)find its value(washisgto.....)
    #this is what i mean by key value if u search on ur fav ai it will try to match this its almost like an actual dictionary
    #like click ur word and get ur meaning
    if capitals.get(states):
        print('It exists')
        print(caps)
        
    else:
        print('Not in the dictionary ')