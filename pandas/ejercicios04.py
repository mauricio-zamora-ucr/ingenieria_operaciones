import pandas as pd
import numpy as np

print("Inicializando generación de números aleatorios con semilla 1405 para reproducibilidad...")
np.random.seed(1405)  # Semilla para que los resultados sean reproducibles
print("Semilla establecida correctamente.\n")

# SERIES TEMPORALES BÁSICAS
print("CREACIÓN DE SERIE TEMPORAL:")
print("Generando rango de 10 fechas diarias a partir del 1/1/2024...")
fechas = pd.date_range('20240101', periods=10, freq='D')  # 'D' indica frecuencia diaria
print("Fechas generadas:", fechas)

print("\nCreando serie temporal con valores aleatorios:")
ts = pd.Series(np.random.randn(len(fechas)), index=fechas)
print("Serie temporal creada:")
print(ts)

# SELECCIÓN DE DATOS TEMPORALES
print("\nSELECCIÓN DE DATOS POR FECHA:")
print("\nSeleccionando valor para el 5 de enero de 2024:")
print(ts['2024-01-05'])  # Selecciona el valor para el 5 de enero de 2024

print("\nSeleccionando todos los valores de enero de 2024:")
print(ts['2024-01'])  # Selecciona todos los valores de enero de 2024

print("\nSeleccionando rango de fechas del 3 al 7 de enero:")
print(ts['2024-01-03':'2024-01-07'])  # Selecciona el rango de fechas

# OPERACIONES TEMPORALES
print("\nOPERACIONES DE REMUESTREO TEMPORAL:")
print("\nResampleo a frecuencia semanal (suma de valores por semana):")
print(ts.resample('W').sum())

print("\nResampleo a frecuencia mensual (media de valores por mes):")
print(ts.resample('ME').mean())

print("\nCÁLCULOS TEMPORALES AVANZADOS:")
print("\nMedia móvil de los últimos 3 días:")
print(ts.rolling(window=3).mean())

print("\nDiferencia con el período anterior:")
print(ts.diff())

print("\nDesplazando datos un día hacia adelante:")
print(ts.shift(1))

print("\nDesplazando datos un día hacia atrás:")
print(ts.shift(-1))

# APLICACIÓN EN INGENIERÍA INDUSTRIAL
print("\nAPLICACIÓN PRÁCTICA: SIMULACIÓN DE DEMANDA DE PRODUCTO")
print("\nGenerando datos de demanda diaria para 30 días...")
fechas_demanda = pd.date_range('20240101', periods=30, freq='D')
demanda = pd.Series(np.random.randint(50, 200, size=30), index=fechas_demanda)
print("\nMuestra de los primeros 5 días de demanda:")
print(demanda.head())

print("\nCalculando media móvil semanal para suavizar fluctuaciones:")
demanda_semanal_media = demanda.rolling(window=7).mean()
print("\nMedia móvil semanal (últimos 5 valores):")
print(demanda_semanal_media.tail())

print("\nCalculando demanda mensual total:")
demanda_mensual_total = demanda.resample('ME').sum()
print("\nDemanda total por mes:")
print(demanda_mensual_total)