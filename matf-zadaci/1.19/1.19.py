"""
Napisati program koji izračunava ukupan račun korpe u svakoj prodavnici
i ispisuje cene na standardni izlaz.
"""
import json
from functools import reduce

fi_korpa = open('korpa.json','r')
korpa = json.loads(fi_korpa.read())
fi_korpa.close()

fi_maxi = open('maxi_cene.json','r')
cene_maxi = json.load(fi_maxi)
fi_maxi.close()

fi_idea = open('idea_cene.json','r')
cene_idea = json.load(fi_idea)
fi_idea.close()

fi_shopngo = open('shopngo_cene.json','r')
cene_shopngo = json.load(fi_shopngo)
fi_shopngo.close()

# Функција подразумева да артикал постоји у продавници, и да је јединствено одређен
def cena_artikla(artikal,prodavnica):
    return [int(x['cena']) for x in prodavnica if x['ime'] == artikal][0]

prodavnice = [cene_maxi,cene_idea,cene_shopngo]

for cene in prodavnice:
    print(str((reduce(lambda x,y: (cena_artikla(y['ime'],cene) * y['kolicina']) + x,korpa,0))))