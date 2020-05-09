import re

#adding brackets to regex compiler seperates matches into groups

#for a phone number like +91 494 242-1484
regexObject = re.compile(r'(\+\d\d|\d\d) (\d\d\d) \d\d\d-\d\d\d\d') #+ is a regex character for something idk
matches = regexObject.search('for a phone number like 91 494 242-1484 let\'s say')

print('country code: ' + matches.group(1))
print('area code: ' + matches.group(2))
print('phone num found: ' + matches.group()) #or matches.group(0)

#|symbol gives you options as shown in 3-regexopts
