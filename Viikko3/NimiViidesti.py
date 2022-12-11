import random
#Kirjoita funktio nimi_viidesti(nimi), joka saa parametrikseen nimen (merkkijono).

#Funktio luo uuden merkkijonon, jossa on parametrina annettu nimi viidesti peräkkäin ja palauttaa tämän merkkijonon kutsujalle.

print("Testataan funktiota nimi_viidesti...")

nimet = "Pekka Paula Pirjo Antti Markku Maija Anne Elisa Elias".split()
random.shuffle(nimet)
nimet = nimet[:3]

def nimi_viidesti(nimi):
    indeksi = 0
    while indeksi <= 5:
        #print(nimi)
        indeksi += 1
        nimi *= 5
        return nimi


for nimi in nimet:
    print(f"Kutsutaan nimi_viidesti({nimi})...")
    a = nimi_viidesti(nimi)
    print(a)

