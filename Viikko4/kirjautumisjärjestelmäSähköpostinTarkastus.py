import random

"""
Totetutetaan muutama funktio, joiden avulla voidaan rakentaa yksinkertainen kirjautumisjärjestelmä.

Kirjoita funktio 

sposti_ok(sposti: str)

...jonka avulla voidaan tarkastaa, onko annettu sähköposti oikean muotoinen. Funktio palauttaa True, jos seuraavat ehdot täyttyvät:

Osoitteesta löytyy tasan yksi @-merkki
@-merkin jälkeisestä osuudesta löytyy vähintään yksi piste ja osuuden pituus on vähintään 3 merkkiä
@-merkkiä edeltävän osuuden pituus on vähintään yksi merkki
Jos ehdot eivät täyty, funktio palauttaa arvon False.

"""
def sposti_ok(sposti: str):
    merkki = ""
    at = []
    i = ""
    if ("@" in sposti):
        at = sposti.find("@")

        if at == 1:

            if ("." in sposti):
                piste = sposti.find(".")
                sposti.split('@')

                if (len(sposti[1]) >= 3):

                    if (len(sposti[0]) >= 1):

                        return True
    else:
        return False


testit = "eka@example.com eka@example @example.com eka@ab testi@testi.com ekaexample.com eka@toka@kolmas.com".split()
random.shuffle(testit)

print("Testataan funktiota sposti_ok(sposti: str)...")

for testi in testit:
    print(f"Testataan kutsulla sposti_ok(\"{testi}\")")
    print(f"Funktio palauttaa: {sposti_ok(testi)}")