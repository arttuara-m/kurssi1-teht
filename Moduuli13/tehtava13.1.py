from flask import Flask

def alkuluvuttaja(luku):
    luku = luku

    if luku == 1:
        return False

    for i in range(2, luku-1):
        if luku % i == 0:
            return False
    return True

app = Flask(__name__)
@app.route('/alkuluku/<halluku>')
def alkuluku(halluku):
    luku = int(halluku)
    isprime = alkuluvuttaja(luku)

    vastaus = {
        "luku": luku,
        "isprime" : isprime
    }

    return vastaus

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)

#http://127.0.0.1:3000/alkuluku/31