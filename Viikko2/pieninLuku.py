import random

#Kirjoita ohjelma, joka kysyy käyttäjältä kolme kokonaislukua.

#Ohjelma tulostaa sen jälkeen tiedon siitä, mikä luvuista oli pienin.

luku1 = int(input("Anna 1. luku: "))
luku2 = int(input("Anna 2. luku: "))
luku3 = int(input("Anna 2. luku: "))

if luku1 < luku2 and luku1 < luku3:
    print("Luku 1 oli pienin")
elif luku2 < luku1 and luku2 < luku3:
    print("Luku 2 oli pienin")
elif luku3 < luku1 and luku3 < luku2:
    print("Luku 3 oli pienin")