import re

stateFile = open('states.txt', 'r')
states = stateFile.read()
stateFile.close()

dictmakerFile = open('statedict.py', 'w')

statesre = re.compile('(\\d+)\n\n(.*)\n\n(.*)')
match = statesre.findall(states)

stateslist = 'states = {'

for set in match:
    stateslist = stateslist + '\'' + set[1] + '\':\'' + set[2] + '\', '

stateslist = stateslist + '}'

dictmakerFile.write(stateslist)
