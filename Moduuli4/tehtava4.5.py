
kauttaja = "Python"
salasana = "rules"
yritykset = 0

while yritykset < 5:
    kyritys = input("Syötä käyttäjänimi: ")
    syritys = input("Syötä salasana: ")

    if kyritys == kauttaja and syritys == salasana:
        break

    yritykset+=1

if yritykset < 5:
    print("Tervetuloa")
else:
    print("Pääsy evätty")