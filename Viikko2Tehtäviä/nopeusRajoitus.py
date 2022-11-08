import random

#Kirjoita ohjelma, joka pyytää käyttäjää syöttämään nopeusrajoituksen ja ajetun nopeuden.
#Jos nopeus ylittää nopeusrajoituksen yli kymmenellä, ohjelma kertoo, että sakkoja tuli.
#Muuten ilmoitetaan, että kuljettaja selvisi sakoista.

nopeusRajoitus = int(input("Anna nopeusrajoitus: "))
nopeus = int(input("Anna nopeus: "))

if nopeus > nopeusRajoitus + 10:
    print("Sakkoa tuli!")
else:
    nopeus < nopeusRajoitus + 10
    print("Selvisit ilman sakkoa.")