import random

#Kirjoita ohjelma, joka tulostaa viestin "Moi!" ja kysyy sitten käyttäjältä jatketaanko.
#Jos käyttäjä vastaa "k", ohjelma tulostaa uuden moikkauksen ja kysyy taas jatkamisesta.

#Jos käyttäjä vastaa "k", ohjelma tulostaa uuden moikkauksen ja kysyy taas jatkamisesta.



while True:
    print("Moi!")
    toistetaanko = input("Toistetaanko k/e: ")
    if toistetaanko == "e":
        break