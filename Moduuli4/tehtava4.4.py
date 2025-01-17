import random

oikea = random.randint(1,10)
arvaus = 0

while arvaus != oikea:
    arvaus = int(input("Syötä luku yhdestä kymmeneen: "))
    if arvaus < oikea:
        print("Liian pieni")
    elif arvaus > oikea:
        print("Liian suuri")
    else:
        print("Oikein")