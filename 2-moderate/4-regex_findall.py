import re

'''While search() will return a Match object of the first matched text
 in the searched string, the findall() method will return the strings of every
 match in the searched string.'''

indianMobilePhoneRegex = re.compile(r'''
    (
        #country code
        (
            (\+|0|00)?91
            (\ |-)?
        )?

        #preceeding zero
        0?

        #10 digit phone number
        (
            \d{10}                              #1234567890
            |
            (\d{4}(-|\ )\d{3}(-|\ )\d{3})       #1234 567 890 &&  1234-567-890
            |
            (\d{5}(-|\ )\d{5})                  #12345 67890  &&  12345-67890
        )

    )''',re.VERBOSE)

mo = indianMobilePhoneRegex.findall('''let's see.. +91 94473 12345 okay? 091 0091 91 sd 09447 383 284''')
for num in mo:
    print(num[0])

print(mo)

#mo is a list of tuples each of which are similar to .group call
#find all returns a list of strings if there are no groups in the regex

xmasRegex = re.compile(r'\d+\s\w+')
op = xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge')
print(op)
