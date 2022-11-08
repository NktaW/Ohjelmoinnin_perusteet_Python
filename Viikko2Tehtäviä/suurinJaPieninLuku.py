import random
#Laajenna edellisen tehtävän ohjelmaa siten, että ohjelma tulostaa nyt myös pienimmän käyttäjän syöttämän luvun.
#Huomaa, että käyttäjä voi syöttää myös negatiivisia lukuja.

#Eli: kirjoita ohjelma, joka kyselee käyttäjältä yksi kerrallaan lukuja.
#Kun käyttäjä syöttää luvun nolla, ohjelma tulostaa suurimman ja pienimmän syötetyistä luvuista ja ohjelman suoritus päättyy.


suurinLuku = 0
pieninLuku = 0

while True:
    luku = int(input("Anna luku: "))
    if luku != 0 and luku > suurinLuku:
        suurinLuku = luku
    elif luku != 0 and luku < pieninLuku:
        pieninLuku = luku
    elif luku == 0:
        print("Suurin luku on", suurinLuku)
        print("Pienin luku on", pieninLuku)
        break
