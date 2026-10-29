import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler

# Impostiamo il seme per ottenere sempre gli stessi dati casuali
np.random.seed(42)

# Generiamo 60 date giornaliere
dates = pd.date_range("2025-01-01", periods=60, freq="D")

# Generiamo il numero giornaliero di passeggeri
n_pass = np.random.randint(1000, 5000, size=60)

# Generiamo le temperature medie giornaliere
temperatura_media = np.random.uniform(-5, 25, size=60)

# Creiamo il DataFrame con i dati
df = pd.DataFrame({
    "Dates": dates,
    "NumeroPasseggeri": n_pass,
    "TemperaturaMedia": temperatura_media
})


# ==================================================
# PRIMO GRAFICO: DOPPIO ASSE VERTICALE
# ==================================================

# Creiamo la figura e il primo asse
fig, ax1 = plt.subplots(figsize=(12, 5))

# Disegniamo il numero di passeggeri sul primo asse
ax1.plot(
    df["Dates"],
    df["NumeroPasseggeri"],
    color="blue",
    label="Passeggeri"
)

# Impostiamo il nome e il colore dell'asse dei passeggeri
ax1.set_xlabel("Data")
ax1.set_ylabel("Passeggeri", color="blue")
ax1.tick_params(axis="y", labelcolor="blue")

# Creiamo il secondo asse verticale
ax2 = ax1.twinx()

# Disegniamo la temperatura sul secondo asse
ax2.plot(
    df["Dates"],
    df["TemperaturaMedia"],
    color="red",
    linestyle="--",
    label="Temperatura"
)

# Impostiamo il nome e il colore dell'asse della temperatura
ax2.set_ylabel("Temperatura (°C)", color="red")
ax2.tick_params(axis="y", labelcolor="red")

# Aggiungiamo il titolo e le legende
fig.suptitle("Trasporto pubblico vs temperatura")
ax1.legend(loc="upper left")
ax2.legend(loc="upper right")

# Sistemiamo gli spazi e visualizziamo il grafico
fig.tight_layout()
plt.show()


# ==================================================
# SECONDO GRAFICO: NORMALIZZAZIONE 0-1
# ==================================================

# Creiamo una copia del DataFrame originale
df_transport_norm = df.copy()

# Creiamo lo strumento per la normalizzazione
scaler = MinMaxScaler()

# Normalizziamo le due colonne numeriche
# Le date rimangono invariate
df_transport_norm[["NumeroPasseggeri", "TemperaturaMedia"]] = (
    scaler.fit_transform(
        df[["NumeroPasseggeri", "TemperaturaMedia"]]
    )
)

# Creiamo il grafico dei valori normalizzati
plt.figure(figsize=(12, 5))

# Disegniamo i passeggeri normalizzati
plt.plot(
    df_transport_norm["Dates"],
    df_transport_norm["NumeroPasseggeri"],
    color="blue",
    label="Passeggeri (norm)"
)

# Disegniamo le temperature normalizzate
plt.plot(
    df_transport_norm["Dates"],
    df_transport_norm["TemperaturaMedia"],
    color="red",
    linestyle="--",
    label="Temperatura (norm)"
)

# Personalizziamo il grafico
plt.title("Trasporto pubblico vs temperatura - normalizzati")
plt.xlabel("Data")
plt.ylabel("Valori normalizzati (0-1)")

# Mostriamo la legenda e sistemiamo gli spazi
plt.legend()
plt.tight_layout()

# Visualizziamo il grafico
plt.show()


# ==================================================
# ANALISI DEI RISULTATI
# ==================================================

print("Analisi:")
print(
    "Il doppio asse mostra i valori reali di passeggeri e temperatura, "
    "ma le scale differenti possono rendere più difficile confrontare "
    "visivamente i rispettivi andamenti."
)
print(
    "La normalizzazione porta entrambe le variabili su una scala da 0 a 1, "
    "facilitando il confronto delle loro variazioni relative."
)
print(
    "La normalizzazione non dimostra, da sola, l'esistenza di una relazione "
    "tra le due variabili."
)