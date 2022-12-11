import random

#Kirjoita ohjelma, joka kysyy käyttäjältä alku- ja loppuluvun.
#Ohjelma tulostaa sen jälkeen allekkain kaikki luvut välitlä
alku = int(input("Anna alku:"))
loppu = int(input("Anna loppu: "))

while True:
    print(alku)
    alku = alku + 1

    if alku == loppu:
        print(loppu)
        break