import random

#Kirjoita seuraavat kaksi funktiota:

#lisaa_seuraava(aakkosjono: str) -> str

#saa parametrikseen määrittelemättömän pituisen pätkän aakkosten alusta (pienillä kirjaimilla). 
#Funktio palauttaa merkkijonon, jossa jonoon on lisätty seuraava aakkonen (esim. "abc" --> "abcd" tai "abcdefg" --> "abcdefgh").

#Funktio 2

#lisää samalla logiikalla jonon perään yhden tai useampia aakkosia. Jos esim. jonoon "abc" lisättäisiin 3 aakkosta, tulos olisi "abcdef".

def lisaa_seuraava(aakkosjono: str) -> str:
    pituus = len(aakkosjono)
    seuraava = aakkoset[pituus]
    return aakkosjono + seuraava

def lisaa_monta(aakkosjono: str, maara: int) -> str:
    i = 0
    for i in range(maara):
        pituus = len(aakkosjono)
        seuraava = aakkoset[pituus]
        aakkosjono = aakkosjono + seuraava
    return aakkosjono
    






aakkoset = "abcdefghijklmnopqrstuvwxyzåäö"

print("Testataan funktiota lisaa_seuraava...")

for i in range(3):
    aak = aakkoset[:random.randint(3, len(aakkoset) - 2)]
    print(f"Kutsutaan lisaa_seuraava(\"{aak}\")")
    val = lisaa_seuraava(aak)
    if val:
        print("Funktio palauttaa:", val)
    else:
        print("Funktio ei palauta mitään.")
        
print("")
print("Testataan funktiota lisaa_monta...")

for i in range(3):
    aak = aakkoset[:random.randint(2, len(aakkoset) - 6)]
    lis = random.randint(2, 5)
    print(f"Kutsutaan lisaa_monta(\"{aak}\", {lis})")
    val = lisaa_monta(aak, lis)
    if val:
        print("Funktio palauttaa:", val)
    else:
        print("Funktio ei palauta mitään.")