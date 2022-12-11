import random

#Ohjelma kysyy käyttäjältä kirjan tyylilajin (merkkijono) ja sivumäärän. 
#Jos kirja on yli 200-sivuinen dekkari, tulostetaan viesti, ettei sitä jaksa lukea. Muuten kirja sopii luettavaksi.

tyylilaji = input("Anna tyylilaji: ")
sivuMaara = int(input("Anna sivumäärä: "))

if sivuMaara > 200 and tyylilaji == "dekkari":
    print("En jaksa lukea")
elif sivuMaara != 200 or tyylilaji != "dekkari":
    print("Luetaan pois")