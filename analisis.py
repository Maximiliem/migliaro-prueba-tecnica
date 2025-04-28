def limpiar_datos(df):
    """
    Limpia los datos del DataFrame: elimina filas vacías, renombra columnas y convierte valores a números.
    """
    # Eliminar filas completamente vacías
    df = df.dropna(how="all")

    # Renombrar la columna sin nombre (columna 7) como "Tipo de Gasto"
    if "Unnamed: 7" in df.columns:
        df.rename(columns={"Unnamed: 7": "Tipo de Gasto"}, inplace=True)

    # Convertir columnas numéricas a números (eliminar comas y $)
    columnas_numericas = ["SALDO DEUDOR M/N", "SALDO ACREEDOR M/N", 
                          "SALDO DEUDOR U$S", "SALDO ACREEDOR U$S"]
    for columna in columnas_numericas:
        df[columna] = df[columna].replace(r'[\$,]', '', regex=True).astype(float)

    return df
