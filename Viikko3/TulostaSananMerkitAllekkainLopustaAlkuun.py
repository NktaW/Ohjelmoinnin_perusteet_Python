#Muuta edellistä ohjelmaa siten, että ohjelma tulostaa nyt sanan merkit viimeisestä ensimmäiseen allekkain.

#Kirjoita ohjelma, joka pyytää käyttäjää syöttämään sanan. Ohjelma tulostaa sen jälkeen sanan merkit allekkain yksitellen viimeisestä ensimmäiseen.

#Esimerkki ohjelman suorituksesta:
#Anna sana: norsu
#u
#s
#r
#o
#n

sana = input("Anna Sana: ")


indeksi = len(sana) - 1

while indeksi >= 0:
    print(sana[indeksi])
    indeksi -= 1



sana = input("Anna Sana: ")


indeksi = len(sana) - 1

while indeksi >= 0:
    print(sana[indeksi])
    indeksi -= 1