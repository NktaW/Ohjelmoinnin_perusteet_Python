import random

#Kirjoita ohjelma, joka kysyy käyttäjältä vuosiluvun. Ohjelma kertoo sen jälkeen, onko vuosi karkausvuosi.

#Vuosi on karkausvuosi, jos se on jaollinen neljällä.
#Sadalla jaollisista vuosista karkausvuosia ovat kuitenkin vain ne, jotka ovat jaollisia myös 400:lla.

vuosi = int(input("Anna vuosi: "))

if vuosi % 400 == 0 and vuosi % 100 == 0 :
    print("On karkausvuosi")
elif vuosi % 4 == 0 and vuosi % 100 != 0:
    print("On karkausvuosi")
else:
    print("Ei ole karkausvuosi")