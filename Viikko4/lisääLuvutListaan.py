import random

"""
Kirjoita ohjelma, joka kyselee käyttäjältä kokonaislukuja yksi kerrallaan.

Ohjelma tallentaa luvut listaan siinä järjestyksessä, jossa käyttäjä ne syöttää.

Kun käyttäjä syöttää luvun -1, ohjelman tulostaa listan ja sen suoritus päättyy.

Esimerkkisuoritus:

Anna luku: 9
Anna luku: 3
Anna luku: 11

"""


luvut = []

while True:
    annaLuku = int(input('Anna luku: '))
    if annaLuku != -1:
        luvut.append(annaLuku)
    else:
        break
print('Lista:',luvut)

