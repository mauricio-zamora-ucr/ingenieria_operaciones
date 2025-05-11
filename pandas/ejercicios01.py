import pandas as pd
import numpy as np


# Ejemplo: Producción diaria (en unidades)
produccion = pd.Series(
    [100, 120, 110, 130, 115, 125, 120],
    index=["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"],
)
print(produccion)


# Ejemplo: Información de Proveedores
proveedores = pd.DataFrame(
    {
        "Nombre": ["Proveedor A", "Proveedor B", "Proveedor C"],
        "Tiempo_Entrega": [5, 7, 6],  # Días
        "Costo_Unidad": [10.50, 9.75, 11.00],  # Dólares
    }
)
print(proveedores)
