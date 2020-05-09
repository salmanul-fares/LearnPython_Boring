#strings have no end character like in C/C++ ('\0')
#print("hello"[6]) Index Error!!

#slices are useful asf
name = "Salmanul Fares"
print(name[len(name)-5:]) #Last five characters

print(name.upper())
print(name.lower().center(40))
print('ul' in name.lower())
print(name.lower().endswith('fares'))

#list of strings
arra = ['My', 'name', 'is', 'Simon']
print('<>'.join(arra).center(40))

print(name.split('a')) #also useful for splitting multiline strings
