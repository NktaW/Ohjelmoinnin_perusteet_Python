#Kirjoita ohjelma, joka pyytää käyttäjää syöttämään kokonaisluvun.

#Ohjelma tulostaa tämän jälkeen kaikki kokonaisluvut, joilla luku on jaollinen. 
# Luvut tulostetaan suuruusjärjestyksessä ykkösestä alkaen alla olevan esimerkin mukaisesti.
#Esimerkkisuoritus:

#Anna luku: 8
#8 on jaollinen luvulla 1
#8 on jaollinen luvulla 2
#8 on jaollinen luvulla 4
#8 on jaollinen luvulla 8

luku = int(input("Anna luku: "))

jakaja = 1

while jakaja <= luku:
    if luku % jakaja == 0:
        print(luku, 'on jaollinen luvulla', jakaja)

    jakaja +=1