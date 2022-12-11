import random

#Kirjoita ohjelma, joka pyytää käyttäjää syöttämään...

#nopeuden kilometreinä tunnissa (kokonaisluku)
#matkan kilometreinä (kokonaisluku)
#tiedon siitä, onko autossa turboboost (merkkijono "k" tai "e").

#Jos autossa on turboboost, se tuplaa ilmoitetun nopeuden.

nopeus = int(input("Anna nopeus km/h: "))
matka = int(input("Anna matka: "))
turbo = input("Onko turboboost k/e: " )
if turbo == "k":
    print("Matka taittuu",float(matka/(nopeus*2)),"tunnissa.")
elif turbo == "e":
    print("Matka taittuu", float(matka/nopeus),"tunnissa.")
