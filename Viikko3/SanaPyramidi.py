#Kirjoita ohjelma, joka kysyy käyttäjältä merkkijonon, ja tulostaa sitten alla olevan esimerkin mukaisen pyramidin.
"""
Esimerkkisuoritus:

Anna merkkijono: laiva
l
la
lai
laiv
laiva

"""

sana = input("Anna merkkijono: ")

indeksi = 1

while indeksi <= len(sana):
    sanan_osa = sana[:indeksi]
    print(sanan_osa)
    indeksi += 1
