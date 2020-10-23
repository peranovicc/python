# A file containing all the even-numbered lines from the original file. 
# Assume 1-based numbering of lines.

fi = open('input.txt','r')
fo = open('output.txt','w')

fo.write(''.join([x for x in fi.readlines()[1::2]])) # Extended slicing


