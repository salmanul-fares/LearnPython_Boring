#in python the list reference is passed when = is used
#copy solves the issue

import copy

spam = ['a',2, [1,34,'sal',[1,2]], 'salman']
fakecopy = spam                 #fakecopy is only a reference to spam
goodCopy = copy.copy(spam)      #seperate list made (duplicate)
deepCopy = copy.deepcopy(spam)  #seperate list with inner lists included

fakecopy[-1] = 'fares47'
print(spam)
print(goodCopy)
print(deepCopy)

#what if strings

ogtext="salman"
cptext=ogtext
cptext="fares47"
print(ogtext) #no issues

'''must find the difference between copy and deepcopy'''
