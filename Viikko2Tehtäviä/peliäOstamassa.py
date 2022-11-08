import random

#Käyttäjä on ostamassa tietokonepeliä.
#Kirjoita sovellus, joka kysyy ensin käyttäjän iän. Jos ikä on alle 18, ohjelma kertoo kuinka monta vuotta tämän tulee vielä odottaa ennen kuin pelin voi laillisesti ostaa.

#Jos käyttäjä on täysi-ikäinen, ohjelma kysyy pelin kappalemäärän. 
# Jos käyttäjä ostaa 5 peliä tai enemmän, kappalehinta on 39.90. Muuten se on 49.90. Lopuksi ohjelma tulostaa pelien yhteishinnan.

ika = int(input("Anna ikä:"))
hinta = 49.90

if ika < 18:
    print("Odota vielä",18 - ika,"vuotta!")
if ika >= 18:
    kpl = int(input("Kuinka monta?"))
    if kpl >= 5:
        print("Hinta yhteensä:",(39.90 / hinta )* hinta * kpl)
    else:
        print("Hinta yhteensä:", hinta * kpl)