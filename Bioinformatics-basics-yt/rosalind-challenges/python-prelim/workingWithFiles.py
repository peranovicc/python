# Tutorial for working with files in python

# Opening file
# Modes:
# r - read mode (the file is opened for reading)
# w - write mode (the file is opened for writing, and if a file having the same name exists, it will be erased)
# a - append mode (the file is opened for appending, which means that data is only to be added to the existing data in the file)

fi = open('input.txt','r') 
# print(fi.read()) # read() can take parameter n (number of bytes to read, when omitted it reads whole file)
# print(fi.readline().strip()) # reads next line and strips trailing \n (newline)
print(fi.readlines()) # List of all lines in file
fo = open('output.txt','w')
fo.write('Neki rezultat programa') # Creates or replaces output.txt with output.txt with given string

fi.close()
fo.close()