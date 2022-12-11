import random
#Kirjoita funktio salakirjoita(teksti), joka saa parametrikseen merkkijonon. Funktio palauttaa salakirjoitetun tekstin.

#Salakirjoitukseen käytetään (nykymittapuulla täysin kelvotonta) ROT-13 algoritmia,
#jonka idea on, että jokainen englanninkielen aakkosten (a - z) kirjain korvataan 13 askelta pidemmällä aakkosissa olevalla kirjaimella.
# Jos 13 askelta on yli viimeisen kirjaimen (eli kirjaimen "z"), askellus jatkuu aakkosten alusta.

#Niinpä esim. kirjain "a" korvattaisiin kirjaimella "n", kirjain "d" kirjaimella "q" ja kirjain "r" kirjaimella "e".
#Koska algoritmi toimii molempiin suuntiin, korvataan vastavasti kirjain "n" kirjaimella "a", kirjain "q" kirjaimella "d" jne.

#Niin kuin sanottu, algoritmi tunnistaa vain englanninkielen aaakkoset a...z. Lisäksi riittää, että salakirjoitus toimii vain pienillä kirjaimilla. 


#Minun koodi alkaa

def salakirjoita(teksti):
   aakkoset = "abcdefghijklmnopqrstuvwxyz"
   i = 0
   salaus = ''
   while i < len(teksti):
        numerojarjestys = aakkoset.find(teksti[i])
        if numerojarjestys + 13 < len(aakkoset):
                lisaysindeksi = numerojarjestys +13
                salaus += aakkoset[lisaysindeksi]
        else:
                lisaysindeksi = numerojarjestys + 13 - len(aakkoset)
                salaus += aakkoset[lisaysindeksi]

        i += 1
   return salaus
#koodi loppuu      

sanat = "hiiri kissa koira lammas auto mopo motskari python java kello kallo suomi ruotsi norja tanska islanti".split()
sanat += "uvvev xvffn xbven ynzznf nhgb zbcb zbgfxnev clguba wnin xryyb xnyyb fhbzv ehbgfv abewn gnafxn vfynagv".split()
random.shuffle(sanat)
sanat = sanat[0:4]

print("Testataan funktiota salakirjoita....")

for sana in sanat:
    print(f'Kutsutaan salakirjoita("{sana}")')
    salattu = salakirjoita(sana)
    print(salattu)
    print("")