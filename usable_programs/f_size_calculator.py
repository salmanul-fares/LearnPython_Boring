'''program to find the file/folder size of path in clipboard'''
import os
import pyperclip

folderPath = pyperclip.paste()
#folderPath = '/home/manjaro/Videos'

def fsize(fpath):
    size = 0
    if(os.path.isfile(fpath)):
        size = size + os.path.getsize(fpath)
    elif(not os.path.isdir(fpath)):
        return -1 #error case where fpath is not a valid file/directory
    else: #if fpath is folder recursively find size of the files & subfolders
        for fname in os.listdir(fpath):
            size = size + fsize(fpath + os.path.sep + fname)
    return size

size = fsize(folderPath)
factor = 0
units = ['bytes','kb','mb','gb','tb']

while(size>1024 and factor<len(units)):
    size /= 1024
    factor += 1

print(size, units[factor])
