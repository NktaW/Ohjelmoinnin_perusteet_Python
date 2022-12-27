import random
#Kirjoita funktio sijoita(lause, nimi, ammatti), joka saa parametrikseen lauseen, nimen ja ammatin. Kaikki parametrit ovat merkkijonoja.

#Funktio sijoittaa annetun nimen ja ammatin lauseeseen. Nimi korvaa lauseessa merkkijonon "nimi" ja ammatti merkkijonon "ammatti".



def sijoita(lause, nimi, ammatti):
    lause = lause.replace('nimi', nimi)
    lause = lause.replace('ammatti', ammatti)
    print(lause)





nimet = "Jarmo Jaakko Jaana Janita Lasse Liisa Matti Maija Pekka Paula Pirjo Pertti".split()
amm = "myyjä opettaja rehtori poliisi pelastaja asiantuntija lehmipaimen kalastaja".split()
random.shuffle(nimet)
random.shuffle(amm)


l1 = "Moi, nimeni on nimi ja olen ammatiltani ammatti."
l2 = "Hei vaan, olen nimi ja työnäni on ammatti."
l3 = "Terve! Minä olen nimi. Mitä teen työkseni? Olen ammatti."

print("Testataan funktiota sijoita(lause, nimi, ammatti)...")

for lause in (l1,l2,l3):
    nimi = nimet.pop()
    ammatti = amm.pop()
    print("Lause:", lause)
    print("Nimi:", nimi)
    print("Ammatti:", ammatti)
    sijoita(lause, nimi, ammatti)