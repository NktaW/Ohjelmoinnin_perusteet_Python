""""
#muuttuja nimeltä nimi, jonka arvo on merkkijono "Pekka ptyhon"
nimi = "Pekka Python"

#Muuttuja ideksimerkki joka saa arvokseen nimi muuttujasta merkkijonon viimeisen merkin
indeksinMerkki = nimi[-12]

#print komennolla tulosettaan indeksimerkin arvo, joka on nimi muuttujan merkkijonon viimeinen merkki eli täs tapaukses tulostuu P
print("Ensimmäinen merkki:", indeksinMerkki)

#Toinen tapa tulostaa merkki jono syöttämällä se suoraan print komentoon...

print("Viimeinen merkki jono:", nimi[len(nimi) -1])

"""

""""
nimi = "Pirjo"

indeksi = 0

while indeksi < len(nimi):
    osa_nimesta = nimi[indeksi: indeksi + 3]
    print(osa_nimesta)

    indeksi += 1

-------------------------------
nimi = "Pirjo"

print(nimi.find("jo"))

"""

"""

luku = int(input("Mikä kertotaulu? "))

print(f"1 kertaa {luku} on {luku * 1}.")
print(f"2 kertaa {luku} on {luku * 2}.")
print(f"3 kertaa {luku} on {luku * 3}.")
print(f"4 kertaa {luku} on {luku * 4}.")
print(f"5 kertaa {luku} on {luku * 5}.")
print(f"6 kertaa {luku} on {luku * 6}.")
print(f"7 kertaa {luku} on {luku * 7}.")
print(f"8 kertaa {luku} on {luku * 8}.")
print(f"9 kertaa {luku} on {luku * 9}.")
print(f"10 kertaa {luku} on {luku * 10}.")

"""
luku = 5


def neliö(luku):
    vastaus = luku * luku
    return vastaus

n = neliö(luku)

print(n)