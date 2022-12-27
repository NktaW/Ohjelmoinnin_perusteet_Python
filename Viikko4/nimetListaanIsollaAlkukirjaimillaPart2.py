import random

"""
Laajenna edellisen tehtävän ohjelmaa siten, että se toimii myös kaksiosaisilla, väliviivalla erotetuilla nimillä. Kannattaa kopioida edellisen tehtävän ratkaisu pohjaksi!

Esimerkki ohjelman suorituksesta:

Anna nimi: marko
Anna nimi: maija-leena
Anna nimi:
Nimet: ['Marko', 'Maija-Leena']

"""

nimet = []

while True:
    annaNimi = input("Anna nimi: ")
    nimet.append(annaNimi)
    if annaNimi == '':
        break
nimet = [nimet.title() for nimet in nimet]

nimet = nimet[:-1]

print('Nimet:',nimet)