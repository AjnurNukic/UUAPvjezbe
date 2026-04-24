import pandas as pd

# Učitavanje podataka
izvjestaj = pd.read_csv("policijski_izvjestaj.csv")
osumnjiceni = pd.read_csv("osumnjiceni.csv")
kartice = pd.read_csv("pristupne_kartice.csv")
svjedoci = pd.read_csv("izjave_svjedoka.csv")

# Ispis osnovnih informacija
print(f"Osumnjičenih: {len(osumnjiceni)} ")
print(f"Izvještaja u bazi: {len(izvjestaj)}")
print(f"Zabilježenih pristupa karticama: {len(kartice)}")
print(f"Izjava svjedoka: {len(svjedoci)}")

# Filtriranje izvještaja za ubistvo
ubistvo = izvjestaj[izvjestaj["tip"] == "ubistvo"]
print("\n--- Detalji zločina ---")
print(ubistvo[["datum", "vrijeme", "lokacija", "opis"]])

# ANALIZA KRETANJA (Tech Hub, 15. mart)
tech_hub_15 = kartice[(kartice["zgrada"] == "Tech Hub") & (kartice["datum"] == "2026-03-15")]

# Filtriranje osoba u zgradi tokom ubistva (19:30 - 20:30)
prisutni_u_vrijeme_zlocina = tech_hub_15[
    (tech_hub_15["vrijeme_ulaza"] < "20:30") &
    ((tech_hub_15["vrijeme_izlaza"] > "19:30") | (tech_hub_15["vrijeme_izlaza"].isna()))
]

# Spajanje sa listom osumnjičenih
u_zgradi = prisutni_u_vrijeme_zlocina.merge(osumnjiceni, on="ime_prezime")

print(f"\nUkupno ulazaka u Tech Hub tog dana: {len(tech_hub_15)}")
print(f"Osoba u zgradi tokom ubistva: {len(prisutni_u_vrijeme_zlocina)}")
print(f"Od toga osumnjičeni: {len(u_zgradi)}")

print("\nGlavni osumnjičeni (bili u zgradi):")
print(u_zgradi[["ime_prezime", "vrijeme_ulaza", "vrijeme_izlaza"]])

# --- DETALJNA ANALIZA IZJAVA ---

# Analiza za Emira Begovića
print("\n--- Izjave koje spominju Emira Begovića ---")
# Koristimo kolonu 'spominje_osumnjicenog' kako si naveo
emir_izjave = svjedoci[svjedoci["spominje_osumnjicenog"] == "Emir Begović"]
if not emir_izjave.empty:
    print(emir_izjave[["izjava_id", "vrijeme", "svjedok", "opis"]].to_string(index=False))

# Analiza za Dina Delića
print("\n--- Izjave koje spominju Dina Delića ---")
dino_izjave = svjedoci[svjedoci["spominje_osumnjicenog"] == "Dino Delić"]
if not dino_izjave.empty:
    print(dino_izjave[["izjava_id", "vrijeme", "svjedok", "opis"]].to_string(index=False))

# Analiza nepoznatih osoba (izjave gdje niko nije imenovan)
print("\n--- Izjave o nepoznatim osobama (niko nije imenovan) ---")
# Uzimamo izjave gdje je kolona 'spominje_osumnjicenog' prazna (ili sadrži 'nepoznato' / NaN)
nepoznati = svjedoci[svjedoci["spominje_osumnjicenog"].isna() | (svjedoci["spominje_osumnjicenog"] == "")]

if not nepoznati.empty:
    print(nepoznati[["izjava_id", "vrijeme", "opis"]].to_string(index=False))


    finansije = pd.read.csv("finansijski_zapisi")