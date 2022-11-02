import random

#Kirjoita ohjelma, joka pyytää käyttäjää syöttämään kaksi kokonaislukua.

#Jos luvut ovat samat, ohjelma tulostaa "Samat luvut!". Muuten ohjelma ei tulosta mitään.

luku1 = int(input("Anna luku 1: "))
luku2 = int(input("Anna luku 2: "))

if luku1 == luku2:
    print("Samat luvut!")