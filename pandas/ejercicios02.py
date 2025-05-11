import pandas as pd
import numpy as np


print("Estableciendo semilla para números aleatorios (1405) para reproducibilidad...")
np.random.seed(1405)  # Semilla para que los resultados sean reproducibles (modificar la generación de números aleatorios)
print("Semilla establecida correctamente.\n")

# Creación de Objetos
print("Creando Series de pandas:")
print("1. Serie básica con valores [1, 3, 5, np.nan, 6, 8]:")
s = pd.Series([1, 3, 5, np.nan, 6, 8])
print(s)

print("\n2. Serie con índices personalizados ['Enero', 'Febrero', 'Marzo']:")
s = pd.Series([10, 20, 15], index=["Enero", "Febrero", "Marzo"])
print(s)

print("\nGenerando rango de fechas desde 20230101 con 6 periodos...")
fechas = pd.date_range("20230101", periods=6)  # Genera un rango de fechas
print("Fechas generadas:", fechas)

print("\nCreando DataFrame con valores aleatorios:")
df = pd.DataFrame(np.random.randn(6, 4), index=fechas, columns=["A", "B", "C", "D"])
print("DataFrame creado:")
print(df)

print("\nCreando DataFrame con datos estructurados:")
df2 = pd.DataFrame(
    {
        "Material": ["Acero", "Aluminio", "Cobre", "Acero"],
        "Costo_Kg": [2.5, 3.0, 4.0, 2.5],
        "Proveedor": pd.Categorical(["A", "B", "A", "C"]),  # Tipo categórico para datos repetidos
    }
)
print("DataFrame de materiales creado:")
print(df2)


# Visualización de Datos
print("\nVISUALIZACIÓN DE DATOS:")
print("\nMostrando las primeras 5 filas del DataFrame:")
print(df.head())

print("\nMostrando las últimas 3 filas del DataFrame:")
print(df.tail(3))

print("\nMostrando los índices (fechas) del DataFrame:")
print(df.index)

print("\nMostrando las columnas del DataFrame:")
print(df.columns)

print("\nConvirtiendo DataFrame a array numpy:")
print(df.to_numpy())

print("\nEstadísticas descriptivas del DataFrame:")
print(df.describe())  # Cuenta, media, desviación estándar, mínimo, máximo, etc.

print("\nTransponiendo el DataFrame:")
print(df.T)

print("\nOrdenando columnas alfabéticamente en orden inverso:")
print(df.sort_index(axis=1, ascending=False))

print("\nOrdenando valores por la columna 'B':")
print(df.sort_values(by='B'))


# Selección de Datos
print("\nSELECCIÓN DE DATOS:")
print("\nSeleccionando solo la columna 'A':")
print(df['A'])

print("\nSeleccionando las columnas 'A' y 'C':")
print(df[['A', 'C']])

print("\nSeleccionando filas desde la posición 0 hasta la 2 (sin incluir la 3):")
print(df[0:3])

print("\nSeleccionando filas con índices desde '20230102' hasta '20230104' (incluyendo extremos):")
print(df['20230102':'20230104'])

print("\nSeleccionando fila con la primera etiqueta de fecha usando loc:")
print(df.loc[fechas[0]])

print("\nSeleccionando todas las filas y solo columnas 'A' y 'B':")
print(df.loc[:, ['A', 'B']])

print("\nSeleccionando rango de filas y columnas específicas:")
print(df.loc['20230102':'20230104', ['A', 'B']])

print("\nSeleccionando valor específico por etiqueta de fila y columna:")
print(df.loc['20230102', ['A', 'B']])

print("\nSeleccionando valor único por fecha y columna (más rápido para un solo valor):")
print(df.loc[fechas[0], 'A'])

# OPERACIONES CON ÍNDICES NUMÉRICOS (ILOC)
print("\nOPERACIONES CON ÍNDICES NUMÉRICOS (ILOC):")
print("\nSeleccionando la fila en la posición 3 (índice 3) usando iloc:")
print(df.iloc[3])  # Selecciona la fila en la tercera posición (índice 3)

print("\nSeleccionando filas 3 a 4 y columnas 0 a 1 usando iloc:")
print(df.iloc[3:5, 0:2])  # Selecciona las filas en las posiciones 3 y 4, y las columnas en las posiciones 0 y 1

print("\nSeleccionando filas específicas (1, 2, 4) y columnas específicas (0, 2) por posición:")
print(df.iloc[[1, 2, 4], [0, 2]])  # Selecciona filas y columnas específicas por posición

print("\nSeleccionando valor específico en la segunda fila (1) y segunda columna (1):")
print(df.iloc[1, 1])  # Selecciona el valor en la segunda fila y la segunda columna


# FILTRADO DE DATOS
print("\nFILTRADO DE DATOS:")
print("\nFiltrando filas donde valores en columna 'A' son mayores que 0:")
print(df[df['A'] > 0])  # Selecciona las filas donde los valores de la columna 'A' son mayores que 0

print("\nFiltrando todos los valores mayores que 0 (otros serán NaN):")
print(df[df > 0])  # Selecciona todos los valores mayores que 0 (los demás serán NaN)

print("\nCreando nuevo DataFrame para demostración de filtrado:")
df2 = pd.DataFrame({
    'Material': ['Acero', 'Aluminio', 'Cobre', 'Acero', 'Bronce'],
    'Proveedor': ['A', 'B', 'A', 'C', 'B']
})
print("DataFrame original:")
print(df2)

print("\nFiltrando filas donde Material es 'Acero' o 'Cobre':")
print(df2[df2['Material'].isin(['Acero', 'Cobre'])])  # Selecciona filas donde la columna 'Material' es 'Acero' o 'Cobre'


# MANEJO DE VALORES FALTANTES
print("\nMANEJO DE VALORES FALTANTES:")
print("\nCreando DataFrame con valores faltantes:")
df_con_nan = df.reindex(index=fechas[:4], columns=list(df.columns) + ['E'])
df_con_nan.loc[:fechas[1], 'E'] = 1  # Asignando valores a las primeras filas de la columna 'E'
print("DataFrame con valores NaN:")
print(df_con_nan)

print("\nEliminando filas con ALGÚN valor faltante:")
print(df_con_nan.dropna(how='any'))  # Elimina filas con *algún* valor faltante

print("\nEliminando filas donde TODOS los valores son faltantes:")
print(df_con_nan.dropna(how='all'))  # Elimina filas donde *todos* los valores son faltantes

print("\nRellenando valores faltantes con 0:")
print(df_con_nan.fillna(value=0))  # Reemplaza los NaN con 0

print("\nIdentificando valores faltantes (True = faltante):")
print(pd.isna(df_con_nan))


# OPERACIONES ESTADÍSTICAS
print("\nOPERACIONES ESTADÍSTICAS:")
print("\nCalculando media de cada columna:")
print(df.mean())  # Calcula la media de cada columna

print("\nCalculando media de cada fila:")
print(df.mean(axis=1))  # Calcula la media de cada fila

print("\nCalculando suma acumulativa para columna 'A':")
print(df['A'].apply(np.cumsum))  # Calcula la suma acumulada de la columna 'A'

print("\nAplicando función para calcular rango (max-min) por columna:")
print(df.apply(lambda x: x.max() - x.min()))  # Aplica función para encontrar diferencia entre máximo y mínimo de cada columna


# VISUALIZACIÓN DE DATOS
print("\nVISUALIZACIÓN DE DATOS:")
print("\nGenerando histograma para columna 'A'...")
import matplotlib.pyplot as plt
plt.figure()  # Crea una nueva figura para el gráfico
df['A'].hist()
plt.xlabel('Valor de A')
plt.ylabel('Frecuencia')
plt.title('Histograma de la Columna A')
plt.show()
print("Histograma mostrado en ventana emergente.")


# COMBINACIÓN DE DATOS
print("\nCOMBINACIÓN DE DATOS:")
print("\nConcatenando primeras 3 filas con el resto del DataFrame:")
df_concat = pd.concat([df[:3], df[3:]])  # Combina las primeras 3 filas con las siguientes
print(df_concat)

print("\nDemostración de merge (unión) de DataFrames:")
izquierda = pd.DataFrame({'clave': ['foo', 'bar'], 'valor': [1, 2]})
derecha = pd.DataFrame({'clave': ['foo', 'foo'], 'valor2': [4, 5]})
print("DataFrame izquierdo:")
print(izquierda)
print("\nDataFrame derecho:")
print(derecha)
print("\nResultado del merge basado en columna 'clave':")
print(pd.merge(izquierda, derecha, on='clave'))  # Combina basado en la columna 'clave'


# AGRUPACIÓN DE DATOS
print("\nAGRUPACIÓN DE DATOS:")
print("\nCreando DataFrame para demostración de agrupación:")
df_agrupado = pd.DataFrame({
    'Departamento': ['Producción', 'Ventas', 'Producción', 'Ventas', 'Logística'],
    'Cantidad': [100, 50, 120, 60, 80]
})
print("DataFrame original:")
print(df_agrupado)

print("\nSumando cantidades por departamento:")
print(df_agrupado.groupby('Departamento').sum())  # Suma la 'Cantidad' por cada 'Departamento'