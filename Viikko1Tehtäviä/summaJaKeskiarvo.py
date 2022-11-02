import random


eka = random.randint(1,10)
toka = random.randint(1,20)
kolmas = random.randint(1,30)

print("Luvut ovat:")
print("Eka:", eka)
print("Toka:", toka)
print("Kolmas:", kolmas)

#Ohjelmassa on alustettu valmiiksi kolme kokonaislukutyyppistä muuttujaa, eka, toka ja kolmas. Kaikilla muuttujilla on siis valmiiksi jokin arvo.
#Tehtäväsi on laskea ja tulostaa lukujen summa ja keskiarvo alla olevan esimerkin mukaisesti. Jos luvut olisivat 7, 3 ja 5, ohjelmasi tulostaisi:
#Summa: 15
#Keskiarvo: 5.0

print("Summa:", eka + toka + kolmas)
print("Keskiarvo:", (eka + toka + kolmas) / 3)