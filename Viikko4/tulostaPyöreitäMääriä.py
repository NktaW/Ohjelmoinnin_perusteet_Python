import random

#Kirjoita funktio, tulosta_pyoreat(luku: float, viesti: str).

#joka saa parameterikseen liukuluvun ja viestin merkkijonona. 
#Funktio  pyöristää luvun matemaattisesti lähimpään kokonaislukuun ja tulostaa sitten annettua viestiä tämän kokonaisluvun mukaisen määrän. 

#Koodini alkaa tästä...

def tulosta_pyoreat(luku: float, viesti: str):
    luku = round(luku)
    for i in range(luku):
        print(viesti)


#koodini loppuu tähän.


luvut = [0.1, 0.25, 0.4, 0.5, 0.6, 0.8, 0.99]
base = [1, 2, 3, 2, 3, 2, 4]
viestit = "Hei Moi Heippa Moikka Terve Tere Moro Morjens Morientes".split()

random.shuffle(luvut)
random.shuffle(base)

print("<ingore>Testataan funktiota tulosta_pyoreat(luku: float, viesti: str)")

for i in range(5):
    luku = base.pop() + luvut.pop()
    viesti = random.choice(viestit)
    print(f"Kutsutaan tulosta_pyoreat({luku}, \"{viesti}\")")
    tulosta_pyoreat(luku, viesti)