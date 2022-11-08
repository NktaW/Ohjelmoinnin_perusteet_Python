luku1 = int(input("Anna eka luku: "))
luku2 = int(input("Anna toka luku: "))
luvut = luku1 + luku2
if luvut % 2 == 0:
    print("Koodi on",luvut * 10)
elif luvut % 2 !=0:
    print("Koodi on: ", luvut * 5)