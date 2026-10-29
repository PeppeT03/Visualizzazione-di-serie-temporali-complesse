import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Impostiamo il seme per ottenere sempre gli stessi dati casuali
np.random.seed(42)

# Creiamo 60 date giornaliere, dal 1° gennaio 2025
dates = pd.date_range("2025-01-01", periods=60, freq="D")

# Generiamo i nuovi casi giornalieri simulati
# La distribuzione di Poisson genera variazioni casuali intorno a 200
# np.linspace crea un aumento progressivo da 0 a 1000
# Sommiamo i due risultati per simulare un'epidemia in crescita
new_cases = (
    np.random.poisson(200, size=60)
    + np.linspace(0, 1000, 60).astype(int)
)

# Creiamo il DataFrame con date e nuovi casi
df = pd.DataFrame({
    "date": dates,
    "new_cases": new_cases
})

# Calcoliamo la media mobile su 7 giorni
# window=7: considera gli ultimi 7 valori
# min_periods=1: all'inizio calcola la media anche se ci sono meno di 7 valori
df["MA7"] = df["new_cases"].rolling(
    window=7,
    min_periods=1
).mean()

# Calcoliamo lo smoothing esponenziale
# alpha=0.3 regola quanto peso dare ai dati più recenti
df["EWMA"] = df["new_cases"].ewm(alpha=0.3).mean()

# Creiamo il grafico
plt.figure(figsize=(12, 5))

# Disegniamo i casi originali, con tutte le oscillazioni giornaliere
plt.plot(
    df["date"],
    df["new_cases"],
    color="lightgray",
    alpha=0.5,
    label="Originale"
)

# Disegniamo la media mobile a 7 giorni
plt.plot(
    df["date"],
    df["MA7"],
    color="blue",
    label="Media mobile 7 giorni"
)

# Disegniamo lo smoothing esponenziale
plt.plot(
    df["date"],
    df["EWMA"],
    color="red",
    label="Smoothing esponenziale"
)

# Personalizziamo il grafico
plt.title("Nuovi casi giornalieri - confronto smoothing")
plt.xlabel("Data")
plt.ylabel("Nuovi casi")

# Mostriamo la legenda
plt.legend()

# Sistemiamo gli spazi
plt.tight_layout()

# Visualizziamo il grafico
plt.show()

# Analisi dei risultati
print("Analisi:")
print(
    "Lo smoothing esponenziale reagisce più rapidamente "
    "ai cambiamenti recenti rispetto alla media mobile,"
)
print(
    "che invece smussa uniformemente i valori su 7 giorni."
)