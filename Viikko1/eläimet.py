import random
#Kirjoita ohjelma, joka pyytää käyttäjää syöttämään eläimen. Jos käyttäjä syöttää tietyn neljästä eläimestä, ohjelma kertoo mitä eläin sanoo...

#Eläimet ja äännähdykset ovat:

#koira: Hau!
#kissa: Miau!
#lehmä: Muu!
#lammas: Bää!

#Jos käyttäjä antaa jonkin muun eläimen, ohjelma ei tulosta mitään.

syotaElain = input("Syötä eläin.")

if syotaElain == "koira":
    print("Hau!")
if syotaElain == "kissa":
    print("Miau!")
if syotaElain == "lehmä":
    print("Muu!")
if syotaElain == "lammas":
    print("Bää!")