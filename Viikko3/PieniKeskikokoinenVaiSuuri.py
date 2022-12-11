#Ohjelmassa on valmiiksi määritelty kolme funktiota:
"""
tulosta_pieni()
tulosta_keski()
tulosta_suuri()
"""
#Täydennä ohjelma kysymällä käyttäjältä, minkä kokoisen laatikon hän haluaa tulostaa. Kutsu sitten oikeaa funktiota sen mukaisesti.

def tulosta_pieni():
    print("Pieni laatikko")
def tulosta_keski():
    print("Keskikoko laatikko")
def tulosta_suuri():
    print("Suuri laatikko")


mikaLaatikko = input("Mikä koko? ")

if mikaLaatikko == 'pieni':
    tulosta_pieni()
elif mikaLaatikko == 'keskikoko':
    tulosta_keski()
elif mikaLaatikko == 'suuri':
    tulosta_suuri()
