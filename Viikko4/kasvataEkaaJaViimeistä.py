import random


for toisto in range(3):
    lista = [random.randint(1,100) for x in range(random.randint(6,20))]
    
    print("Lista ennen:", lista)
    

#Ohjelmassa on alustettu kokonaistyyppisiä arvoja sisältävä lista satunnaisilla arvoilla.

#Muuttujaan lista on tallennettu viittaus listaan.

#Tehtäväsi on kasvattaa listan ensimmäistä ja viimeistä arvoa molempia yhdellä.


lista[0] = lista[0] +1
lista[-1] = lista[-1] +1






print("Lista jälkeen:", lista)
print("")