import random

#Kirjoita ohjelma, joka kyselee alla olevien esimerkkien mukaisesti käyttäjältä neljä kysymystä, joilla kerätään tietoa asunnon siisteydestä.
#Onko nurkissa pölyä? kyllä
#Ovatko matot likaiset? kyllä
#Onko tiskialtaassa likaisia astioita? ei
#Ovatko ikkunat likaiset? ei
#Pyyhi pölyt!
#Tamppaa matot!
#Siivous valmis!

#Jos käyttäjä vastaa johonkin kohtaan "kyllä"; ohjelma tulostaa sitä vastaavan siivousohjeen. Lopuksi tulostetaan "Siivous valmis!".

nurkissa = input("Onko nurkissa pölyä? ")
matot = input("Ovatko matot likaiset? ")
tiskiallas = input("Onko tiskialtaassa likaisia astioita? ")
ikkunat = input("Ovatko ikkunat likaiset? ")

valmis = "Siivous valmis!"

if nurkissa == "kyllä":
    print("Pyyhi pölyt!")
if matot == "kyllä":
    print("Tamppaa matot!")
if tiskiallas == "kyllä":
    print("Pese astiat!")
if ikkunat == "kyllä":
    print("Pese ikkunat!")
print(valmis)