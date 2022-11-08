import random

#Kirjoita ohjelma, joka kysyy lipun hinnan ja käyttäjän iän.

#Jos käyttäjä on ...

#Alle 12-vuotias, hän saa lipun puoleen hintaan.
#Yli 63-vuotias, hän saa lipun neljäsosahinnalla.

#Kaikki muut käyttäjät saavat lipusta 5 prosenttia alennusta ihan muuten vaan. 

lipunHinta = int(input("Anna lipunt hinta: "))
ika = int(input("Anna ikä: "))

if ika <= 12:
    print("Hinnaksi tuli", lipunHinta * 0.5, "euroa.")
elif ika >= 63:
    print("Hinnaksi tuli", lipunHinta * 0.25, "euroa.")
else:
     print("Hinnaksi tuli", lipunHinta * 0.95, "euroa.")
