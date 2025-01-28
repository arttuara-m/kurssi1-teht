import math

def pitsamittari(halkaisija, hinta):
    hintanelioina = hinta / (halkaisija * math.pi / 100)
    return hintanelioina

halkaisija1 = float(input("Syötä ensimmäisen pitsan halkaisija senttimetreinä: "))
hinta1 = float(input("Syötä ensimmäisen pitsan hinta euroina: "))
halkaisija2 = float(input("Syötä toisen pitsan halkaisija senttimetreinä: "))
hinta2 = float(input("Syötä toisen pitsan hinta euroina: "))

if pitsamittari(halkaisija1,hinta1) < pitsamittari(halkaisija2,hinta2):
    print("Ensimmäinen pitsa antaa paremman vastineen rahalle.")
elif pitsamittari(halkaisija2,hinta2) < pitsamittari(halkaisija1,hinta1):
    print("Toinen pitsa antaa paremman vastineen rahalle.")
else:
    print("Pitsojen hinta per neliömetri on täsmälleen sama!")