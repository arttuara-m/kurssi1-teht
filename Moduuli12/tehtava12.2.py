import requests

appid = "placeholder"
paikkakunta = input("Syötä haluttu paikkakunta suomeksi: ")
pyynto = f"https://api.openweathermap.org/data/2.5/weather?q={paikkakunta}&appid={appid}&units=metric&lang=fi"
vastaus = requests.get(pyynto).json()
print(f'{vastaus["weather"][0]["description"]}')
print(f'{vastaus["main"]["temp"]}C')

#Jos haluat testata, laita oma API-avain placeholderin tilalle.