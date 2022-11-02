import random

#Kirjoita ohjelma, joka kysyy käyttäjältä erikseen etu- ja sukunimen.
#Jos käyttäjän koko nimi on Erno Esimerkki, ohjelma tulostaa viestin "Ernohan se siellä!". Muuten ei tehdä mitään.

nimi = input("Anna etunimi: ")
sukunimi = input("Anna sukunimi: ")
if nimi == "Erno":
    if sukunimi == "Esimerkki":
        print("Ernohan se siellä!")