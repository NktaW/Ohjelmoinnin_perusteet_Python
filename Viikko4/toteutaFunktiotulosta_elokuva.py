import random

#Toteuta edellisessä tehtävässä määritelty funkto tulosta_elokuva niin, että se tulostaa annetun elokuvan tiedot. Muista tyyppivihjeet!

#Katso esimerkkiä seuraavasta kahdesta esimerkkikutsusta:

#tulosta_elokuva("E.T.", "Steven Spielberg", 115.0, 7, False)

#Ohjelma tulostaa:
"""
Elokuvasuositus: E.T., jonka ohjasi maineikas Steven Spielberg.
Elokuva kestää 115.00 minuuttia, ja sen ikäraja on 7.
Elokuva ei ole tällä hetkellä ohjelmistossa.

"""

def tulosta_elokuva(nimi: str, ohjaaja: str, kesto: float, ikaraja: int, ohjelmistossa: bool):  
    print(f'Elokuvasuositus: {nimi}, jonka ohjasi maineikas {ohjaaja}.')
    print(f'Elokuva kestää {kesto:.2f} minuuttia, ja sen ikäraja on {ikaraja}.')
    if ohjelmistossa == False:
        print(f'Elokuva ei ole tällä hetkellä ohjelmistossa.')
    else:
        print(f'Elokuva on tällä hetkellä ohjelmistossa.')

tulosta_elokuva("E.T.", "Steven Spielberg", 115.0, 7, False)

tulosta_elokuva("E.T. 2", "Senior Spielbergo", 97.25, 18, True)