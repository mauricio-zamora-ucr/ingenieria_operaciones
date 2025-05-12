from prophet import Prophet
import pandas as pd
import numpy as np

import pandas as pd
import numpy as np
from prophet import Prophet
import matplotlib.pyplot as plt

# PREDICCIÓN DE SERIES TEMPORALES CON PROPHET
print("\n" + "="*60)
print("SISTEMA DE PREDICCIÓN INDUSTRIAL - DEMANDA Y PRODUCCIÓN")
print("="*60 + "\n")

## 1. CONFIGURACIÓN INICIAL
print("\n1. INICIALIZACIÓN DEL MODELO")
print("-"*50)
print("Configurando entorno predictivo...")
np.random.seed(1405)  # Semilla para reproducibilidad
print("✓ Semilla aleatoria establecida (1405)")
print("✓ Librerías Prophet y Matplotlib importadas")
print("✓ Entorno listo para modelado predictivo\n")

## 2. GENERACIÓN DE DATOS SIMULADOS
print("\n2. PREPARACIÓN DE DATOS")
print("-"*50)

### 2.1 Datos de Demanda Diaria
print("\n2.1 Generando datos de demanda diaria (100 días)...")
fechas_demanda = pd.date_range('2024-01-01', periods=100, freq='D')

# Componentes de la demanda
tendencia = np.linspace(100, 150, 100)
estacionalidad_semanal = 20 * np.sin(2 * np.pi * fechas_demanda.dayofweek / 7)
ruido = np.random.normal(0, 10, 100)
demanda = np.round(tendencia + estacionalidad_semanal + ruido, 2)

df_demanda = pd.DataFrame({
    'ds': fechas_demanda,
    'y': demanda
})

print("\nMuestra de datos de demanda (primeros 5 registros):")
print(df_demanda.head())
print(f"\nEstadísticas descriptivas:\n{df_demanda['y'].describe()}")

### 2.2 Datos de Producción Horaria
print("\n2.2 Generando datos de producción horaria (30 días)...")
fechas_produccion = pd.date_range('2024-01-01 00:00:00', periods=24*30, freq='h')

# Componentes de producción
patron_diario = 10 * np.sin(2 * np.pi * fechas_produccion.hour / 24) + 50
ruido_horario = np.random.normal(0, 5, 24*30)
produccion = np.round(patron_diario + ruido_horario, 2)

df_produccion = pd.DataFrame({
    'ds': fechas_produccion,
    'y': produccion
})

print("\nMuestra de datos de producción (primeros 5 registros):")
print(df_produccion.head())
print(f"\nEstadísticas descriptivas:\n{df_produccion['y'].describe()}")

## 3. MODELADO PREDICTIVO
print("\n\n3. ENTRENAMIENTO DE MODELOS")
print("-"*50)

### 3.1 Modelo de Demanda
print("\n3.1 Entrenando modelo de demanda diaria...")
modelo_demanda = Prophet(
    yearly_seasonality=False,
    daily_seasonality=False,
    weekly_seasonality=True,
    seasonality_mode='additive'
)
modelo_demanda.fit(df_demanda)
print("✓ Modelo de demanda entrenado correctamente")

### 3.2 Modelo de Producción
print("\n3.2 Entrenando modelo de producción horaria...")
modelo_produccion = Prophet(
    yearly_seasonality=False,
    daily_seasonality=True,
    weekly_seasonality=True,
    seasonality_mode='additive'
)
modelo_produccion.fit(df_produccion)
print("✓ Modelo de producción entrenado correctamente")

## 4. PREDICCIÓN Y VISUALIZACIÓN
print("\n\n4. GENERACIÓN DE PREDICCIONES")
print("-"*50)

### 4.1 Predicción de Demanda
print("\n4.1 Prediciendo demanda para los próximos 30 días...")
futuro_demanda = modelo_demanda.make_future_dataframe(periods=30)
prediccion_demanda = modelo_demanda.predict(futuro_demanda)

print("\nResumen de predicción de demanda:")
print(prediccion_demanda[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail())

# Visualización
print("\nGenerando gráficos de predicción de demanda...")
fig1 = modelo_demanda.plot(prediccion_demanda)
plt.title('Predicción de Demanda Diaria - 30 Días', pad=20)
plt.xlabel('Fecha')
plt.ylabel('Unidades Demandadas')
plt.grid(True, linestyle='--', alpha=0.3)
plt.tight_layout()
plt.savefig('prediccion_demanda.png', dpi=300)
plt.show()
print("✓ Gráfico guardado como 'prediccion_demanda.png'")

fig2 = modelo_demanda.plot_components(prediccion_demanda)
plt.tight_layout()
plt.savefig('componentes_demanda.png', dpi=300)
plt.show()
print("✓ Componentes guardados como 'componentes_demanda.png'")

### 4.2 Predicción de Producción
print("\n4.2 Prediciendo producción para las próximas 48 horas...")
futuro_produccion = modelo_produccion.make_future_dataframe(periods=48, freq='h')
prediccion_produccion = modelo_produccion.predict(futuro_produccion)

print("\nResumen de predicción de producción:")
print(prediccion_produccion[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail())

# Visualización
print("\nGenerando gráficos de predicción de producción...")
fig3 = modelo_produccion.plot(prediccion_produccion)
plt.title('Predicción de Producción Horaria - 48 Horas', pad=20)
plt.xlabel('Fecha y Hora')
plt.ylabel('Unidades Producidas')
plt.grid(True, linestyle='--', alpha=0.3)
plt.tight_layout()
plt.savefig('prediccion_produccion.png', dpi=300)
plt.show()
print("✓ Gráfico guardado como 'prediccion_produccion.png'")

fig4 = modelo_produccion.plot_components(prediccion_produccion)
plt.tight_layout()
plt.savefig('componentes_produccion.png', dpi=300)
plt.show()
print("✓ Componentes guardados como 'componentes_produccion.png'")

# Probando diferentes valores de changepoint_prior_scale
modelos = {}
valores_cps = [0.001, 0.01, 0.1, 0.5]

for cps in valores_cps:
    m = Prophet(changepoint_prior_scale=cps)
    m.fit(df_demanda)
    future = m.make_future_dataframe(periods=30)
    forecast = m.predict(future)
    modelos[cps] = forecast[['ds', 'yhat']]

# Ahora puedes comparar las predicciones de los diferentes modelos
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(df_demanda['ds'], df_demanda['y'], 'k.', label='Datos Históricos')
for cps, forecast in modelos.items():
    ax.plot(forecast['ds'], forecast['yhat'], label=f'CPS = {cps}')
ax.legend()
plt.show()
plt.savefig('comparacion_cps.png', dpi=300)
print("✓ Gráfico de comparación de changepoint_prior_scale guardado como 'comparacion_cps.png'")

import pandas as pd
import numpy as np
from prophet import Prophet
import matplotlib.pyplot as plt

# PREDICCIÓN DE SERIES TEMPORALES CON PROPHET
print("\n" + "="*60)
print("SISTEMA DE PREDICCIÓN INDUSTRIAL - DEMANDA Y PRODUCCIÓN")
print("="*60 + "\n")

## 1. CONFIGURACIÓN INICIAL
print("\n1. INICIALIZACIÓN DEL MODELO")
print("-"*50)
print("Configurando entorno predictivo...")
np.random.seed(1405)  # Semilla para reproducibilidad
print("✓ Semilla aleatoria establecida (1405)")
print("✓ Librerías Prophet y Matplotlib importadas")
print("✓ Entorno listo para modelado predictivo\n")

## 2. GENERACIÓN DE DATOS SIMULADOS
print("\n2. PREPARACIÓN DE DATOS")
print("-"*50)

### 2.1 Datos de Demanda Diaria
print("\n2.1 Generando datos de demanda diaria (100 días)...")
fechas_demanda = pd.date_range('2024-01-01', periods=100, freq='D')

# Componentes de la demanda
tendencia = np.linspace(100, 150, 100)
estacionalidad_semanal = 20 * np.sin(2 * np.pi * fechas_demanda.dayofweek / 7)
ruido = np.random.normal(0, 10, 100)
demanda = np.round(tendencia + estacionalidad_semanal + ruido, 2)

df_demanda = pd.DataFrame({
    'ds': fechas_demanda,
    'y': demanda
})

print("\nMuestra de datos de demanda (primeros 5 registros):")
print(df_demanda.head())
print(f"\nEstadísticas descriptivas:\n{df_demanda['y'].describe()}")

### 2.2 Datos de Producción Horaria
print("\n2.2 Generando datos de producción horaria (30 días)...")
fechas_produccion = pd.date_range('2024-01-01 00:00:00', periods=24*30, freq='h')

# Componentes de producción
patron_diario = 10 * np.sin(2 * np.pi * fechas_produccion.hour / 24) + 50
ruido_horario = np.random.normal(0, 5, 24*30)
produccion = np.round(patron_diario + ruido_horario, 2)

df_produccion = pd.DataFrame({
    'ds': fechas_produccion,
    'y': produccion
})

print("\nMuestra de datos de producción (primeros 5 registros):")
print(df_produccion.head())
print(f"\nEstadísticas descriptivas:\n{df_produccion['y'].describe()}")

## 3. MODELADO PREDICTIVO
print("\n\n3. ENTRENAMIENTO DE MODELOS")
print("-"*50)

### 3.1 Modelo de Demanda
print("\n3.1 Entrenando modelo de demanda diaria...")
modelo_demanda = Prophet(
    yearly_seasonality=False,
    daily_seasonality=False,
    weekly_seasonality=True,
    seasonality_mode='additive'
)
modelo_demanda.fit(df_demanda)
print("✓ Modelo de demanda entrenado correctamente")

### 3.2 Modelo de Producción
print("\n3.2 Entrenando modelo de producción horaria...")
modelo_produccion = Prophet(
    yearly_seasonality=False,
    daily_seasonality=True,
    weekly_seasonality=True,
    seasonality_mode='additive'
)
modelo_produccion.fit(df_produccion)
print("✓ Modelo de producción entrenado correctamente")

## 4. PREDICCIÓN Y VISUALIZACIÓN
print("\n\n4. GENERACIÓN DE PREDICCIONES")
print("-"*50)

### 4.1 Predicción de Demanda
print("\n4.1 Prediciendo demanda para los próximos 30 días...")
futuro_demanda = modelo_demanda.make_future_dataframe(periods=30)
prediccion_demanda = modelo_demanda.predict(futuro_demanda)

print("\nResumen de predicción de demanda:")
print(prediccion_demanda[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail())

# Visualización
print("\nGenerando gráficos de predicción de demanda...")
fig1 = modelo_demanda.plot(prediccion_demanda)
plt.title('Predicción de Demanda Diaria - 30 Días', pad=20)
plt.xlabel('Fecha')
plt.ylabel('Unidades Demandadas')
plt.grid(True, linestyle='--', alpha=0.3)
plt.tight_layout()
plt.savefig('prediccion_demanda.png', dpi=300)
plt.show()
print("✓ Gráfico guardado como 'prediccion_demanda.png'")

fig2 = modelo_demanda.plot_components(prediccion_demanda)
plt.tight_layout()
plt.savefig('componentes_demanda.png', dpi=300)
plt.show()
print("✓ Componentes guardados como 'componentes_demanda.png'")

### 4.2 Predicción de Producción
print("\n4.2 Prediciendo producción para las próximas 48 horas...")
futuro_produccion = modelo_produccion.make_future_dataframe(periods=48, freq='h')
prediccion_produccion = modelo_produccion.predict(futuro_produccion)

print("\nResumen de predicción de producción:")
print(prediccion_produccion[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail())

# Visualización
print("\nGenerando gráficos de predicción de producción...")
fig3 = modelo_produccion.plot(prediccion_produccion)
plt.title('Predicción de Producción Horaria - 48 Horas', pad=20)
plt.xlabel('Fecha y Hora')
plt.ylabel('Unidades Producidas')
plt.grid(True, linestyle='--', alpha=0.3)
plt.tight_layout()
plt.savefig('prediccion_produccion.png', dpi=300)
plt.show()
print("✓ Gráfico guardado como 'prediccion_produccion.png'")

fig4 = modelo_produccion.plot_components(prediccion_produccion)
plt.tight_layout()
plt.savefig('componentes_produccion.png', dpi=300)
plt.show()
print("✓ Componentes guardados como 'componentes_produccion.png'")
