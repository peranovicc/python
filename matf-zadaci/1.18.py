"""
Napisati program koji iz datoteke datoteka.txt učitava JSON objekat, a potom
na standardni izlaz ispisuje podatke o imenu, prezimenu i godininama
"""
import json

fi = open('1.18-datoteka.txt','r')
print(json.loads(fi.read()))