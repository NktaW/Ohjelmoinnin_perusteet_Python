import random

#Kirjoita kaksi funktiota:

#puoleen_hintaan(hinta)
#tulosta_tarjous(hinta)

#Funktio puolita_hinta  saa parametrikseen hinnan kokonaislukuna ja palauttaa hinnan josta on laskettu 50% alennus.

#Funktio tulosta_tarjous saa parametrina hinnan ja tulostaa tarjouksen alla näkyvässä muodossa.

#Oma koodi alkaa tästä...
def puolita_hinta(hinta):
    hinta = hinta * 0.5
    return hinta

def tulosta_tarjous(hinta):
    print(f"Tuotteen tarjoushinta on {hinta:.2f} €")
    return puolet
#Oma koodi loppuu tähän.

print("Testataan funktiota puoleen_hintaan...")

hinnat = "7 101 49 37 21 15".split()
random.shuffle(hinnat)
hinnat = [int(x) for x in hinnat[:3]]

for hinta in hinnat:
    print(f"Kutsutaan puoleen_hintaan({hinta})...")
    puolet = puolita_hinta(hinta)
    print(f"Alunperin hinta oli {hinta} €")
    tulosta_tarjous(puolet)
    



