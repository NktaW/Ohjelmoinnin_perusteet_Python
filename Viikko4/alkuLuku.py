from math import sqrt
import random

#Alkuluvuilla on tärkeä rooli tietojen ja kommunikaation salaamisessa. Tämän takia tarvitaan tehokkaita algoritmeja alkulukujen löytämiseen.

#Alkuluvulla tarkoitetaan sellaista lukuja, jonka ainoa jakajat ovat 1 ja luku itse.

#Kirjoita funktio onko_alkuluku joka saa parametrina positiivisen kokonaisluvun. Jos luku on alkuluku, funktio palauttaa True. Jos luku ei ole alkuluku, funktio palauttaa False.

#Tehokkuudella ei ole merkitystä, sillä suurten alkulukujen etsiminen olisi vaikeaa (mihin koko modernien salausalgoritmi turvallisuus perustuu).  
#Riittää siis, että ohjelma toimii nopeasti pienillä luvuilla (< 10 000 000).

def onko_alkuluku(luku):
    if luku <= 1:
        return False
    
    jakaja = 2

    while jakaja < luku:
        #print('Testataan jakaajaa', jakaja)
        if luku % jakaja == 0:
            return False
        
        jakaja += 1
    return True

#print(onko_alkuluku(10))

print("testataan peruslukuja..")
a = [i for i in range(30)]
random.shuffle(a)
for i in a:
    result = onko_alkuluku(i)
    print(f"Luku {i} {'on' if result else 'EI OLE'} alkuluku")
    
x = [random.randint(1000,5000) for i in range(10)]
print("Testataan isompia lukuja")
for i in x:
    result = onko_alkuluku(i)
    print(f"Luku {i} {'on' if result else 'EI OLE'} alkuluku")