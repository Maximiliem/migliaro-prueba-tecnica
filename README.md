nforme Prueba Técnica Migliaro 

Este proyecto procesa el archivo Excel "Balancete Maxi Bertta.xlsx", realiza un análisis financiero detallado y genera tableros/tablas organizados por tipo de gasto. El objetivo es facilitar la interpretación de los datos para los contadores y otros usuarios. 
📋 Contenido 

    Descripción del Proyecto 
    Estructura del Proyecto 
    Instrucciones de Uso 
    Resultados Generados 
    Requisitos y Dependencias 
     

1. Descripción del Proyecto 

El proyecto analiza un archivo Excel que contiene información sobre saldos deudores y acreedores en moneda nacional y dólares, agrupados por rubros y categorías (ej: ingresos, gastos ganaderos, gastos agrícolas, etc.).  

Se generan tableros/tablas para cada tipo de gasto, mostrando: 

    Totales de saldos deudores y acreedores en moneda nacional y dólares.
    Listado de ítems dentro de cada tipo de gasto, ordenados de mayor a menor según el saldo más relevante (deudor o acreedor).
     

Esto permite identificar rápidamente los rubros más importantes y facilita la toma de decisiones. 
2. Estructura del Proyecto 

El proyecto está organizado en los siguientes archivos y carpetas: 
migliaro-prueba-tecnica/
│
├── app.py               # Script principal: Orquesta todo el proceso.
├── analisis.py          # Funciones para procesar y analizar los datos.
├── tableros.py          # Funciones para generar tableros/tablas.
├── data/                # Carpeta para datos de entrada y salida.
│   ├── Balancete Maxi Bertta.xlsx  # Archivo Excel original.
│   └── Tableros_por_Tipo_Gasto.xlsx  # Resultado procesado.
└── README.md            # Documentación del proyecto.

migliaro-prueba-tecnica/
│
├── app.py               # Script principal: Orquesta todo el proceso.
├── analisis.py          # Funciones para procesar y analizar los datos.
├── tableros.py          # Funciones para generar tableros/tablas.
├── data/                # Carpeta para datos de entrada y salida.
│   ├── Balancete Maxi Bertta.xlsx  # Archivo Excel original.
│   └── Tableros_por_Tipo_Gasto.xlsx  # Resultado procesado.
└── README.md            # Documentación del proyecto.
 
 
3. Instrucciones de Uso 
Paso 1: Instalar dependencias  

Antes de ejecutar el proyecto, asegúrate de instalar las dependencias necesarias. Ejecuta el siguiente comando: 
pip install pandas xlsxwriter

Si prefieres usar openpyxl en lugar de xlsxwriter, puedes instalarlo con:
pip install pandas openpyxl

Paso 2: Colocar el archivo Excel  

Coloca el archivo Balancete Maxi Bertta.xlsx en la carpeta data/. 
Paso 3: Ejecutar el script  

Ejecuta el script principal con el siguiente comando: 
python app.py

Esto generará un archivo Excel llamado Tableros_por_Tipo_Gasto.xlsx en la carpeta data/. 
4. Resultados Generados 

El archivo generado (Tableros_por_Tipo_Gasto.xlsx) contiene una hoja por tipo de gasto, con dos secciones: 

    Totales : 
        Resumen de saldos deudores y acreedores en moneda nacional y dólares.
         

    Ítems : 
        Listado de todos los ítems dentro de ese tipo de gasto, ordenados de mayor a menor según el saldo más relevante (deudor o acreedor).
         
     

5. Requisitos y Dependencias 
Requisitos  

    Python 3.6 o superior.
    Las siguientes librerías instaladas:
        pandas
        xlsxwriter (o openpyxl si prefieres usar otro motor).
         
     

Dependencias  

Para instalar todas las dependencias necesarias, ejecuta: 
pip install pandas xlsxwriter


🙌 Créditos 

Este proyecto fue desarrollado por Maximiliano Bertta Borges como parte de la prueba técnica para Migliaro. Si tienes preguntas o sugerencias, no dudes en contactarme. 