"""
Korisnik na standarni ulaz unosi podatke o imenu, prezimenu i godinama.
Program potom kreira JSON objekat junak, koji ima podatke Ime, Prezime i Godine, i ispisuje ga
na standardni izlaz, a potom i u datoteku [junak.txt]
"""
import json


fo = open('1.17-junakOut.txt','w')
data = input('Uneti ime, prezime i godine: ime prezime godine').split()
obj = {
    "ime": data[0],
    "prezime": data[1],
    "godine": data[2]
}
fo.write(json.dumps(obj))
fo.close()