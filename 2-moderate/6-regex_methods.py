'''REGEX_RECAP

• The ? matches zero or one of the preceding group.•
• The * matches zero or more of the preceding group.•
• The + matches one or more of the preceding group.•
• The {n} matches exactly n of the preceding group.•
• The {n,} matches n or more of the preceding group.•
• The {,m} matches 0 to m of the preceding group.•
• The {n,m} matches at least n and at most m of the preceding group.•
• {n,m}? or *? or +? performs a nongreedy match of the preceding group.•
• ^spam means the string must begin with spam.•
• spam$ means the string must end with spam.•
• The . matches any character, except newline characters.•
• \d, \w, and \s match a digit, word, or space character, respectively.•
• \D, \W, and \S match anything except a digit, word, or space character, respectively.•
• [abc] matches any character between the brackets (such as a, b, or c).•
• [^abc] matches any character that isn’t between the brackets.•
'''

import re

#re.IGNORECASE or re.I      |||     ignore case/ case-insensitive matches
robocop = re.compile(r'robocop', re.I)
print(robocop.findall('robocop RoBOcOP RoboCop roboCOP'))

#Regexobj.sub('abc', str)   |||     substitutes the matches in str with 'abc'
namesRegex = re.compile(r'Agent \w+')
print(namesRegex.sub('█████', 'Agent Alice gave the secret documents to Agent Bob.'))

#re.VERBOSE                 ||| ignores whitespace and comments
#see 4-regex_findall.py

#COMBINE THESE USING | (Bitwise or)
