#Kirjoita ohjelma, joka kyselee käyttäjältä sanoja ja muodostaa näistä yhden pitkän yhdyssanan.

#Kun yhdyssanan pituus on vähintään 20 merkkiä, ohjelma päättyy ja yhdyssana tulostetaan.

"""
Esimerkkisuoritus:

Anna sana: omena
Anna sana: naama
Anna sana: marsu
Anna sana: sarvi
Yhdyssanaksi tuli: omenanaamamarsusarvi

"""
#Yksi ratkaisu tapa While True/ break silmukalla:
"""
yhdysSana = ''

while True:
    sana = input("Anna sana: ")
    yhdysSana = yhdysSana + sana
    pituus = len(yhdysSana)
    if pituus >= 20:
        print("Yhdyssanaksi tuli:",yhdysSana)
        break

"""
#Toinen ratkaisu tapa While silmukalla:

sana = input("Anna sana: ")
yhdysSana = ''

while sana not in yhdysSana:
    yhdysSana += sana
    if len(yhdysSana) < 20 and len(yhdysSana) != 20:
        sana = input("Anna sana: ")
print('Yhdyssanaksi tuli:', yhdysSana)

