# TODO: sample list program
print(['x','y',35,56.89][::-1]*4)
#for c in "Salman":#or any array
    #print(c)

#in and not in ops

cat=['fat', 'black', 'loud']
size, color, dispo = cat
#print(size + color + dispo)

cat.append('sala') #cat = cat + ['sala']
cat.remove('fat') # '-' not supported

#other like sort
#tuplle and string not mutable
copy = cat #only reference no copy made!!!
copy[2]='not sala'
print(cat)
