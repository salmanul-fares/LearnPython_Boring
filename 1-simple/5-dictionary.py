#learn to do dictionaries

#25% completion of course!!

birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}

def printit(array):
    for element in array:
        print(element)


while True:
    print('Enter a name: (0 to quit, 1 for all names, 2 for all name and dates, 3 for all dates)')
    name = input()
    if name == '0':
        break
    if name == '1':
        printit(birthdays.keys())
        continue
    if name == '2':
        printit(birthdays.items())
        continue
    if name=='3':
        printit(birthdays.values())
        continue

    if name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name)
    else:
        print('I do not have bday info for ' + name)
        print('What is their Bday: (blank if you dont know)')
        bday = input()
        if bday != '':
            birthdays[name]=bday
            print('Database updated')

'''
    get and set defualt methods
        picnicItems.get('cup', 0)
        >>>prints value of cup or zero if not defined
        cat.setdefault('color', 'white')
        >>>adds a new item to cat 'color':'white' iff color is not defined
'''
