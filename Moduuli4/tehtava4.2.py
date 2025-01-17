while True:
    tuuma = float(input("Syötä senttimetreiksi käännettävä tuumamäärä: "))
    if tuuma < 0:
        break
    print(str(tuuma * 2.54) + " cm")