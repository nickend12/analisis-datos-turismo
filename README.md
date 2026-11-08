# 📊 EA2. Caso de Estudio: Análisis de los Diferentes Tipos de Datos

# Integrante

Oscar Javier Garcia

Este proyecto implementa un pipeline analítico profesional y modular en Python para procesar, auditar, visualizar y reportar datos de turismo y hospedaje (10,000 registros). Incluye un orquestador principal de procesos, pruebas unitarias automatizadas y un dashboard web interactivo desarrollado con Streamlit.

---

## 📁 Estructura del Proyecto

```text
analisis diferentes tipos datos/
├── datos/
│   └── datos_procesados_turismo.csv      # Dataset principal (10,000 registros)
├── output/
│   ├── graficos/
│   │   ├── vis1_gasto_alojamiento_box.png # Visualización estática (Seaborn)
│   │   └── vis2_tendencia_mensual.html    # Visualización interactiva (Plotly)
│   ├── informes/
│   │   ├── informe_ejecutivo.xlsx         # Resumen ejecutivo y estadísticos
│   │   ├── reporte_errores_datos.xlsx     # Auditoría de calidad de datos
│   │   └── reporte_fallas_sistema.txt     # Log resumido de fallas de ejecución
│   └── logs/
│       └── ejecucion.log                  # Registro de auditoría con timestamps
├── src/
│   ├── __init__.py
│   ├── config.py                          # Configuración centralizada de rutas
│   ├── logger.py                          # Sistema logging central
│   ├── carga.py                           # Carga y validación de esquema
│   ├── visualizaciones.py                 # Generación automática de gráficos
│   ├── reporte.py                         # Exportación a Excel
│   └── reporte_errores.py                 # Auditoría de inconsistencias y fallas
├── tests/
│   ├── __init__.py
│   └── test_pipeline.py                   # Pruebas unitarias (pytest)
├── app.py                                 # Dashboard Web Interactivo (Streamlit)
├── main.py                                # Orquestador principal del pipeline
├── pytest.ini                             # Configuración de rutas para Pytest
├── requirements.txt                       # Librerías y dependencias
└── README.md                              # Documentación general del proyecto
```

---

## 📈 Visualizaciones Generadas

## 🔎 Investigación y selección de herramientas

Para desarrollar esta actividad se revisaron tres herramientas de visualización de datos populares:

| Herramienta | Características principales | Ventajas | Limitaciones |
|---|---|---|---|
| **Tableau** | Plataforma especializada en análisis visual y creación de dashboards mediante una interfaz de arrastrar y soltar. | Permite construir paneles interactivos con rapidez, conectar múltiples fuentes y compartir resultados. | Algunas funciones avanzadas requieren licencia y su uso depende de una herramienta externa al entorno de desarrollo del proyecto. |
| **Power BI** | Plataforma de Microsoft para integrar datos, crear modelos, medidas y reportes interactivos. | Buena integración con Excel y otros productos de Microsoft, además de opciones de publicación y colaboración. | La experiencia completa depende del ecosistema Microsoft y ciertas funciones requieren licencia o configuración adicional. |
| **Python** | Lenguaje de programación que permite analizar datos y generar visualizaciones mediante bibliotecas como Matplotlib, Seaborn y Plotly. | Es flexible, reproducible, automatizable y está disponible gratuitamente. Facilita conectar la carga, validación, análisis, visualización y generación de informes en un mismo flujo. | Requiere conocimientos de programación y la construcción de dashboards puede demandar más trabajo inicial que una herramienta de arrastrar y soltar. |

### Herramienta seleccionada

Se seleccionó **Python** porque el conjunto de datos contiene variables categóricas, numéricas y temporales que requieren limpieza, transformación y análisis antes de visualizarse. Además, Python permite ejecutar todo el proceso de forma reproducible a partir del archivo CSV, guardar los resultados y volver a generar los informes cuando cambien los datos.

La selección se relaciona con los objetivos de la actividad de la siguiente manera:

* **Comparar el gasto según el tipo de alojamiento y el motivo del viaje:** se utilizó **Seaborn**, sobre Matplotlib, para generar un diagrama de caja que permite observar la distribución, dispersión y posibles valores extremos del gasto diario.
* **Analizar la evolución temporal del gasto:** se utilizó **Plotly** para generar una línea interactiva con la tendencia mensual del gasto total. Esta alternativa facilita explorar los valores al pasar el cursor sobre el gráfico.
* **Procesar y resumir los datos:** se utilizó **pandas** para cargar el dataset, convertir la fecha, agrupar los registros y producir el informe ejecutivo en Excel.
* **Presentar el análisis de forma interactiva:** se incorporó **Streamlit** como dashboard web, con filtros por fecha, alojamiento y motivo de viaje.

La elección considera la complejidad del dataset, la necesidad de combinar visualizaciones estáticas e interactivas, la facilidad de automatización y la disponibilidad de las bibliotecas dentro del entorno virtual del proyecto.

### 1. Distribución del Gasto Diario por Alojamiento y Motivo de Viaje (Seaborn)
![Distribución de Gasto Diario](output/graficos/vis1_gasto_alojamiento_box.png)

> **Descripción:** Muestra la variabilidad y dispersión del gasto diario según el tipo de alojamiento (Hotel, Hostal, Cabaña, Departamento) segmentado por motivo de viaje (Negocios, Vacaciones, Familiar).

### 2. Tendencia Mensual de Gasto e Ingresos Totales (Plotly)
* **Archivo de salida:** `output/graficos/vis2_tendencia_mensual.html`
> **Descripción:** Gráfico temporal interactivo que permite explorar el comportamiento mensual acumulado del gasto total y la frecuencia de viajes. Puede abrirse con cualquier navegador web.

## 🎥 Video de presentación del proyecto

Enlace del video:
https://drive.google.com/file/d/1kdnEz0DhO_ZRTERdkA07a4UgoWEtB7NP/view?usp=sharing

---

## 🛠️ Requisitos Previos

* **Python 3.10+** (Probado y validado en Python 3.12)
* **PowerShell** / Terminal de comandos

---

## 🚀 Guía de Instalación

1. **Clonar el repositorio:**
   ```powershell
   git clone [https://github.com/tu-usuario/analisis-datos-turismo.git](https://github.com/tu-usuario/analisis-datos-turismo.git)
   cd "analisis diferentes tipos datos"
   ```

2. **Crear y activar el entorno virtual (PowerShell):**
   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```

3. **Instalar dependencias:**
   ```powershell
   pip install -r requirements.txt
   ```

---

## ⚙️ Modos de Ejecución

### Opción A: Ejecutar el Pipeline Completo (Consola y Reportes)
Procesa los datos, valida la calidad, genera gráficos en alta resolución y exporta los informes ejecutivos en Excel:

```powershell
python main.py
```

### Opción B: Iniciar el Dashboard Interactivo (Streamlit)
Despliega la aplicación web para realizar análisis exploratorio en tiempo real con filtros dinámicos, tarjetas KPI y descarga directa de reportes:

```powershell
python -m streamlit run app.py
```
> *El navegador abrirá automáticamente la dirección `http://localhost:8501`.*

### Opción C: Ejecutar Pruebas Automatizadas
Verifica la calidad y correcto funcionamiento de los módulos del proyecto:

```powershell
pytest
```

---

## 📄 Informes Generados en `output/`

* **`output/informes/informe_ejecutivo.xlsx`**: Resumen analítico por tipo de hospedaje y matriz descriptiva del dataset.
* **`output/informes/reporte_errores_datos.xlsx`**: Mapeo de inconsistencias de datos, nulos y valores fuera de rango.
* **`output/logs/ejecucion.log`**: Traza detallada de ejecución con marcas de tiempo y niveles de severidad (`INFO`, `WARNING`, `ERROR`).