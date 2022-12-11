import random

#Kirjoita ohjelma, joka kysyy käyttäjältä kokonaislukuna ylärajan.

#Ohjelma tulostaa sen jälkeen pienimmästä suurimpaan sellaiset positiivisten kokonaislukujen neliöt laskukaavoineen, jotka ovat pienempiä kuin yläraja.

luku = 0
ylaRaja = int(input("Anna yläraja: "))

while True:
    luku = luku + 1
    if luku*luku <= ylaRaja:
        print(luku,'*',luku,'=',luku*luku)
    if luku*luku+1 == ylaRaja or luku*luku+1 >= ylaRaja:
        break