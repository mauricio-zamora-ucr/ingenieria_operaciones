import pandas as pd
import numpy as np


np.random.seed(
    1405
)  # Semilla para que los resultados sean reproducibles (modificar la generación de números aleatorios)

# Creación de Objetos
s = pd.Series([1, 3, 5, np.nan, 6, 8])
print(s)

s = pd.Series([10, 20, 15], index=["Enero", "Febrero", "Marzo"])
print(s)

fechas = pd.date_range("20230101", periods=6)  # Genera un rango de fechas
df = pd.DataFrame(np.random.randn(6, 4), index=fechas, columns=["A", "B", "C", "D"])
print(df)
