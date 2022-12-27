import random

#Kirjoita ohjelma, joka kyselee käyttäjältä kokonaislukuja. 
#Kun käyttäjä syöttää luvun -1, ohjelma tulostaa käyttäjän yhteensä syöttämien kolmosten määrän ja lisäksi syötettyjen lukujen summan.

#Jos käyttäjä esim. syöttäisi luvut 33, 13 ja -1, kolmosten määrä olisi kolme (kaksi luvussa 33, yksi luvussa 13) ja summa 46.

#Vinkki: muunnos joko kokonaisluvusta merkkijonoksi tai päinvastoin on varmasti tarpeellinen operaatio. Kertaa myös viime kerralla esitetyt merkkijonometodit!

kolmosia = 0
summa = 0

while True:
    syote = input("Anna luku: ")
    luku = int(syote)

    if luku == -1:
        break

    summa = summa + luku

    kolmosia = kolmosia + syote.count("3")

print(f'Kolmosia: {kolmosia}')
print(f'Summa: {summa}')