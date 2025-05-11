# Tutorial Introductorio a Pandas para Ingenieros Industriales

## Introducción a las Estructuras de Datos

Pandas ofrece dos clases principales para manejar datos:

* **Series:** Es como una lista unidimensional con etiquetas. Imagina que tienes una lista de la producción diaria de una fábrica durante una semana. Con una Serie, puedes etiquetar cada día (Lunes, Martes, etc.) y acceder a la producción de un día específico fácilmente.

    ```python
    import pandas as pd
    import numpy as np

    # Ejemplo: Producción diaria (en unidades)
    produccion = pd.Series([100, 120, 110, 130, 115, 125, 120],
                           index=['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo'])
    print(produccion)
    ```

    En este ejemplo, `produccion` es una Serie donde cada día de la semana está etiquetado y asociado a su valor de producción.

* **DataFrame:** Es como una tabla con filas y columnas. Piensa en una hoja de cálculo donde puedes tener diferentes tipos de datos (números, texto, fechas) organizados. Por ejemplo, podrías tener un DataFrame con información de diferentes proveedores, incluyendo su nombre, tiempo de entrega promedio y costo por unidad.

    ```python
    # Ejemplo: Información de Proveedores
    proveedores = pd.DataFrame({
        'Nombre': ['Proveedor A', 'Proveedor B', 'Proveedor C'],
        'Tiempo_Entrega': [5, 7, 6],  # Días
        'Costo_Unidad': [10.50, 9.75, 11.00] #Dólares
    })
    print(proveedores)
    ```

    Aquí, `proveedores` es un DataFrame que organiza la información de cada proveedor en filas y columnas.

## Creación de Objetos

* **Series:**

    * Puedes crear una Serie a partir de una lista de valores. Pandas asignará automáticamente etiquetas numéricas (0, 1, 2, …) a cada valor.

        ```python
        s = pd.Series([1, 3, 5, np.nan, 6, 8])
        print(s)
        ```

        `np.nan` representa un valor faltante. En Ingeniería Industrial, esto podría representar un día sin datos de producción o un fallo en un sensor.

    * También puedes especificar las etiquetas (índices) al crear la Serie.

        ```python
        s = pd.Series([10, 20, 15], index=['Enero', 'Febrero', 'Marzo'])
        print(s)
        ```

        Esto es útil para datos con etiquetas significativas, como meses o nombres de máquinas.

* **DataFrame:**

    * Puedes crear un DataFrame a partir de un array de NumPy. Necesitarás especificar las etiquetas de las filas (índices) y las columnas.

        ```python
        fechas = pd.date_range('20230101', periods=6) #Genera un rango de fechas
        df = pd.DataFrame(np.random.randn(6, 4), index=fechas, columns=['A', 'B', 'C', 'D'])
        print(df)
        ```

        `np.random.randn(6, 4)` crea un array de 6x4 con números aleatorios. En un contexto de Ingeniería Industrial, esto podría representar mediciones de diferentes sensores a lo largo del tiempo.

    * Otra forma común es crear un DataFrame a partir de un diccionario de Python. Las claves del diccionario serán los nombres de las columnas, y los valores serán listas o Series con los datos de cada columna.

        ```python
        df2 = pd.DataFrame({
            'Material': ['Acero', 'Aluminio', 'Cobre', 'Acero'],
            'Costo_Kg': [2.5, 3.0, 4.0, 2.5],
            'Proveedor': pd.Categorical(['A', 'B', 'A', 'C']) #Tipo categórico para datos repetidos
        })
        print(df2)
        ```

        Esto es útil para datos con diferentes tipos, como nombres de materiales, costos y proveedores.

## Visualización de Datos

* Puedes ver las primeras filas de un DataFrame con `head()` y las últimas con `tail()`.

    ```python
    print(df.head()) #Muestra las primeras 5 filas
    print(df.tail(3)) #Muestra las últimas 3 filas
    ```

    Esto te permite inspeccionar rápidamente los datos.

* `index` y `columns` te dan las etiquetas de las filas y columnas, respectivamente.

    ```python
    print(df.index) #Muestra las fechas
    print(df.columns) #Muestra las columnas ('A', 'B', 'C', 'D')
    ```

* `to_numpy()` convierte el DataFrame a un array de NumPy.

    ```python
    print(df.to_numpy())
    ```

    Esto es útil para trabajar con los datos en otras librerías.

* `describe()` te da un resumen estadístico de los datos numéricos.

    ```python
    print(df.describe()) #Cuenta, media, desviación estándar, mínimo, máximo, etc.
    ```

    Esto es muy útil para entender la distribución de tus datos.

* `T` transpone el DataFrame (intercambia filas y columnas).

    ```python
    print(df.T)
    ```

* `sort_index()` ordena por etiquetas de filas o columnas, y `sort_values()` ordena por los valores de una columna.

    ```python
    print(df.sort_index(axis=1, ascending=False)) #Ordena las columnas alfabéticamente en reversa
    print(df.sort_values(by='B')) #Ordena por los valores de la columna 'B'
    ```

## Selección de Datos

Hay varias formas de acceder a los datos en un DataFrame:

* **Selección por etiqueta:** Puedes seleccionar una columna específica utilizando su nombre, como si fuera un atributo del DataFrame.

    ```python
    print(df['A']) #Selecciona la columna 'A'
    ```

    También puedes seleccionar varias columnas pasando una lista de nombres.

    ```python
    print(df[['A', 'C']]) #Selecciona las columnas 'A' y 'C'
    ```

* **Selección por posición:** Puedes usar la notación de slicing (`[:]`) para seleccionar filas por su posición numérica (índices).

    ```python
    print(df[0:3]) #Selecciona las filas desde la posición 0 hasta la 2 (sin incluir la 3)
    print(df['20230102':'20230104']) #Selecciona las filas con etiquetas de índice desde '20230102' hasta '20230104' (¡ojo! aquí sí se incluye el final)
    ```

* **Selección por etiqueta con `.loc`:** Esta es una forma más explícita y recomendada para seleccionar datos usando las etiquetas de las filas y columnas.

    ```python
    print(df.loc[fechas[0]]) #Selecciona la fila con la primera etiqueta de fecha
    print(df.loc[:, ['A', 'B']]) #Selecciona todas las filas y las columnas 'A' y 'B'
    print(df.loc['20230102':'20230104', ['A', 'B']]) #Selecciona un rango de filas y columnas
    print(df.loc['20230102', ['A', 'B']]) #Selecciona un valor específico por etiqueta de fila y columna
    print(df.loc[fechas[0], 'A']) #Otra forma de seleccionar un valor específico (más rápido para un solo valor)
    ```

* **Selección por posición con `.iloc`:** Similar a `.loc`, pero se utiliza para seleccionar por la posición numérica (índice) de las filas y columnas.

    ```python
    print(df.iloc[3]) #Selecciona la fila en la tercera posición (índice 3)
    print(df.iloc[3:5, 0:2]) #Selecciona las filas en las posiciones 3 y 4, y las columnas en las posiciones 0 y 1
    print(df.iloc[[1, 2, 4], [0, 2]]) #Selecciona filas y columnas específicas por posición
    print(df.iloc[1, 1]) #Selecciona el valor en la segunda fila y la segunda columna
    ```

* **Indexación booleana:** Puedes usar condiciones para seleccionar filas que cumplan con ciertos criterios.

    ```python
    print(df[df['A'] > 0]) #Selecciona las filas donde los valores de la columna 'A' son mayores que 0
    print(df[df > 0]) #Selecciona todos los valores mayores que 0 (los demás serán NaN)
    ```

    También puedes usar el método `.isin()` para filtrar por valores específicos dentro de una columna.

    ```python
    df2 = pd.DataFrame({
        'Material': ['Acero', 'Aluminio', 'Cobre', 'Acero', 'Bronce'],
        'Proveedor': ['A', 'B', 'A', 'C', 'B']
    })
    print(df2[df2['Material'].isin(['Acero', 'Cobre'])]) #Selecciona filas donde la columna 'Material' es 'Acero' o 'Cobre'
    ```

## Valores Faltantes

En datos del mundo real, es común encontrarse con valores faltantes. Pandas utiliza `np.nan` para representarlos.

* `.dropna()` elimina las filas que tienen valores faltantes.

    ```python
    df_con_nan = df.reindex(index=fechas[:4], columns=list(df.columns) + ['E'])
    df_con_nan.loc[:2, 'E'] = 1
    print(df_con_nan)
    print(df_con_nan.dropna(how='any')) #Elimina filas con *algún* valor faltante
    print(df_con_nan.dropna(how='all')) #Elimina filas donde *todos* los valores son faltantes
    ```

* `.fillna()` reemplaza los valores faltantes.

    ```python
    print(df_con_nan.fillna(value=0)) #Reemplaza los NaN con 0
    ```

* `.isna()` devuelve una máscara booleana donde `True` indica un valor faltante.

    ```python
    print(pd.isna(df_con_nan))
    ```

## Operaciones

Pandas facilita realizar operaciones con los datos.

* **Estadísticas:** Ya vimos `describe()`. Aquí tienes otras funciones útiles:

    ```python
    print(df.mean()) #Calcula la media de cada columna
    print(df.mean(axis=1)) #Calcula la media de cada fila
    ```

* **Aplicación de funciones:** Puedes aplicar funciones a los datos utilizando `apply()`.

    ```python
    print(df['A'].apply(np.cumsum)) #Calcula la suma acumulada de la columna 'A'
    print(df.apply(lambda x: x.max() - x.min())) #Aplica una función anónima para encontrar la diferencia entre el máximo y el mínimo de cada columna
    ```

* **Histogramas:** Puedes generar histogramas directamente desde Pandas.

    ```python
    import matplotlib.pyplot as plt
    plt.figure() #Crea una nueva figura para el gráfico
    df['A'].hist()
    plt.xlabel('Valor de A')
    plt.ylabel('Frecuencia')
    plt.title('Histograma de la Columna A')
    plt.show()
    ```

## Combinación de Datos

Pandas proporciona varias formas de combinar Series y DataFrames:

* **`concat()`:** Concatena objetos de Pandas a lo largo de un eje (filas o columnas).

    ```python
    df_concat = pd.concat([df[:3], df[3:]]) #Combina las primeras 3 filas con las siguientes
    print(df_concat)
    ```

* **`merge()`:** Similar a las operaciones de JOIN en SQL, combina DataFrames basados en una o más columnas en común.

    ```python
    izquierda = pd.DataFrame({'clave': ['foo', 'bar'], 'valor': [1, 2]})
    derecha = pd.DataFrame({'clave': ['foo', 'foo'], 'valor2': [4, 5]})
    print(pd.merge(izquierda, derecha, on='clave')) #Combina basado en la columna 'clave'
    ```

* **`groupby()`:** Permite agrupar filas basadas en los valores de una o más columnas y luego realizar operaciones agregadas (suma, media, etc.) en cada grupo.

    ```python
    df_agrupado = pd.DataFrame({
        'Departamento': ['Producción', 'Ventas', 'Producción', 'Ventas', 'Logística'],
        'Cantidad': [100, 50, 120, 60, 80]
    })
    print(df_agrupado.groupby('Departamento').sum()) #Suma la 'Cantidad' por cada 'Departamento'
    ```

## Entrada y Salida de Datos

Pandas puede leer y escribir datos en una variedad de formatos. Aquí nos centraremos en los más comunes para un ingeniero industrial: CSV y Excel.

* **CSV (Comma Separated Values):** Un formato de texto plano donde los valores están separados por comas. Es muy común para intercambiar datos.

    * **Leer desde un archivo CSV:** Usamos la función `pd.read_csv()`.

        ```python
        # Asumamos que tienes un archivo llamado 'datos_produccion.csv' con columnas como 'Fecha', 'Producto', 'Cantidad', 'Defectos'
        datos_produccion = pd.read_csv('datos_produccion.csv')
        print(datos_produccion.head())
        ```

        Puedes especificar varios parámetros al leer el CSV, como el separador (si no es coma), el encabezado (si la primera fila no son los nombres de las columnas), los índices, etc. Por ejemplo, si tu archivo usa punto y coma como separador:

        ```python
        # datos_produccion_semicolon.csv
        # Fecha;Producto;Cantidad;Defectos
        # 2023-01-01;A;100;5
        # 2023-01-01;B;150;2
        datos_produccion_semicolon = pd.read_csv('datos_produccion_semicolon.csv', sep=';')
        print(datos_produccion_semicolon.head())
        ```

    * **Escribir a un archivo CSV:** Usamos el método `.to_csv()`.

        ```python
        # Guardar el DataFrame 'df_agrupado' que creamos antes en un archivo CSV llamado 'resumen_produccion.csv'
        df_agrupado.to_csv('resumen_produccion.csv')

        # Puedes controlar si se guarda el índice o no
        df_agrupado.to_csv('resumen_produccion_sin_indice.csv', index=False)
        ```

* **Excel:** Un formato de hoja de cálculo ampliamente utilizado.

    * **Leer desde un archivo Excel:** Usamos la función `pd.read_excel()`. Necesitarás tener instalada la librería `openpyxl` (puedes instalarla con `pip install openpyxl`).

        ```python
        # Asumamos que tienes un archivo llamado 'datos_inventario.xlsx' con una hoja llamada 'Hoja1' y columnas como 'ID_Producto', 'Nombre', 'Cantidad_Stock', 'Precio_Unitario'
        datos_inventario = pd.read_excel('datos_inventario.xlsx', sheet_name='Hoja1')
        print(datos_inventario.head())

        # Puedes especificar la hoja por su índice (empezando desde 0)
        datos_inventario_hoja2 = pd.read_excel('datos_inventario.xlsx', sheet_name=1)
        print(datos_inventario_hoja2.head())
        ```

    * **Escribir a un archivo Excel:** Usamos el método `.to_excel()`. También necesitarás `openpyxl`.

        ```python
        # Guardar el DataFrame 'proveedores' en un archivo Excel llamado 'info_proveedores.xlsx' en la hoja 'Proveedores'
        proveedores.to_excel('info_proveedores.xlsx', sheet_name='Proveedores')

        # Puedes controlar si se guarda el índice
        proveedores.to_excel('info_proveedores_sin_indice.xlsx', sheet_name='Proveedores', index=False)
        ```

## Series de Tiempo

Cuando trabajamos con datos secuenciales en el tiempo, es crucial que Pandas entienda que el índice representa momentos en el tiempo. Ya hemos visto cómo crear un `DatetimeIndex` con `pd.date_range()`.

```python
fechas = pd.date_range('20240101', periods=10, freq='D') # 'D' indica frecuencia diaria
ts = pd.Series(np.random.randn(len(fechas)), index=fechas)
print(ts)
```

Aquí, `ts` es una Serie donde el índice son fechas. Podemos usar estas fechas para seleccionar datos de manera intuitiva.

* **Selección por fecha:**
¡Tienes toda la razón! Mil disculpas, se cortó la generación del Markdown. Aquí tienes la continuación y el final del tutorial completo en formato Markdown:

```markdown
    ```python
    print(ts['2024-01-05']) # Selecciona el valor para el 5 de enero de 2024
    print(ts['2024-01'])   # Selecciona todos los valores de enero de 2024
    ```

* **Slicing por rango de fechas:**

    ```python
    print(ts['2024-01-03':'2024-01-07']) # Selecciona el rango de fechas
    ```

Pandas ofrece varias funcionalidades específicas para series de tiempo:

* **Resampling:** Permite cambiar la frecuencia de los datos (por ejemplo, convertir datos diarios a semanales o mensuales).

    ```python
    # Resampleo a frecuencia semanal, tomando la suma de los valores de cada semana
    print(ts.resample('W').sum())

    # Resampleo a frecuencia mensual, tomando la media de los valores de cada mes
    print(ts.resample('M').mean())
    ```

    Las opciones de frecuencia son variadas: 'D' (diario), 'W' (semanal), 'M' (mensual), 'Q' (trimestral), 'A' (anual), 'H' (hora), 'T' o 'min' (minuto), 'S' (segundo), etc.

* **Ventanas móviles:** Permiten calcular estadísticas (media, suma, etc.) sobre una ventana de tiempo deslizante. Esto es útil para suavizar tendencias o identificar patrones.

    ```python
    # Calcula la media móvil de los últimos 3 días
    print(ts.rolling(window=3).mean())
    ```

* **Diferencias:** Útil para analizar la tasa de cambio de una serie temporal.

    ```python
    # Calcula la diferencia con el período anterior
    print(ts.diff())
    ```

* **Shift:** Desplaza los datos hacia adelante o hacia atrás en el tiempo.

    ```python
    # Desplaza los datos un día hacia adelante
    print(ts.shift(1))

    # Desplaza los datos un día hacia atrás
    print(ts.shift(-1))
    ```

**Ejemplo en Contexto de Ingeniería Industrial:**

Imagina que tienes datos de la demanda diaria de un producto:

```python
fechas_demanda = pd.date_range('20240101', periods=30, freq='D')
demanda = pd.Series(np.random.randint(50, 200, size=30), index=fechas_demanda)
print(demanda.head())

# Calcular la media móvil de la demanda semanal para suavizar las fluctuaciones diarias
demanda_semanal_media = demanda.rolling(window=7).mean()
print("\nMedia móvil semanal de la demanda:\n", demanda_semanal_media.tail())

# Resamplear la demanda a frecuencia mensual y obtener la demanda total del mes
demanda_mensual_total = demanda.resample('M').sum()
print("\nDemanda total mensual:\n", demanda_mensual_total)
```

## Introducción a Plotting en Python con Pandas

Pandas proporciona métodos convenientes para generar gráficos directamente desde Series y DataFrames, utilizando Matplotlib por debajo. Seaborn se construye sobre Matplotlib y ofrece una interfaz de más alto nivel con estilos visuales atractivos y gráficos estadísticos más avanzados.

**Conceptos Básicos de Graficación**

* **Figura (Figure):** Es la ventana o el lienzo completo donde se dibuja el gráfico. Puede contener uno o varios subgráficos.
* **Subgráfico (Axes):** Es una región individual dentro de una figura donde se realiza el trazado de los datos. Cada subgráfico tiene sus propios ejes (x e y), título, etiquetas, etc.
* **Ejes (Axes):** Son las líneas que marcan las escalas de los datos (eje x horizontal y eje y vertical).
* **Título (Title):** Una descripción del gráfico.
* **Etiquetas (Labels):** Textos que describen los ejes (eje x y eje y).
* **Leyenda (Legend):** Una guía que explica qué representa cada elemento del gráfico (por ejemplo, diferentes colores de líneas).
* **Tipos de gráficos comunes:**
    * **Gráfico de líneas (Line Plot):** Útil para mostrar tendencias a lo largo del tiempo o la relación entre dos variables continuas.
    * **Gráfico de barras (Bar Plot):** Útil para comparar valores entre diferentes categorías.
    * **Histograma (Histogram):** Útil para visualizar la distribución de una sola variable numérica.
    * **Gráfico de dispersión (Scatter Plot):** Útil para mostrar la relación entre dos variables numéricas y buscar correlaciones.
    * **Gráfico de caja (Box Plot):** Útil para visualizar la distribución de una variable numérica y detectar valores atípicos por categorías.

**Graficación con Pandas y Matplotlib**

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Ejemplo de Serie de tiempo (producción diaria)
fechas_produccion = pd.date_range('20240101', periods=30, freq='D')
produccion_diaria = pd.Series(np.random.randint(80, 150, size=30), index=fechas_produccion)

# Gráfico de líneas de la producción diaria
plt.figure(figsize=(10, 6)) # Define el tamaño de la figura
produccion_diaria.plot(kind='line', title='Producción Diaria') # 'kind' especifica el tipo de gráfico
plt.xlabel('Fecha')
plt.ylabel('Unidades Producidas')
plt.grid(True) # Agrega una cuadrícula al gráfico
plt.show()

# Ejemplo de DataFrame (comparación de costos por proveedor)
datos_costos = pd.DataFrame({
    'Proveedor': ['A', 'B', 'C', 'D'],
    'Costo_Promedio': [10.5, 9.8, 11.2, 10.1]
})

# Gráfico de barras de los costos promedio por proveedor
plt.figure(figsize=(8, 5))
datos_costos.plot(x='Proveedor', y='Costo_Promedio', kind='bar', title='Costo Promedio por Proveedor')
plt.xlabel('Proveedor')
plt.ylabel('Costo Promedio')
plt.xticks(rotation=0) # Rota las etiquetas del eje x si es necesario
plt.show()

# Ejemplo de DataFrame (distribución de tiempos de ciclo)
tiempos_ciclo = pd.DataFrame({'Tiempo': np.random.normal(loc=5, scale=1, size=100)})

# Histograma de los tiempos de ciclo
plt.figure(figsize=(8, 5))
tiempos_ciclo['Tiempo'].plot(kind='hist', bins=15, title='Distribución de Tiempos de Ciclo') # 'bins' define el número de barras
plt.xlabel('Tiempo (minutos)')
plt.ylabel('Frecuencia')
plt.show()
```

**Graficación con Seaborn**

```python
import seaborn as sns
import matplotlib.pyplot as plt

# Ejemplo de DataFrame (relación entre temperatura y rendimiento)
datos_rendimiento = pd.DataFrame({
    'Temperatura': np.random.uniform(20, 35, size=50),
    'Rendimiento': 50 + 2 * np.random.uniform(0, 1, size=50) * (35 - np.random.uniform(20, 35, size=50))
})

# Gráfico de dispersión con Seaborn
plt.figure(figsize=(8, 6))
sns.scatterplot(x='Temperatura', y='Rendimiento', data=datos_rendimiento)
plt.title('Relación entre Temperatura y Rendimiento')
plt.xlabel('Temperatura (°C)')
plt.ylabel('Rendimiento (%)')
plt.show()

# Ejemplo de DataFrame (comparación de la eficiencia de diferentes máquinas)
datos_eficiencia = pd.DataFrame({
    'Máquina': ['A'] * 30 + ['B'] * 30 + ['C'] * 30,
    'Eficiencia': np.concatenate([np.random.normal(85, 5, size=30),
                                  np.random.normal(90, 3, size=30),
                                  np.random.normal(88, 4, size=30)])
})

# Gráfico de caja con Seaborn
plt.figure(figsize=(8, 6))
sns.boxplot(x='Máquina', y='Eficiencia', data=datos_eficiencia)
plt.title('Comparación de Eficiencia por Máquina')
plt.xlabel('Máquina')
plt.ylabel('Eficiencia (%)')
plt.show()

# Histograma con Seaborn (con una estimación de densidad kernel)
plt.figure(figsize=(8, 5))
sns.histplot(datos_tiempos_ciclo['Tiempo'], kde=True) # 'kde=True' añade la estimación de densidad
plt.title('Distribución de Tiempos de Ciclo')
plt.xlabel('Tiempo (minutos)')
plt.ylabel('Frecuencia')
plt.show()

# Integración con Pandas
# Agrupar los datos de eficiencia por máquina y obtener la media
eficiencia_media = datos_eficiencia.groupby('Máquina')['Eficiencia'].mean().reset_index()

# Crear un gráfico de barras de la eficiencia media con Seaborn
plt.figure(figsize=(6, 4))
sns.barplot(x='Máquina', y='Eficiencia', data=eficiencia_media)
plt.title('Eficiencia Media por Máquina')
plt.xlabel('Máquina')
plt.ylabel('Eficiencia Media (%)')
plt.show()
```
