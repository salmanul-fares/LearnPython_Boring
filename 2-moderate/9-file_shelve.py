import shelve
import os
import pprint
'''
shelfFile = shelve.open('storage.dat')
names = ['salman', 'banna', 'ismail', 'banna']
shelfFile['names'] = names
shelfFile.close()
''' #data stored in dat file!

if os.path.exists('storage.dat'):
    shelfFile = shelve.open('storage.dat')
    names = shelfFile['names']
    pprint.pprint(names)
