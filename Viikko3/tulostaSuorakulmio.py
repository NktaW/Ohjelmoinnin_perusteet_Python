#Kirjoita ohjelma, joka kysyy käyttäjältä leveyden ja korkeuden,
#ja tulostaa sitten asteriskeista koostuvan suorakulmion alta löytyvän esimerkin mukaisesti.

#Vinkki: muista, että merkin kertominen kokonaisluvulla tuottaa uuden merkkijonon
#  - esim. "X" * 5 == "XXXXX". 

leveys = int(input("Anna leveys: "))
korkeus = int(input("Anna korkeus: "))

i = 0 
rivi = leveys * '*'


while i < korkeus:
    i +=1
    print(rivi)