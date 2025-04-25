import pandas as pd
from analisis import limpiar_datos, agrupar_por_tipo_gasto
from tableros import generar_tableros

# Paso 1: Leer el Excel
df = pd.read_excel("data/Balancete Maxi Bertta.xlsx")

# Paso 2: Limpiar los datos
df = limpiar_datos(df)

# Paso 3: Agrupar por tipo de gasto
tipos_gasto = agrupar_por_tipo_gasto(df)

# Paso 4: Generar tableros/tablas
generar_tableros(tipos_gasto)

print("Tableros generados y guardados en 'data/Tableros_por_Tipo_Gasto.xlsx'")