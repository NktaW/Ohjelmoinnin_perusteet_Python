#Kirjoita ohjelma, joka kysyy käyttäjältä sanan. Ohjelma tulostaa sen jälkeen kirjain kerrallaan tiedon siitä, löytyvätkö sanasta kirjaimet "p", "y", "t", "h", "o" tai "n".

#Lukumäärällä ei ole väliä, ainoastaan sillä, löytyykö kirjainta vai ei.

#Katso mallia alla olevasta esimerkkitulostuksesta:

"""
Anna sana: potilas
p löytyy
y ei löydy
t löytyy
h ei löydy
o löytyy
n ei löydy

"""


sana = input("Anna sana: ")

if 'p' in sana:
    print('p löytyy')
else:
    print('p ei löydy')
if 'y' in sana:
    print('y löytyy')
else:
    print('y ei löydy')
if 't' in sana:
    print('t löytyy')
else:
    print('t ei löydy')
if 'h' in sana:
    print('h löytyy')
else:
    print('h ei löydy')
if 'o' in sana:
    print('o löytyy')
else:
    print('o ei löydy')
if 'n' in sana:
    print('n löytyy')
else:
    print('n ei löydy')