# Kirjoita kolme funktiota: summa, erotus ja tulo

#Jokainen funktioista saa parametrikseen kaksi kokonaislukua ja palauttaa nimensä mukaisen laskutoimituksen tuloksen.

def summa(a: int, b: int):
    summa = a + b
    return summa

print(summa(1, 2))

def tulo(a: int, b: int):
    tulo = a * b
    return tulo

print(tulo(2,2))

def erotus(a: int, b: int):
    erotus = a - b
    return erotus

print(erotus(10,3))