import random 

#Kirjoita ohjelma, joka kysyy käyttäjältä huudahduksen. Jos huudahdus on "Hiiohoi", sen perään lisätään kolme huutomerkkiä. 

#Lopuksi huudahdus tulostetaan alla olevien esimerkkitulostusten mukaisesti riippumatta siitä, mikä huudahdus oli.

#Anna huudahdus: Hiiohoi
#Huuto oli Hiiohoi!!!

#Anna huudahdus: Jippii

huudahdus = input("Anna huudahdus: ")
if huudahdus == "Hiiohoi":
    print("Huuto oli",huudahdus +"!!!")
else:
    print("Huuto oli",huudahdus)