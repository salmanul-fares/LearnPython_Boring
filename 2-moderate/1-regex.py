'''Regular expressions are helpful, but not many non-programmers know about them even though most modern text editors and word pro-cessors, such as Microsoft Word or OpenOffice, have find and find-and-replace features that can search based on regular expressions. Regular expressions are huge time-savers, not just for software users but also for www.it-ebooks.info
148Chapter 7programmers. In fact, tech writer Cory Doctorow argues that even before teaching programming, we should be teaching regular expressions: '''

import re

#re works in objects

simplePhoneRegex = re.compile(r'\d\d\d\d-\d\d\d-\d\d\d')
#a regex to match a phone number like 9447-383-284
#   r'string here' is used to ovverride escape character detection!!! raw strings

#to search for a phone number in a text
matchObject = simplePhoneRegex.search('a regex to match a phone number like 9447-383-284 lets see it work')
#matchObject is None if a match is not found

print('Number found: ' + matchObject.group())

#visit www.regexpal.com
