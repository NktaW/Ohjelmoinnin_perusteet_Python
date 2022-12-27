import random
"""
Kirjoita ohjelma, joka kyselee käyttäjältä nimiä. Käyttäjä syöttää nimet kokonaan pienillä kirjaimilla.
Ohjelma muuttaa nimen alkukirjaimen isoksi ja tallentaa nimen sitten listaan. Jos käyttäjä syöttää tyhjän merkkijonon, ohjelma tulostaa listan ja sen suoritus päättyy.

Esimerkki ohjelman suorituksesta:

Anna nimi: marko
Anna nimi: maija
Anna nimi:
Nimet: ['Marko', 'Maija']

"""


nimet = []

while True:
    annaNimi = input("Anna nimi: ")
    nimet.append(annaNimi)
    if annaNimi == '':
        break
nimet = [nimet.capitalize() for nimet in nimet]

nimet = nimet[:-1]

print('Nimet:',nimet)