import random

#Rakenna ohjelma, joka tulostaa tiedon siitä, onko muuttujaan luku tallennettu luku alle, yli vai tasan sata.


luku = int(input("Anna luku: "))

if luku == 100:
    print("Tasan sata")
elif luku < 100:
    print("Alle sata")
else:
    print("Yli sata")