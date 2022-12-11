import random

#Kirjoita ohjelma, joka kysyy käyttäjältä kaksi lukua.
#Jos käyttäjä antaa kaksi samaa lukua, ohjelma tulostaa "Kiitos! ja suoritus päättyy.
#Muuten ohjelma tulostaa luvuista suuremman esimerkkitulosteen mukaisestai ja kysyy sitten kaksi seuraavaa lukua.

while True:
    luku1 = int(input("Anna luku 1: "))
    luku2 = int(input("Anna luku 2: "))
    if luku1 > luku2:
        print(luku1, "oli suurempi!")       
    elif luku1 < luku2:
        print(luku2, "oli suurempi!")
    else:
        luku1 == luku2
        print("Kiitos!")
        break