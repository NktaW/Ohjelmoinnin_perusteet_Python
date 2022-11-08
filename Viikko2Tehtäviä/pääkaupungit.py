import random

#Kirjoita ohjelma, joka pyytää käyttäjää syöttämään maan nimen.

#Jos maa on Suomi, Ruotsi tai Norja, ohjelma tulostaa maan pääkaupugin nimen.

#Muuten ohjelma tulostaa, ettei pääkaupungista ole tietoa.

maa = input("Mikä maa? ")

if maa == "Suomi":
    print("Helsinki")
elif maa == "Ruotsi":
    print("Tukholma")
elif maa == "Norja":
    print("Oslo")
else:
    print("En tiedä pääkaupunkia")