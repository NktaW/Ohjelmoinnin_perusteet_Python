import random

#Kirjoita ohjelma, joka kysyy käyttäjältä tämän nimen ja syntymävuoden, ja tulostaa sitten alla olevan esimerkkitulosteen mukaisen tervehdyksen ja tiedon käyttäjän iästä vuoden 2021 lopussa.
#Huomaa, että tulosteiden pitää olla täsmälleen vastaavat kuin esimerkissä:

#Anna nimesi: Mari
#Anna syntymavuosi: 2013
#Moi, Mari!
#Olet 8 vuotta vanha vuoden 2021 lopussa.


nimi = input("Anna nimesi: ")
syntymavuosi = int(input("Anna syntymavuosi: "))
summa = 2022 - syntymavuosi
print("Moi, " + nimi+"!")
print("Olet ", summa, " vuotta vanha vuoden 2022 lopussa.")