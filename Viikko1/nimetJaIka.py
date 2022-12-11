import random


rc = random.choice

etunimet = "Pekka Pirjo Paula Arto Kimmo Liisa Maija Lasse Leena".split()
sukunimet = "Virtanen Lahtinen Hakanen Järvinen Jokinen Saarinen".split()

etunimi = rc(etunimet)
sukunimi = rc(sukunimet)
ika = random.randint(10,99)

#Ohjelmassa on alustettu kolme muuttujaa satunnaisilla alkuarvoilla: 
#etunimi (merkkijono)
#sukunimi (merkkijono) ja
#ika (kokonaisluku)

#Tehtäväsi on tulostaa alla olevan esimerkin mukainen viesti muuttujia hyödyntäen. Huomaa, että tulostuksen tulee noudattaa esimerkkitulostusta täsmälleen.

print("Moi, nimeni on", etunimi, sukunimi, "ja olen", ika, "vuotta vanha.")