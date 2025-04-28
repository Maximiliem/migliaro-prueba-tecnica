
# 📊 Informe Prueba Técnica Migliaro

Este proyecto procesa el archivo Excel **`Balancete Maxi Bertta.xlsx`**, realiza un análisis financiero detallado y genera tableros/tablas organizados por tipo de gasto. El objetivo es facilitar la interpretación de los datos para contadores y otros usuarios.

---

## 📋 Contenido

- [📝 Descripción del Proyecto](#-descripción-del-proyecto)
- [📁 Estructura del Proyecto](#-estructura-del-proyecto)
- [⚙️ Instrucciones de Uso](#️-instrucciones-de-uso)
- [📈 Resultados Generados](#-resultados-generados)
- [🧰 Requisitos y Dependencias](#-requisitos-y-dependencias)
- [🙌 Créditos](#-créditos)

---

## 📝 Descripción del Proyecto

El proyecto analiza un archivo Excel que contiene información sobre:

- Saldos deudores y acreedores
- En moneda nacional (M/N) y dólares (U$S)
- Agrupados por **rubros** y **categorías** (ej: Ingresos, Gastos Ganaderos, Gastos Agrícolas, etc.)

### 📌 Qué se genera:
- Un archivo .csv para poder manejar los datos de mejor manera en algún dashboard interactivo como pueda ser Tableau, Google Looker Studio, Power BI, entre otras herramientas posibles de análisis de datos.

---

## 📁 Estructura del Proyecto

```
migliaro-prueba-tecnica/
│
├── app.py                         # Script principal: orquesta todo el proceso.
├── analisis.py                    # Funciones para procesar y analizar los datos.
├── data/                          # Carpeta para datos de entrada y salida.
│   ├── Balancete Maxi Bertta.xlsx       # Archivo Excel original.
│   └── Balancete_Maxi_Bertta_limpio.csv     # Resultado procesado.
└── README.md                      # Documentación del proyecto.
```

---

## ⚙️ Instrucciones de Uso

### 🔧 Paso 1: Instalar dependencias

```bash
pip install pandas xlsxwriter
# o alternativamente:
pip install pandas openpyxl
```

### 📥 Paso 2: Colocar el archivo Excel

Guarda el archivo `Balancete Maxi Bertta.xlsx` en la carpeta `/data`.

### 🚀 Paso 3: Ejecutar el script

```bash
python app.py
```

Esto generará un archivo CSV llamado `Balancete_Maxi_Bertta_limpio.csv` dentro de la carpeta `/data`.

---

## 📈 Resultados Generados

El archivo `Balancete_Maxi_Bertta_limpio.csv` contiene los datos del Excel pero en formato .csv.

---

## 🧰 Requisitos y Dependencias

### ✅ Requisitos:
- Python 3.6 o superior
- Librerías:
  - `pandas`
  - `xlsxwriter` (o `openpyxl` como alternativa)

### 📦 Instalación rápida:
```bash
pip install pandas xlsxwriter
```

---

## 🙌 Créditos

Este proyecto fue desarrollado por **Maximiliano Bertta Borges** como parte de la prueba técnica para **Migliaro**.

📬 *¿Preguntas o sugerencias? No dudes en contactarme. maxibertta@gmail.com*

---
