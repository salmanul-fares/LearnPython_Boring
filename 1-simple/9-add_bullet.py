'''
program adds a bullet point to whatever lines is in the clipboard
'''
bullet = '* '       #text that is prefixed to each line of text in Ctrl+C
                    #defualt value is '* '

seperator = '\n'    #text that identifies between lines
                    #defualt value is '\n'


import pyperclip
text = pyperclip.paste()

lines = text.split(seperator)
for i in range(len(lines)):
    lines[i] = bullet + lines[i]
text = seperator.join(lines)



pyperclip.copy(text)
