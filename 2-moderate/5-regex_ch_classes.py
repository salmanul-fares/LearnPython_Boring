import re

# common character classes(inbuilt)
# \d for digit \D for anything not a digit
# \w for letter, digit or underscore - username characters
# \W inverse of username characters
# \s white spaces \S non-white spaces

#making your own
#(1|2|3|4|5) is same as [1-5] and [12345]

nonvowelsRegex = re.compile(r'[^aeiouAEIOU\s\W\d]')
vowelsRegex = re.compile(r'[aeiouAEIOU]')
vowelStrList = vowelsRegex.findall('The quick brow__n 2343  \n fox jumped over the lazy dog')
vowelDict = {}
for char in vowelStrList:
    vowelDict.setdefault(char,0)
    vowelDict[char] += 1
print(vowelDict)

#squarebrackets are character classes adding ^ inside squarebrackets inverts
