vuosi = int(input("Syötä vuosi: "))

if vuosi % 4 == 0:
    if vuosi % 100 == 0:
        if vuosi % 400 == 0:
            print("on")
        else:
            print("ei")
    else:
        print("on")
else:
    print("ei")
