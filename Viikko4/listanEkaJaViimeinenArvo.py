import random


for toisto in range(3):
    lista = [random.randint(1,100) for x in range(random.randint(6,20))]
    
    print("Lista ennen:", lista)

"""
Ohjelmassa on alustettu kokonaistyyppisiä arvoja sisältävä lista satunnaisilla arvoilla.

Muuttujaan lista on tallennettu viittaus listaan.

Tehtäväsi on vaihtaa keskenään listan ensimmäinen ja viimeinen arvo.

Jos lista olisi siis ennen vaihtoa tällainen:

[1, 2, 3, 4]

..näyttäisi se vaihdon jälkeen tältä:

[4, 2, 3, 1]

"""

lista[0], lista[-1] = lista[-1], lista[0]

    


print("Lista jälkeen:", lista)
print("")