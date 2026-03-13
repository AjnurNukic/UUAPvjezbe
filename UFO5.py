import pandas as pd
import plotly.express as px

# Učitavanje podataka
df = pd.read_csv('ufo_sightings.csv', low_memory=False)

# 1. Čišćenje kolona s datumom i vremenom
# 'errors="coerce"' pretvara neispravne datume u NaT (Not a Time)
df['datetime'] = pd.to_datetime(df['datetime'], errors='coerce')
df = df.dropna(subset=['datetime'])

# 2. Izdvajanje godine, mjeseca i sata
df['year'] = df['datetime'].dt.year
df['month'] = df['datetime'].dt.month
df['hour'] = df['datetime'].dt.hour

# --- 3. Analiza ---

# Viđenja godišnje
yearly_counts = df['year'].value_counts().sort_index()

# Viđenja po državi (top 10)
country_counts = df['country'].value_counts().head(10)

# Najčešći oblici NLO-a (top 10)
shape_counts = df['shape'].value_counts().head(10)

print("Analiza završena. Prikazujem vizualizaciju...")

# --- 4. Vizualizacija karte svijeta ---

# Čistimo koordinate za kartu (kao i prije)
df['latitude'] = pd.to_numeric(df['latitude'], errors='coerce')
df['longitude'] = pd.to_numeric(df['longitude'], errors='coerce')
df_map = df.dropna(subset=['latitude', 'longitude']).sample(5000) # Uzorak za brži prikaz

fig = px.scatter_geo(
    df_map,
    lat="latitude",
    lon="longitude",
    hover_name="city",
    color="year", # Boja po godini viđenja
    title="NLO viđenja kroz godine",
    template="plotly_dark",
    color_continuous_scale=px.colors.sequential.Plasma
)

fig.show()