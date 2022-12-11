import random
#Kirjoita ohjelma, joka kyselee käyttäjältä yksi kerrallaan lukuja.
#Kun käyttäjä syöttää luvun nolla, ohjelma tulostaa suurimman syötetyistä luvuista ja ohjelman suoritus päättyy.

suurinLuku = 0

while True:
    luku = int(input("Anna luku: "))
    if luku != 0 and luku > suurinLuku:
        suurinLuku = luku
    elif luku == 0:
        print("Suurin luku on", suurinLuku)
        break

    
