import random
#Kirjoita funktio tulosta_hlo seuraavien sääntöjen mukaisesti:

# 1) Funktiolla on neljä muodollista parametria.

# 2) Parametrit saavat arvoikseen tässä järjestyksessä.
#   merkkijonoina nimen, osoitteen, puhellinnumeron ja sähköpostiosoitteen

# 3) Funktio tulostaa todelliset parametrien arvot allekkain muodollisia parametreja vastaavassa järjestyksessä

# 4) Funktio ei tulosta muuta kuin todellisten parametrien arvot.

def tulosta_hlo(nimi, osoite, puhelinNro, sposti):
    print(f'{nimi}\n{osoite}\n{puhelinNro}\n{sposti}')




n = "Jarmo Jaana Pirjo Pekka Kai Karoliina Leena Lasse Mikko Maija Outi Olli".split()
o = "Java Python Ohjelmointi Parametri Muuttuja Silmukka Ehto".split()
o2 = "tie katu kuja polku ranta".split()

print("Kutsutaan funktiota tulosta_hlo...")

for i in range(3):
    ni = random.choice(n)
    os = random.choice(o) + random.choice(o2) + " " + str(random.randint(1,50))
    pn = str(random.randint(100,999)) + "-" + str(random.randint(1000000,9999999))
    sp = ni.lower() + "@example.com"
    
    tulosta_hlo(ni, os, pn, sp)
    
    print("")