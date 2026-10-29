import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Impostiamo il seme per ottenere sempre gli stessi dati casuali
np.random.seed(42)

# Generiamo 30 giorni di date, con una misurazione ogni ora
dates = pd.date_range("2026-01-01", freq="h", periods=30*24)

# Generiamo i consumi energetici simulati in watt
# Media dei consumi: 300 W
# Variabilità: 50 W
consumo_watt = np.random.normal(
    loc=300,
    size=720,
    scale=50
)

# Creiamo il DataFrame con date e consumi
df = pd.DataFrame({
    "Date": dates,
    "Consumi": consumo_watt
})

# Impostiamo le date come indice del DataFrame
df.set_index("Date", inplace=True)

# Calcoliamo le medie giornaliere e settimanali
daily_mean = df.resample("D").mean()
weekly_mean = df.resample("W").mean()

# Creiamo il grafico
plt.figure(figsize=(12, 5))

# Disegniamo i consumi orari
plt.plot(
    df.index,
    df["Consumi"],
    alpha=0.5,
    color="lightgray",
    label="Orario"
)

# Disegniamo le medie giornaliere
plt.plot(
    daily_mean.index,
    daily_mean["Consumi"],
    color="blue",
    marker="o",
    label="Giornaliero"
)

# Disegniamo le medie settimanali
plt.plot(
    weekly_mean.index,
    weekly_mean["Consumi"],
    color="red",
    marker="s",
    label="Settimanale"
)

# Personalizziamo il grafico
plt.title("Consumi energetici - confronto aggregazioni")
plt.ylabel("Consumo (W)")
plt.xlabel("Data")

# Mostriamo la legenda
plt.legend()

# Sistemiamo gli spazi del grafico
plt.tight_layout()

# Visualizziamo il grafico
plt.show()

# Analizziamo i risultati
print("Analisi:")
print(
    "La media giornaliera smussa le fluttuazioni orarie "
    "evidenziando i picchi di consumo."
)
print(
    "La media settimanale riduce ulteriormente la variabilità, "
    "rendendo meno visibili i picchi giornalieri ma più leggibile "
    "il trend complessivo."
)