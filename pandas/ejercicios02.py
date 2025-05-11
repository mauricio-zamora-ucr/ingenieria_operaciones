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

df2 = pd.DataFrame(
    {
        "Material": ["Acero", "Aluminio", "Cobre", "Acero"],
        "Costo_Kg": [2.5, 3.0, 4.0, 2.5],
        "Proveedor": pd.Categorical(
            ["A", "B", "A", "C"]
        ),  # Tipo categórico para datos repetidos
    }
)
print(df2)


# Visualización de Datos
print(df.head())  # Muestra las primeras 5 filas
print(df.tail(3))  # Muestra las últimas 3 filas

print(df.index)  # Muestra las fechas
print(df.columns)  # Muestra las columnas ('A', 'B', 'C', 'D')

print(df.to_numpy())

print(df.describe())  # Cuenta, media, desviación estándar, mínimo, máximo, etc.

print(df.T)

print(
    df.sort_index(axis=1, ascending=False)
)  # Ordena las columnas alfabéticamente en reversa
print(df.sort_values(by="B"))  # Ordena por los valores de la columna 'B'


# Selección de Datos
print(df["A"])  # Selecciona la columna 'A'
print(df[["A", "C"]])  # Selecciona las columnas 'A' y 'C'

print(df[0:3])  # Selecciona las filas desde la posición 0 hasta la 2 (sin incluir la 3)
print(
    df["20230102":"20230104"]
)  # Selecciona las filas con etiquetas de índice desde '20230102' hasta '20230104' (¡ojo! aquí sí se incluye el final)

print(df.loc[fechas[0]])  # Selecciona la fila con la primera etiqueta de fecha
print(df.loc[:, ["A", "B"]])  # Selecciona todas las filas y las columnas 'A' y 'B'
print(
    df.loc["20230102":"20230104", ["A", "B"]]
)  # Selecciona un rango de filas y columnas
print(
    df.loc["20230102", ["A", "B"]]
)  # Selecciona un valor específico por etiqueta de fila y columna
print(
    df.loc[fechas[0], "A"]
)  # Otra forma de seleccionar un valor específico (más rápido para un solo valor)
