#Kirjoita ohjelma, joka kysyy käyttäjältä alku- ja loppupisteen, 
#ja laskee sitten tälle välille [alku, loppu] sijoittuvien lukujen summan.

summa = 0

alku = int(input("Anna alku: "))
loppu = int(input("Anna loppu: "))

summa = 0
while loppu >= alku:
    summa += alku
    #print(summa)
    alku +=1    
print('Summa on', summa)
 
 #Toinen tapa ilman silmukkaa, käyttämällä python funktioita...
 #print("Summa on", sum(range(alku,loppu+1)))