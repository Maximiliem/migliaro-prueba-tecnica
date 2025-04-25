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
    df["SALDO DEUDOR M/N"] = df["SALDO DEUDOR M/N"].replace(r'[\$,]', '', regex=True).astype(float)
    df["SALDO ACREEDOR M/N"] = df["SALDO ACREEDOR M/N"].replace(r'[\$,]', '', regex=True).astype(float)
    df["SALDO DEUDOR U$S"] = df["SALDO DEUDOR U$S"].replace(r'[\$,]', '', regex=True).astype(float)
    df["SALDO ACREEDOR U$S"] = df["SALDO ACREEDOR U$S"].replace(r'[\$,]', '', regex=True).astype(float)

    return df


def agrupar_por_tipo_gasto(df):
    """
    Agrupa los datos por tipo de gasto y devuelve un diccionario con DataFrames separados por tipo.
    """
    # Obtener la lista de tipos de gasto únicos
    tipos_gasto = df["Tipo de Gasto"].dropna().unique()

    # Crear un diccionario para almacenar los DataFrames agrupados
    grupos = {}

    for tipo_gasto in tipos_gasto:
        grupos[tipo_gasto] = df[df["Tipo de Gasto"] == tipo_gasto]

    return grupos