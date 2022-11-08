#Kirjoita ohjelma, joka kysyy käyttäjältä tuotteita ja koostaa näistä kauppalistan.
#Kun käyttäjä antaa saman tuotteen kahteen kertaan peräkkäin, ohjelma tulostaa listan alla olevan esimerkkisuorituksen mukaisesti ja sen suoritus päättyy.

#Vinkki: tarvitset luultavasti ohjelmassa useita apumuuttujia - mieti mitä ne olisivat. Ainakin edellinen syötetty tuote olisi varmasti hyvä pitää muistissa...

#Esimerkki ohjelman suorituksesta:

#Anna tuote: tomaatti
#Anna tuote: kurkku
#Anna tuote: perunat
#Anna tuote: perunat
#Kauppalista:
#tomaatti ja kurkku ja perunat
#------------------------------------------------


kauppaLista = []

while True:
    tuote = input('Anna tuote: ')
    if tuote not in kauppaLista:
        kauppaLista += [tuote]
    elif tuote in kauppaLista:
        kauppaLista = kauppaLista
        print("Kauppalista:")
        print(' ja '.join(kauppaLista))
        break