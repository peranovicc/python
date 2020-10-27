"""
Napisati program koji iz datoteke [niska.txt] učitava nisku, a u datoteku [slova.txt]
ispisuje sve karaktere koji nisu slova.
"""

fi = open('1.16-niska.txt','r')
fo = open('1.16-niskaOut.txt','w')

fo.write(''.join(str(x) for x in fi.read() if not x.isalpha()))

fi.close()
fo.close()