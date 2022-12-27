import random

#Kirjoita funktio suurin_luku, joka saa parametrikseen kolme kokonaislukua.

#Funktio tulostaa luvuista suurimman alla olevan esimerkkisuorituksen mukaisesti.

"""
Esimerkki funktion kutsusta:

suurin_luku(50, 67, 13)
Suurin luku on 67

"""
"""
def suurin_luku(luku1, luku2, luku3):
    if luku1 > luku2 and luku1 > luku3:
        return print(f'Suurin luku on {luku1}')
    elif luku2 > luku1 and luku2 > luku3:
        return print(f'Suurin luku on {luku2}')
    else:
        return print(f'Suurin luku on {luku3}')



"""

def suurin_luku(a, b, c):
    luvut = []
    luvut.append(a)
    luvut.append(b)
    luvut.append(c)
    for i in luvut:
        i = max(luvut)
    print(i)

jtn = suurin_luku(4,5,7)

print(jtn)


print("Testataan funktiota suurin_luku")

for i in range(5):
    n1 = random.randint(-100, 100)
    n2 = n1 + random.randint(1, 100)
    n3 = n2 + random.randint(1, 100)
    
    par = [n1,n2,n3]
    random.shuffle(par)
    
    print(f"Kutsutaan suurin_luku({par[0]}, {par[1]}, {par[2]})...")
    suurin_luku(par[0], par[1], par[2])