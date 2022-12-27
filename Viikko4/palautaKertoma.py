import random
#Luvun kertoma luku! on luku kerrottuna kaikilla itseään pienemmillä positiivisilla kokonaisluvuilla.

# Niinpä esimerkiksi luvun 5 kertoma 5! on lausekkeen 5 * 4 * 3 * 2 * 1 lopputulos.



def kertoma(n: int):
    faktoriaali = 1
    if n >= 1:
        for i in range (1, n +1):
            faktoriaali = faktoriaali * i
        return(faktoriaali)
       

inputs = [1,2,3,4,5,6,7,8,9,10]
random.shuffle(inputs)

for i in range(5):
    n = inputs.pop()
    print(f"Kutsutaan kertoma({n})...")
    val = kertoma(n)
    if val:
        print("Funktio palauttaa:", kertoma(n))
    else:
        print("Funktio ei palauta mitään!")