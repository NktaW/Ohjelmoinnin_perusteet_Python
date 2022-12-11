#Muuta edellisen tehtävän ratkaisua siten, että ohjelma tulostaa nyt asteriskeista vain neliön "ääriviivat" alta löytyvän esimerkin mukaisesti.

#Voit olettaa, että leveys ja korkeus ovat molemmat vähintään 4.

#Vinkki: muista, että merkin kertominen kokonaisluvulla tuottaa uuden merkkijonon - esim. "X" * 5 == "XXXXX". 

leveys = int(input("Anna leveys: "))
korkeus = int(input("Anna korkeus: "))

muutettuRivi = 1 * '*' + (leveys -2) * ' ' + 1 * '*'

i = 0 
rivi = leveys * '*'

print(rivi)

while i < korkeus - 2:
    print(muutettuRivi)
    i +=1
print(rivi)