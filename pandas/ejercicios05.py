import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# ANÁLISIS DE DATOS INDUSTRIALES - VISUALIZACIÓN
print("\n" + "="*60)
print("SISTEMA DE VISUALIZACIÓN DE DATOS INDUSTRIALES")
print("="*60 + "\n")

## 1. CONFIGURACIÓN INICIAL
print("\n1. INICIALIZACIÓN DEL SISTEMA")
print("-"*50)
print("Configurando entorno de análisis...")
np.random.seed(1405)  # Establecemos semilla para reproducibilidad
print("✓ Semilla aleatoria configurada (1405)")
print("✓ Librerías cargadas correctamente")
print("✓ Entorno listo para análisis\n")

## 2. ANÁLISIS DE PRODUCCIÓN DIARIA
print("\n2. ANÁLISIS DE PRODUCCIÓN")
print("-"*50)
print("Generando datos de producción diaria para 30 días...")
fechas_produccion = pd.date_range('2024-01-01', periods=30, freq='D')
produccion_diaria = pd.Series(
    np.random.randint(80, 150, size=30),
    index=fechas_produccion,
    name="Producción"
)

print("\n2.1 Resumen estadístico de producción:")
print(produccion_diaria.describe())

print("\n2.2 Visualizando tendencia de producción...")
plt.figure(figsize=(12, 6))
produccion_diaria.plot(
    kind='line',
    title='Producción Diaria - Enero 2024',
    color='green',
    linewidth=2,
    marker='o'
)
plt.xlabel('Fecha')
plt.ylabel('Unidades Producidas')
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('produccion_diaria.png', dpi=300)
plt.show()
print("✓ Gráfico de producción guardado como 'produccion_diaria.png'")

## 3. COMPARATIVO DE COSTOS POR PROVEEDOR
print("\n\n3. ANÁLISIS DE COSTOS")
print("-"*50)
print("Generando datos comparativos de proveedores...")
datos_costos = pd.DataFrame({
    'Proveedor': ['A', 'B', 'C', 'D'],
    'Costo_Promedio': [10.5, 9.8, 11.2, 10.1],
    'Tiempo_Entrega': [3.2, 4.1, 2.9, 3.8]
})

print("\n3.1 Datos completos de proveedores:")
print(datos_costos)

print("\n3.2 Visualizando comparativo de costos...")
plt.figure(figsize=(10, 6))
ax = datos_costos.plot(
    x='Proveedor',
    y='Costo_Promedio',
    kind='bar',
    title='Comparación de Costos por Proveedor',
    color='skyblue',
    edgecolor='navy',
    alpha=0.8
)
plt.xlabel('Proveedor')
plt.ylabel('Costo Promedio (USD)')
plt.xticks(rotation=0)
plt.grid(axis='y', linestyle='--', alpha=0.6)

# Agregar valores encima de las barras
for p in ax.patches:
    ax.annotate(f"{p.get_height():.1f}", 
                (p.get_x() + p.get_width() / 2., p.get_height()),
                ha='center', va='center', 
                xytext=(0, 5), 
                textcoords='offset points')

plt.tight_layout()
plt.savefig('costo_promedio_proveedor.png', dpi=300)
plt.show()
print("✓ Gráfico de costos guardado como 'costo_promedio_proveedor.png'")

## 4. DISTRIBUCIÓN DE TIEMPOS DE CICLO
print("\n\n4. ANÁLISIS DE TIEMPOS")
print("-"*50)
print("Generando datos de tiempos de ciclo...")
tiempos_ciclo = pd.DataFrame({
    'Tiempo': np.random.normal(loc=5, scale=1, size=100)
})

print("\n4.1 Estadísticos de tiempos de ciclo:")
print(tiempos_ciclo.describe())

print("\n4.2 Visualizando distribución de tiempos...")
plt.figure(figsize=(10, 6))
tiempos_ciclo['Tiempo'].plot(
    kind='hist',
    bins=15,
    title='Distribución de Tiempos de Ciclo',
    color='purple',
    edgecolor='white',
    alpha=0.7
)
plt.xlabel('Tiempo (minutos)')
plt.ylabel('Frecuencia')
plt.grid(True, linestyle='--', alpha=0.5)

# Línea para la media
mean_val = tiempos_ciclo['Tiempo'].mean()
plt.axvline(mean_val, color='red', linestyle='dashed', linewidth=2)
plt.text(mean_val+0.1, plt.ylim()[1]*0.9, f'Media: {mean_val:.2f} min', color='red')

plt.tight_layout()
plt.savefig('distribucion_tiempos_ciclo.png', dpi=300)
plt.show()
print("✓ Gráfico de tiempos guardado como 'distribucion_tiempos_ciclo.png'")

print("\n" + "="*60)
print("ANÁLISIS COMPLETADO EXITOSAMENTE")
print("="*60)