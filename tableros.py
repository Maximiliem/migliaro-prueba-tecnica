import pandas as pd

def generar_tableros(tipos_gasto):
    """
    Genera tableros/tablas para cada tipo de gasto y los guarda en un archivo Excel.
    Los números se muestran con exactamente dos decimales.
    """
    # Crear un Excel Writer para guardar todas las tablas en un solo archivo
    with pd.ExcelWriter("data/Tableros_por_Tipo_Gasto.xlsx", engine="xlsxwriter") as writer:
        for tipo_gasto, df_filtrado in tipos_gasto.items():
            # Redondear todos los valores numéricos a 2 decimales
            df_filtrado = df_filtrado.round({
                "SALDO DEUDOR M/N": 2,
                "SALDO ACREEDOR M/N": 2,
                "SALDO DEUDOR U$S": 2,
                "SALDO ACREEDOR U$S": 2
            })

            # Calcular totales (redondeados a 2 decimales)
            total_saldo_deudor_mn = round(df_filtrado["SALDO DEUDOR M/N"].sum(), 2)
            total_saldo_acreedor_mn = round(df_filtrado["SALDO ACREEDOR M/N"].sum(), 2)
            total_saldo_deudor_usd = round(df_filtrado["SALDO DEUDOR U$S"].sum(), 2)
            total_saldo_acreedor_usd = round(df_filtrado["SALDO ACREEDOR U$S"].sum(), 2)

            # Crear un DataFrame con los totales
            totales = pd.DataFrame({
                "Concepto": ["Total Saldo Deudor M/N", "Total Saldo Acreedor M/N",
                             "Total Saldo Deudor U$S", "Total Saldo Acreedor U$S"],
                "Monto": [total_saldo_deudor_mn, total_saldo_acreedor_mn,
                          total_saldo_deudor_usd, total_saldo_acreedor_usd]
            })

            # Decidir por qué columna ordenar
            if total_saldo_deudor_mn > total_saldo_acreedor_mn:
                columna_orden = "SALDO DEUDOR M/N"
                orden_ascendente = False  # De mayor a menor
            else:
                columna_orden = "SALDO ACREEDOR M/N"
                orden_ascendente = False  # De mayor a menor

            # Crear un DataFrame con los ítems ordenados por la columna seleccionada
            items_ordenados = df_filtrado[["NOMBRE", "SALDO DEUDOR M/N", "SALDO ACREEDOR M/N",
                                           "SALDO DEUDOR U$S", "SALDO ACREEDOR U$S"]]
            items_ordenados = items_ordenados.sort_values(by=columna_orden, ascending=orden_ascendente)

            # Guardar los totales en una hoja (con formato de dos decimales)
            totales.to_excel(writer, sheet_name=f"{tipo_gasto} - Totales", index=False, float_format="%.2f")

            # Guardar los ítems ordenados en otra hoja (con formato de dos decimales)
            items_ordenados.to_excel(writer, sheet_name=f"{tipo_gasto} - Items", index=False, float_format="%.2f")

    print("Tableros generados correctamente.")