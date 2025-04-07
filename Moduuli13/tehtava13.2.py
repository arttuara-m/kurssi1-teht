from flask import Flask
import mysql.connector

app = Flask(__name__)
@app.route('/kentta/<icao>')
def kentta(icao):
    return lentoaseman_loytaja(icao)

def lentoaseman_loytaja(icao):
    sql = f"SELECT id, name, municipality FROM airport WHERE ident ='{icao}'"

    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchone()

    kenttatieto = {
        "ICAO": tulos[0],
        "Name": tulos[1],
        "Municipality": tulos[2]
    }

    return kenttatieto

#[('Helsinki Vantaa Airport', 'Helsinki')]

yhteys = mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        database='flight_game',
        user='python',
        password='isbad',
        autocommit=True
    )

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)

#print(lentoaseman_loytaja("EFHK"))

#http://127.0.0.1:3000/kentta/EFHK
#{"ICAO":"EFHK", "Name":"Helsinki Vantaa Airport", "Municipality":"Helsinki"}