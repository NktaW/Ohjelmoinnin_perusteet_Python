#Kirjoita ohjelma, joka pyytää käyttäjää syöttämään lauseen. Ohjelma tulostaa tämän jälkeen lauseen ekan sanan.

#Voi olettaa, että lausessa on vähintään kaksi sanaa.

lause = input("Anna lause: ")

annettuLause = lause.split()

ekaSana = annettuLause[0]

print(f'Eka sana on {ekaSana}')