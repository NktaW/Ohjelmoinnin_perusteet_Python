import random

#Alusta muuttuja veljekset, joka osoittaa merkkijonoja sisältävään listaan.

#Listan sisältönä ovat Aleksis Kiven seitsemän veljeksen veljekset, kukin omana alkionaan.

#Muistin virkistämiseksi: veljeksethän olivat

veljekset = ['Aapo', 'Eero', 'Juhani', 'Lauri', 'Simeoni', 'Timo', 'Tuomas']


print("Listassa veljekset on seuraavat alkiot aakkosjärjestyksessä: ")

for veljes in sorted(veljekset):
    print(veljes)