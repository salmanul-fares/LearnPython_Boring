hellofile = open('../1-simple/3-lists.py')
    # ^^ is same as open('fname','r')
#listOfStringValues=hellofile.readlines() #reads line by line
#hugeString = hellofile.read()

hugeString = 'imagine some sample content'
print(hugeString)

writefile = open('txtfileio.txt','w')
writefile.write('hello salman\n')
writefile.write(hugeString)
writefile.close()
