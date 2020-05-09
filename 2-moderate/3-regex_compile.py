import re

# | for one or the other
familyRegex = re.compile(r'salman|banna|ismail|shameema')
mo1 = familyRegex.search('shammi ismail salman banna kuttan')
print(mo1.group()) #matches first occurance of family name!!

# ? for optional matching
mynameRegex = re.compile(r'salman(ul fares)?')
mo2 = mynameRegex.search('my name is salmanul fares')
print(mo2.group())

# * for zero or more groups, ie needs parenthisis
capitalLaughRegex = re.compile(r'Ha(ha)*')
mo3 = capitalLaughRegex.search('Hahahaha')
print(mo3.group())

# + for one or more groups
smallLaughRegex = re.compile(r'(ha)+')
mo4 = smallLaughRegex.search('hahaha')
print(mo4.group())


# curly for specific repetitions {\d(, \d)}
tenDigitRegex = re.compile(r'\d{10}')
mo5 = tenDigitRegex.search('call me 9447383983 oka?')
print(mo5.group())

# Non greedy and greedy

carSpeedRegex = re.compile(r'\d{1,3}( )?(kmph|km/h)') #matches largest speed, GREEDY
mo6 = carSpeedRegex.search('i was going at 150 kmph') #150 kmph when greedy
print(mo6.group())

laughRegex = re.compile(r'(Ha){2,4}?')
mo7 = laughRegex.search('HaHaHaHaHaHaHaHaHaHa')
print(mo7.group())  #matches HaHa despite HaHaHaHa being in string
                    #Non greedy when ? is added after }

#adding ^ at the start indicates match must occur at the beginning of the string
#same with adding $ at the end means match at end
#. matches anything except \n, '.at' matches mat rat cat...
#for dot to match \n too -> re.compile('.', re.DOTALL)

#.* matches anything!
'''
nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)')
>>> mo = nameRegex.search('First Name: Al Last Name: Sweigart')
>>> mo.group(1)
'Al'
>>> mo.group(2)
'Sweigart'
'''

#.*? is non greedy version of above
'''
>> nongreedyRegex = re.compile(r'<.*?>')
>>> mo = nongreedyRegex.search('<To serve man> for dinner.>')
>>> mo.group()
'<To serve man>'

>>> greedyRegex = re.compile(r'<.*>')
>>> mo = greedyRegex.search('<To serve man> for dinner.>')
>>> mo.group()
'<To serve man> for dinner.>'

'''
