# **Tutorial Introductorio a Meta Prophet para Ingeniería Industrial**

## **Introducción a la Predicción de Series de Tiempo con Prophet**

Así como Pandas nos ayuda a analizar y manipular datos estructurados, Prophet, desarrollado por Facebook (Meta), es una herramienta poderosa para la predicción de series de tiempo. Es particularmente útil para series de tiempo con fuertes patrones estacionales y efectos de días festivos, lo cual es común en muchos contextos de Ingeniería Industrial (demanda de productos, consumo de energía, etc.).

En este tutorial, utilizaremos nuestros conocimientos de Pandas para preparar los datos para Prophet y luego interpretar las predicciones.

## **Instalación**

Primero, asegúrate de tener instalada la librería `prophet`. Puedes instalarla usando pip:

```bash
pip install prophet
```

También necesitaremos `pandas` y `matplotlib`:

```bash
pip install pandas matplotlib
```

## **Preparación de los Datos**

Prophet espera un DataFrame con dos columnas específicas:

* **`ds`**: La columna de la marca de tiempo (debe ser en formato `YYYY-MM-DD` para datos diarios, o `YYYY-MM-DD HH:MM:SS` para datos horarios, etc.).
* **`y`**: La columna de la métrica que queremos predecir (debe ser numérica).

Vamos a crear algunos datasets de ejemplo usando Pandas, inspirados en los datos de producción que vimos antes.

## **Dataset de Ejemplo 1: Demanda Diaria de un Producto**

Imaginemos que tenemos datos de la demanda diaria de un producto durante un período de tiempo.

```python
import pandas as pd
import numpy as np
from prophet import Prophet
import matplotlib.pyplot as plt

# Generamos un rango de fechas
fechas_demanda = pd.date_range('2024-01-01', periods=100, freq='D')

# Generamos datos de demanda con alguna tendencia y estacionalidad semanal
tendencia = np.linspace(100, 150, 100)
estacionalidad_semanal = 20 * np.sin(2 * np.pi * fechas_demanda.dayofweek / 7)
ruido = np.random.normal(0, 10, 100)
demanda = tendencia + estacionalidad_semanal + ruido

# Creamos el DataFrame para Prophet
df_demanda = pd.DataFrame({'ds': fechas_demanda, 'y': demanda})

print(df_demanda.head())
```

En este dataset, `ds` representa la fecha y `y` representa la cantidad demandada del producto. Hemos introducido una tendencia lineal y una estacionalidad semanal simulada.

## **Dataset de Ejemplo 2: Producción Horaria de una Máquina**

Consideremos ahora datos de la producción horaria de una máquina, con posibles fluctuaciones diarias.

```python
# Generamos un rango de fechas y horas
fechas_produccion = pd.date_range('2024-01-01 00:00:00', periods=24 * 30, freq='H') # 30 días de datos horarios

# Generamos datos de producción con un patrón diario
patron_diario = 10 * np.sin(2 * np.pi * fechas_produccion.hour / 24) + 50
ruido_horario = np.random.normal(0, 5, 24 * 30)
produccion = patron_diario + ruido_horario

# Creamos el DataFrame para Prophet
df_produccion = pd.DataFrame({'ds': fechas_produccion, 'y': produccion})

print(df_produccion.head())
```

Aquí, `ds` tiene la fecha y la hora, y `y` representa la cantidad producida por hora. Hemos simulado un patrón diario sinusoidal.

## **Entrenamiento del Modelo Prophet**

Una vez que tenemos nuestros datos en el formato correcto, podemos instanciar y entrenar el modelo Prophet.

```python
# Inicializamos el modelo
modelo_demanda = Prophet()

# Entrenamos el modelo con el DataFrame de demanda
modelo_demanda.fit(df_demanda)

# Inicializamos y entrenamos el modelo para la producción horaria
modelo_produccion = Prophet()
modelo_produccion.fit(df_produccion)
```

La función `fit()` es la que realiza el aprendizaje del modelo a partir de los datos históricos.

## **Realización de Predicciones**

Para hacer predicciones, necesitamos crear un DataFrame con las fechas futuras para las que queremos predecir.

```python
# Para la demanda diaria, vamos a predecir los próximos 30 días
futuro_demanda = modelo_demanda.make_future_dataframe(periods=30)
print(futuro_demanda.tail())

# Para la producción horaria, vamos a predecir las próximas 48 horas
futuro_produccion = modelo_produccion.make_future_dataframe(periods=48, freq='H')
print(futuro_produccion.tail())
```

`make_future_dataframe()` genera un DataFrame con las fechas futuras, incluyendo las fechas históricas. El argumento `periods` especifica cuántos períodos futuros queremos predecir, y `freq` indica la frecuencia ('D' para diario, 'H' para horario, etc.).

Ahora podemos usar el método `predict()` para obtener las predicciones.

```python
# Realizamos las predicciones para la demanda
prediccion_demanda = modelo_demanda.predict(futuro_demanda)
print(prediccion_demanda[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail())

# Realizamos las predicciones para la producción horaria
prediccion_produccion = modelo_produccion.predict(futuro_produccion)
print(prediccion_produccion[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail())
```

El DataFrame de predicción contiene varias columnas, siendo las más importantes:

* **`ds`**: La marca de tiempo para la que se realizó la predicción.
* **`yhat`**: La predicción (valor esperado).
* **`yhat_lower`**: El límite inferior del intervalo de confianza de la predicción.
* **`yhat_upper`**: El límite superior del intervalo de confianza de la predicción.

## **Visualización de las Predicciones**

Prophet tiene herramientas integradas para visualizar las predicciones.

```python
# Visualización de la predicción de la demanda
fig1 = modelo_demanda.plot(prediccion_demanda)
plt.title('Predicción de la Demanda Diaria')
plt.xlabel('Fecha')
plt.ylabel('Demanda')
plt.show()

# Visualización de los componentes de la predicción de la demanda (tendencia, estacionalidad semanal, etc.)
fig2 = modelo_demanda.plot_components(prediccion_demanda)
plt.show()

# Visualización de la predicción de la producción horaria
fig3 = modelo_produccion.plot(prediccion_produccion)
plt.title('Predicción de la Producción Horaria')
plt.xlabel('Fecha y Hora')
plt.ylabel('Producción')
plt.show()

# Visualización de los componentes de la predicción de la producción horaria
fig4 = modelo_produccion.plot_components(prediccion_produccion)
plt.show()
```

`plot()` muestra la predicción junto con los datos históricos. `plot_components()` descompone la predicción en sus diferentes componentes (tendencia, estacionalidad anual, semanal, diaria, efectos de días festivos, etc.), lo cual es muy útil para entender cómo el modelo está realizando las predicciones.

## **Conclusión**

Este tutorial introductorio te ha mostrado los pasos básicos para usar Meta Prophet: preparar los datos en un DataFrame con las columnas `ds` e `y`, instanciar y entrenar el modelo, hacer predicciones para fechas futuras y visualizar los resultados.

Prophet ofrece muchas más opciones de personalización, como el manejo de días festivos, la especificación de estacionalidades personalizadas y la incorporación de regresores externos. Anima a tus estudiantes a explorar la documentación de Prophet para profundizar en estas funcionalidades y aplicarlas a problemas más complejos en el contexto de la Ingeniería Industrial.

## **Ejercicios propuestos:**

1.  Carga un archivo CSV con datos de una serie de tiempo relevante para la Ingeniería Industrial (por ejemplo, datos de ventas mensuales, consumo de energía diario, tiempos de ciclo promedio semanales). Asegúrate de que tenga una columna de fecha y una columna numérica para la métrica.
2.  Prepara los datos para Prophet, renombrando las columnas si es necesario a `ds` e `y`.
3.  Entrena un modelo Prophet con estos datos y realiza una predicción para un horizonte futuro razonable.
4.  Visualiza la predicción y los componentes. ¿Qué tendencias y estacionalidades observas?
5.  Experimenta con diferentes períodos de predicción. ¿Cómo cambia el intervalo de confianza?
