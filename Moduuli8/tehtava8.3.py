from geopy import distance
import mysql.connector

def tiedon_hakija(ident):
    sql = f"SELECT latitude_deg, longitude_deg FROM airport WHERE ident ='{ident}'"

    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchone()

    return tulos[0], tulos[1]

def etaisyyden_mittaaja(ident1, ident2):
    return distance.distance(ident1, ident2).kilometers


#luodaan yhteys
yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='python',
         password='isbad',
         autocommit=True
         )

icao1 = input("Syötä ensimmäisen lentokentän ICAO-koodi: ")
icao2 = input("Syötä toisen lentokentän ICAO-koodi: ")

sijainti1 = tiedon_hakija(icao1)
sijainti2 = tiedon_hakija(icao2)

print(round(etaisyyden_mittaaja(sijainti1, sijainti2), 1))
