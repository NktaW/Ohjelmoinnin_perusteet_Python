import random

#Kirjoita ohjelma, joka pyytää käyttäjää syöttämään syntymävuoden ja nykyisen vuoden.
#Jos käyttäjä on vähintään kahdeksantoista, ohjelma tulostaa tervetuloviestin. Muuten ohjelma tulostaa tiedon siitä, ettei ikää ole trapeeksi.

syntymavuosi = int(input("Anna syntymavuosi: "))
nykyinenVuosi = int(input("Anna nykyinen vuosi: "))

if nykyinenVuosi - syntymavuosi >=18:
    print("Tervetuloa")
elif nykyinenVuosi - syntymavuosi <= 18:
    print("Et ole tarpeeksi vanha.")


print("")

