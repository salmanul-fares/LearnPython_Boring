import os
#os.chdir('/home/manjaro') #changes folder, cd
#os.makedirs('waffles') #makes folder(s), mkdir
print(os.getcwd()) #pwd
print(os.listdir()) #lists current folder, ls
#print(os.listdir('/home/manjaro/Downloads')) #lists mentioned folder
print(os.path.sep) #prints / on unix based systems and \ on windows
print(os.path.join('usr','salman','downloads')) #uses / or \ depending on OS
print(os.path.abspath('../0-basics'))#converts relpath to abspath
print(os.path.relpath('/home/manjaro/Downloads')) #gets relpath
print(os.path.dirname('/usr/home/salman.exe')) #everything before last \ or /
print(os.path.basename('/usr/home/salman.exe')) #everything after last \ or /
print(os.path.split('/usr/home/salman.exe')) #splits into directory and filename
                    #use pathstring.split(os.path.sep) to get list of directories
print(os.path.getsize('/7-files.py'))
#os.path.exists(path)
#os.path.isdir(path)
#os.path.isfile(path)
