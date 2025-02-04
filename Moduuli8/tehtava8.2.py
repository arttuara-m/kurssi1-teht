import mysql.connector

def lentoasemien_laskija(maakoodi):
    sql = f"SELECT type, count(*) FROM airport WHERE iso_country ='{maakoodi}' GROUP BY type"

    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()

    if kursori.rowcount >0 :
        for rivi in tulos:
            print(f"{rivi[0]}   {rivi[1]}")

    return

yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='python',
         password='isbad',
         autocommit=True
         )

syote = input("Syötä maakoodi: ")
lentoasemien_laskija(syote)

