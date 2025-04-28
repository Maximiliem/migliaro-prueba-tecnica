import pandas as pd
from analisis import limpiar_datos

# Paso 1: Leer el Excel
df = pd.read_excel("data/Balancete Maxi Bertta.xlsx")

# Paso 2: Limpiar los datos
df_limpio = limpiar_datos(df)

# Paso 3: Guardar el archivo limpio en formato CSV
df_limpio.to_csv("data/Balancete_Maxi_Bertta_limpio.csv", index=False)

print("Archivo limpio guardado como 'Balancete_Maxi_Bertta_limpio.csv'")