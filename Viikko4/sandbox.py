"""

Oletetaan, että on määritelty seuraavat funktiot (funktioiden toteutuksia ei tässä yhteydessä anneta):

def rekisteroi(kurssi, opiskelija, op, vuosi)
def suorita(kurssi, opiskelija, arvosana)
 

Funktioita kutsutaan seuraavasti:

rekisteroi("TKT_1234", "Jussi", 5, 1)
suorita("TKT_4321", "Jussi", 3,)

"""
"""
#Tarkastele alla olevaa ohjelmakoodia ja valitse sitten jokaiselle muuttujalle oikea näkyvyys ohjelman eri osissa.

def tulosta1(nimi):
    print(nimi)

def tulosta2(osoite):
    global n
    n = "nimi:" + n
    print(n, " - ", osoite)

n = "Mikko Mallikas"
ika = 45
os = "Keksittykatu 12"

"""
#Tarkastele alla olevia funktomäärittelyjä. Kirjoita sitten jokaisen funktiokutsun kohdalle joko

#arvo, joka tulostetaan kun funktiota kutsutaan annetuilla parametreilla TAI
#sana virhe, jos funktiokutsu annetuilla parametreilla johtaa virheeseen.
#Ohjelmakoodi:
"""
def eka(a, b):
    print(a + b)

def toka(a, b):
    print(a - b)

def kolmas(a, b):
    print(a * b)

kolmas('ab','cd')
print("TÄMÄ OLI ENSIMMÄINEN")

"""
n = int(input('Anna n: '))
luku = n - 1

a = []

i = 1
for i in range(luku):
    kerrotaan = n * (luku - i)
    kerrotaan *= i
    i += 1


    print(kerrotaan)