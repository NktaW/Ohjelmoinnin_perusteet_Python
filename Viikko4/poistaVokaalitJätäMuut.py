import random

#Kitjoita funktio poista_vokaalit(sana: str)

#...joka saa parametrikseen merkkijonon. Funktio palauttaa uuden merkkijonon, jossa alkuperäisestä jonosta on poistettu kaikki vokaalit (aeiouyåäö).

def poista_vokaalit(sana: str):
    for i in 'aeiouyåäö':
        sana = sana.replace(i,'')
    return sana
    


testit = "karhu kettu kani norsu elefantti hedelmäkori asetyylisalisyylihappo"
testit += "kirahvi algebra rämälämädingdong abrakadabra megawatti bananasplit"
tlista = testit.split()

random.shuffle(tlista)

for i in range(5):
    sana = tlista.pop()
    print(f"Kutsutaan poista_vokaalit({sana})...")
    
    tulos = poista_vokaalit(sana)
    if tulos:
        print("Funktio palautti sanan", tulos)
    else:
        print("Funktio ei palauttanut mitään!")