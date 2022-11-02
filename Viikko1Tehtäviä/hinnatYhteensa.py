import random

#Kirjoita ohjelma, 
# joka kysyy käyttäjältä tuotteen kappalemäärän, yksittäisen tuotteen hinnan ja alenusprosentin, 
# ja laskee ja tulostaa sitten kokonaishinnan alla olevan esimerkin mukaisesti.

#Anna kappalemäärä: 4
#Anna hinta: 2.50
#Anna alennus%: 5
#Hinta yhteensä: 9.5



kpl = int(input("Anna kappalemäärä: "))
hinta = float((input("Anna hinta: ")))
ale = float(input("Anna alennus%: "))
yhteensa = kpl * hinta * (100 - ale) / 100
print("Hinta Yhteensä:", yhteensa)