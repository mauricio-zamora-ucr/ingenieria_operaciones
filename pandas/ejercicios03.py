import pandas as pd
import numpy as np


np.random.seed(
    1405
)  # Semilla para que los resultados sean reproducibles (modificar la generación de números aleatorios)

# Asumamos que tienes un archivo llamado 'datos_produccion.csv' con columnas como 'Fecha', 'Producto', 'Cantidad', 'Defectos'
datos_produccion = pd.read_csv('./pandas/datos_produccion.csv')
print(datos_produccion.head())

df_agrupado = datos_produccion.groupby(['Producto']).agg(
    Total_Producido=('Cantidad', 'sum'),
    Total_Defectos=('Defectos', 'mean')  # Cambiado 'average' por 'mean'
)
print(df_agrupado)

# Guardar el DataFrame 'df_agrupado' que creamos antes en un archivo CSV llamado 'resumen_produccion.csv'
df_agrupado.to_csv('resumen_produccion.csv')

# Puedes controlar si se guarda el índice o no
df_agrupado.to_csv('resumen_produccion_sin_indice.csv', index=False)