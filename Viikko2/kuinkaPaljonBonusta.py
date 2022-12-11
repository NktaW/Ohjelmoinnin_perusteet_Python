import random

#Kirjoita ohjelma, joka kysyy käyttäjän käyttämän rahamäärän.

#Ohjelma ilmoittaa sen jälkeen käyttäjän tienaamat bonuspisteet seuraavan taulukon mukaisesti:

#rahaa      bonusta
#0 - 99         10
#100 - 499      30
#500 - 999      50
#1000 - 4999   100
#yli 5000      150

rahamaara = int(input("Kuinka paljon käytit rahaa? "))

if rahamaara <= 99:
    print(rahamaara,"eurolla saa", 10, "bonuspistettä!" )
elif rahamaara <= 499:
    print(rahamaara,"eurolla saa", 30, "bonuspistettä!")
elif rahamaara <= 999:
    print(rahamaara,"eurolla saa", 50, "bonuspistettä!")
elif rahamaara <= 4999:
    print(rahamaara,"eurolla saa", 100, "bonuspistettä!")
else:
    print(rahamaara,"eurolla saa", 150, "bonuspistettä!")

