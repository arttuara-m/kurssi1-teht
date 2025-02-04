import mysql.connector

def lentoaseman_loytaja(icao):
    sql = f"SELECT name, municipality FROM airport WHERE ident ='{icao}'"

    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()

    return tulos

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='python',
         password='isbad',
         autocommit=True
         )

syote = input("Syötä ICAO-koodi: ")
printattava = lentoaseman_loytaja(syote)
print(printattava)
