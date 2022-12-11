import random
#Fibonaccin lukusarjassa luku on aina kahden edellisen luvun summa. Kaksi ensimmäistä lukua ovat 1 ja 1.

#Sarjan alku näyttää siis tältä:
#1, 1, 2, 3, 5, 8, 13, 21 jne.

#Koska muutkin haluavat savupiippuunsa vastaavaan lukusarjan, mutta savupiippuja on eri kokoisia, tarvitaan funktio, joka luo eri pituisia sarjoja.

#Kirjoita funktio luo_fibosarja(n), joka luo sarjan allekain olevia lukuja. Sarjassa on n ensimmäistä lukua alkaen luvuista 1 ja 1.

#Huomioita:

#Jos haluat merkkijonoon rivinvaihdon, käytä erikoismerkkiä "\n".
#Jotta voit lisätä lukuja merkkijonon perään, täytyy luvut ensin muuntaa merkkijonoiksi str() -funktiolla.

#Minun koodi alkaa tästä
def luo_fibosarja(n):
    i = 0
    edellinen = 1
    nykyinen = 1

    sarja = ''

    while i < n:
        sarja = sarja + str(edellinen)+"\n"
        seuraava = edellinen + nykyinen
        edellinen = nykyinen
        nykyinen = seuraava

        i += 1

    return sarja
#Koodini loppuu tähän

n = [2, 4, 8, 10]
random.shuffle(n)

print("Testataan funktiota tulosta_fibot...")

for kpl in n:
    print(f"Kutsutaan tulosta_fibot({kpl})")
    jono = luo_fibosarja(kpl)
    print(f"Funktion palauttama arvo:")
    print(jono)