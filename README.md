
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
- Totales de saldos por categoría
- Listado ordenado de ítems por impacto financiero

Esto permite **identificar rápidamente** los rubros más importantes y **facilita la toma de decisiones contables**.

---

## 📁 Estructura del Proyecto

```
migliaro-prueba-tecnica/
│
├── app.py                         # Script principal: orquesta todo el proceso.
├── analisis.py                    # Funciones para procesar y analizar los datos.
├── tableros.py                    # Funciones para generar tableros/tablas.
├── data/                          # Carpeta para datos de entrada y salida.
│   ├── Balancete Maxi Bertta.xlsx       # Archivo Excel original.
│   └── Tableros_por_Tipo_Gasto.xlsx     # Resultado procesado.
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

Esto generará un archivo Excel llamado `Tableros_por_Tipo_Gasto.xlsx` dentro de la carpeta `/data`.

---

## 📈 Resultados Generados

El archivo `Tableros_por_Tipo_Gasto.xlsx` contiene:

- 🧮 **Totales**:
  - Resumen de saldos deudores y acreedores (M/N y U$S)

- 📋 **Ítems**:
  - Lista detallada de cada ítem en el tipo de gasto correspondiente
  - Ordenados de mayor a menor según el saldo más relevante

Cada tipo de gasto aparece en una hoja independiente del Excel generado.

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

📬 *¿Preguntas o sugerencias? No dudes en contactarme.*

---
