#Kivi, paperi ja sakset on peli, jossa molemmat pelaajat valitsevat yhden kolmesta pelin nimen mukaisesta vaihtoehdosta. Voittaja määräytyy seuraavien sääntöjen mukaan:
'''
Kivi voittaa sakset
Sakset voittaa paperin
Paperi voittaa kiven

'''
#Jos molemmat valitsevat saman valinnan, kyseessä on tasapeli.

#Kirjoita ohjelma, joka kysyy molempien pelaajien valinnnan yksitellen. Voittaja saa aina erävoitosta pisteen. Tasapelin sattuessa kumpikaan ei saa pistettä.

#Kun ykköspelaajan valinnaksi annetaan tyhjä merkkijono, ohjelma tulostaa lopullisen pistetilanteen ja päättyy.

p1pisteet = 0
p2pisteet = 0

while True:
    p1valinta = input("Pelaaja 1 valinta: ")
    
    if p1valinta == '':
        print('Peli päättyi')
        break

    p2valinta = input("Pelaaja 2 valinta: ")

    if p1valinta == p2valinta:
        print('Tasapeli')
    else:

        if p1valinta == 'kivi' and p2valinta == 'sakset':
            print('Pelaaja 1 voitti')
            p1pisteet += 1
        elif p1valinta == 'paperi' and p2valinta == 'kivi':
            print('Pelaaja 1 voitti')
            p1pisteet += 1
        elif p1valinta == 'sakset' and p2valinta == 'paperi':
            print('Pelaaja 1 voitti')
            p1pisteet += 1

        elif p2valinta == 'kivi' and p1valinta == 'sakset':
            print('Pelaaja 2 voitti')
            p2pisteet += 1
        elif p2valinta == 'paperi' and p1valinta == 'kivi':
            print('Pelaaja 2 voitti')
            p2pisteet += 1
        elif p2valinta == 'sakset' and p1valinta == 'paperi':
            print('Pelaaja 2 voitti')
            p2pisteet += 1

print(f'Pelaaja 1 sai {p1pisteet} pistettä')
print(f'Pelaaja 2 sai {p2pisteet} pistettä')