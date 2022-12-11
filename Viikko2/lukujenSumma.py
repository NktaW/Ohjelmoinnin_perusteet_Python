import random

#Kirjoita ohjelma, joka kyselee käyttäjältä yksi kerrallaan lukuja.
#Kun käyttäjä syöttää luvun nolla, ohjelma tulostaa lukujen summan ja ohjelman suoritus päättyy.

laskuri = 0


while True:
    luku = int(input("Anna luku: "))
    if luku !=0:
        luku + luku
        laskuri = laskuri + luku
    elif luku == 0:
        print("Lukujen summa on", laskuri)
        break