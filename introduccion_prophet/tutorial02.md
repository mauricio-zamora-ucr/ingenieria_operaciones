# "tune up" o ajuste de hiperparámetros

Aquí te presento algunas de las formas más comunes de realizar un tune up al modelo Prophet:

## **1. Ajuste de la Sensibilidad a los Cambios de Tendencia (`changepoint_prior_scale`)**

* **Concepto:** Este parámetro controla la flexibilidad de la tendencia. Un valor más alto permite que la tendencia cambie más frecuentemente, mientras que un valor más bajo la hace más rígida.
* **Cuándo ajustarlo:** Si notas que la tendencia del modelo no se adapta lo suficientemente rápido a cambios reales en tus datos, o si la tendencia parece sobreajustarse a fluctuaciones aleatorias, este parámetro es un buen punto de partida.
* **Cómo ajustarlo:** Puedes probar diferentes valores de `changepoint_prior_scale`. Valores típicos suelen estar en el rango de 0.001 a 0.5. Puedes usar técnicas como la validación cruzada (que veremos más adelante) para encontrar el valor óptimo.

    ```python
    from prophet import Prophet
    import pandas as pd
    import numpy as np

    # (Asumimos que ya tienes tu DataFrame 'df_demanda')

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
    ```

## **2. Selección del Número y Ubicación de los Puntos de Cambio (`n_changepoints`, `changepoints`)**

* **Concepto:** Por defecto, Prophet coloca automáticamente un número de puntos de cambio potenciales al principio de la serie de tiempo. Puedes controlar el número (`n_changepoints`) y también especificar las fechas exactas de los puntos de cambio (`changepoints`).
* **Cuándo ajustarlo:** Si tienes conocimiento previo de eventos específicos que causaron cambios en la tendencia (por ejemplo, una nueva estrategia de marketing, un cambio en la cadena de suministro), puedes especificar esas fechas como puntos de cambio. Ajustar `n_changepoints` puede ser útil si el valor por defecto no parece adecuado para la complejidad de los cambios de tendencia en tus datos.
* **Cómo ajustarlo:**

    ```python
    # Ajustando el número de puntos de cambio
    m1 = Prophet(n_changepoints=10)
    m1.fit(df_demanda)
    future1 = m1.make_future_dataframe(periods=30)
    forecast1 = m1.predict(future1)
    fig1 = m1.plot(forecast1)
    plt.title('Modelo con 10 Puntos de Cambio')
    plt.show()

    # Especificando puntos de cambio exactos
    fechas_cambio = ['2024-03-01', '2024-05-01', '2024-07-01']
    m2 = Prophet(changepoints=fechas_cambio)
    m2.fit(df_demanda)
    future2 = m2.make_future_dataframe(periods=30)
    forecast2 = m2.predict(future2)
    fig2 = m2.plot(forecast2)
    plt.title('Modelo con Puntos de Cambio Específicos')
    plt.show()
    ```

## **3. Ajuste de la Fuerza de la Estacionalidad (`seasonality_prior_scale`)**

* **Concepto:** Este parámetro controla la flexibilidad de las estacionalidades (anual, semanal, diaria, etc.). Un valor más alto permite que las estacionalidades varíen más con el tiempo, mientras que un valor más bajo las fuerza a ser más consistentes.
* **Cuándo ajustarlo:** Si las estacionalidades en tus datos parecen cambiar significativamente a lo largo del tiempo, o si el modelo no está capturando bien la magnitud de las fluctuaciones estacionales, puedes ajustar este parámetro.
* **Cómo ajustarlo:** Similar a `changepoint_prior_scale`, puedes probar diferentes valores y usar validación cruzada. Valores típicos también suelen estar en el rango de 0.01 a 10.

    ```python
    # Probando diferentes valores de seasonality_prior_scale
    modelos_estacionalidad = {}
    valores_sps = [0.01, 0.1, 1.0, 10.0]

    for sps in valores_sps:
        m = Prophet(seasonality_prior_scale=sps)
        m.fit(df_demanda)
        future = m.make_future_dataframe(periods=30)
        forecast = m.predict(future)
        modelos_estacionalidad[sps] = forecast[['ds', 'yhat']]

    # (Visualización similar al ejemplo de changepoint_prior_scale)
    ```

## **4. Ajuste de la Fuerza de los Efectos de los Días Festivos (`holidays_prior_scale`)**

* **Concepto:** Si incluyes información sobre días festivos, este parámetro controla la flexibilidad con la que el modelo puede ajustar los efectos de estos días en la predicción.
* **Cuándo ajustarlo:** Si los efectos de los días festivos parecen demasiado suaves o demasiado pronunciados en la predicción, ajusta este parámetro.
* **Cómo ajustarlo:** Similar a los anteriores, prueba diferentes valores y usa validación cruzada.

## **5. Validación Cruzada para la Evaluación del Modelo y Ajuste de Hiperparámetros**

* **Concepto:** La validación cruzada es una técnica fundamental para evaluar el rendimiento de un modelo en datos no vistos y para comparar diferentes configuraciones de hiperparámetros. Prophet proporciona la función `cross_validation` para realizar esto.
* **Cómo usarla:** Necesitas definir un horizonte de predicción (`horizon`), un período inicial para comenzar el entrenamiento (`initial`), y un período para separar los conjuntos de entrenamiento y prueba (`period`).

    ```python
    from prophet.diagnostics import cross_validation
    from prophet.diagnostics import performance_metrics

    # Horizonte de predicción: 30 días
    horizon = '30 days'
    # Período inicial para comenzar la validación cruzada
    initial = '70 days'
    # Período entre cortes de validación cruzada
    period = '15 days'

    df_cv = cross_validation(modelo_demanda, initial=initial, period=period, horizon=horizon)
    print(df_cv.head())

    # Métricas de rendimiento
    df_p = performance_metrics(df_cv)
    print(df_p.head())
    ```

    Las métricas comunes para evaluar el rendimiento de la predicción incluyen el Error Absoluto Medio (MAE), el Error Cuadrático Medio (MSE), la Raíz del Error Cuadrático Medio (RMSE), el Error Absoluto Porcentual Medio (MAPE), y la Cobertura del Intervalo de Confianza (coverage).

* **Ajuste con Validación Cruzada:** Puedes usar la validación cruzada para probar diferentes combinaciones de hiperparámetros y seleccionar la que produce las mejores métricas de rendimiento en los datos de "prueba" generados durante la validación. Podrías usar un enfoque de búsqueda por cuadrícula (grid search) o búsqueda aleatoria (random search) para explorar el espacio de hiperparámetros.

    ```python
    from prophet import Prophet
    from prophet.diagnostics import cross_validation
    from prophet.diagnostics import performance_metrics
    import itertools

    param_grid = {
        'changepoint_prior_scale': [0.001, 0.01, 0.1, 0.5],
        'seasonality_prior_scale': [0.01, 0.1, 1.0, 10.0]
    }

    # Generar todas las combinaciones de parámetros
    all_params = [dict(zip(param_grid.keys(), v)) for v in itertools.product(*param_grid.values())]
    rmses = []

    # Realizar validación cruzada para cada combinación de parámetros
    for params in all_params:
        m = Prophet(**params)
        cv_results = cross_validation(m, initial=initial, period=period, horizon=horizon, parallel="processes")
        df_p = performance_metrics(cv_results, metrics=['rmse'])
        rmses.append(df_p['rmse'].values[0])

    # Encontrar los mejores parámetros
    best_rmse = min(rmses)
    best_params = all_params[np.argmin(rmses)]
    print(f"Mejor RMSE: {best_rmse}")
    print(f"Mejores parámetros: {best_params}")

    # Entrenar el modelo final con los mejores parámetros
    modelo_optimizado = Prophet(**best_params)
    modelo_optimizado.fit(df_demanda)
    future_opt = modelo_optimizado.make_future_dataframe(periods=30)
    forecast_opt = modelo_optimizado.predict(future_opt)
    fig_opt = modelo_optimizado.plot(forecast_opt)
    plt.title('Predicción con Modelo Optimizado')
    plt.show()
    ```

## **Consideraciones Adicionales:**

* **Conocimiento del Dominio:** Siempre es útil aplicar tu conocimiento del dominio al ajustar los parámetros. ¿Esperas cambios bruscos en la tendencia? ¿Son las estacionalidades muy variables?
* **Costo Computacional:** La validación cruzada, especialmente al probar muchas combinaciones de hiperparámetros, puede ser costosa computacionalmente.
* **Sobreajuste:** Ten cuidado de no sobreajustar el modelo a los datos históricos, lo que podría resultar en un mal rendimiento en datos futuros no vistos. La validación cruzada ayuda a mitigar este riesgo.

En resumen, el tune up de un modelo Prophet implica comprender el significado de sus hiperparámetros clave y utilizar técnicas de evaluación como la validación cruzada para encontrar la configuración que mejor se adapte a tus datos y objetivos de predicción. Anima a tus estudiantes a experimentar con estos parámetros y a observar cómo afectan las predicciones. ¡Es un proceso de aprendizaje iterativo!