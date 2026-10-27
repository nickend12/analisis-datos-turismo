import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

from src.config import DATA_PATH
from src.carga import cargar_y_validar_datos
from src.reporte import exportar_informe_excel
from src.reporte_errores import auditoria_calidad_datos

# Configuración de la página
st.set_page_config(
    page_title="Dashboard Analítico de Viajes",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Dashboard Analítico de Turismo y Hospedaje")
st.markdown("---")

# Carga de datos con caché de Streamlit para optimizar rendimiento
@st.cache_data
def cargar_datos_cache():
    return cargar_y_validar_datos(DATA_PATH)

try:
    df = cargar_datos_cache()
except Exception as e:
    st.error(f"Error al cargar los datos: {e}")
    st.stop()

# ==========================================
# FILTROS EN BARRA LATERAL
# ==========================================
st.sidebar.header("🔍 Filtros de Análisis")

# Filtro por Rango de Fechas
fecha_min = df["fecha"].min().date()
fecha_max = df["fecha"].max().date()
rango_fechas = st.sidebar.date_input(
    "Selecciona el rango de fechas:",
    value=[fecha_min, fecha_max],
    min_value=fecha_min,
    max_value=fecha_max
)

# Filtro por Tipo de Alojamiento
alojamientos = ["Todos"] + sorted(list(df["tipo_alojamiento"].dropna().unique()))
alojamiento_sel = st.sidebar.selectbox("Tipo de Alojamiento:", alojamientos)

# Filtro por Motivo de Viaje
motivos = ["Todos"] + sorted(list(df["motivo_viaje"].dropna().unique()))
motivo_sel = st.sidebar.selectbox("Motivo de Viaje:", motivos)

# Aplicar filtros al DataFrame
df_filtrado = df.copy()

if len(rango_fechas) == 2:
    df_filtrado = df_filtrado[
        (df_filtrado["fecha"].dt.date >= rango_fechas[0]) & 
        (df_filtrado["fecha"].dt.date <= rango_fechas[1])
    ]

if alojamiento_sel != "Todos":
    df_filtrado = df_filtrado[df_filtrado["tipo_alojamiento"] == alojamiento_sel]

if motivo_sel != "Todos":
    df_filtrado = df_filtrado[df_filtrado["motivo_viaje"] == motivo_sel]

# ==========================================
# TARJETAS DE MÉTRICAS (KPIs)
# ==========================================
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total de Registros", f"{len(df_filtrado):,}")

with col2:
    gasto_prom = df_filtrado["gasto_diario"].mean() if not df_filtrado.empty else 0
    st.metric("Gasto Diario Promedio", f"${gasto_prom:,.2f}")

with col3:
    estancia_prom = df_filtrado["duracion_estancia"].mean() if not df_filtrado.empty else 0
    st.metric("Estancia Promedio", f"{estancia_prom:.1f} días")

with col4:
    valoracion_prom = df_filtrado["valoracion"].mean() if not df_filtrado.empty else 0
    st.metric("Valoración Promedio", f"{valoracion_prom:.2f} / 5.0")

st.markdown("---")

# ==========================================
# VISUALIZACIONES INTERACTIVAS
# ==========================================
tab1, tab2, tab3 = st.tabs(["📈 Tendencia Mensual", "📦 Distribución de Gasto", "📋 Datos e Informes"])

with tab1:
    st.subheader("Evolución del Gasto Total Mensual")
    if not df_filtrado.empty:
        df_mes = df_filtrado.set_index("fecha").resample("ME").agg({
            "gasto_diario": "sum",
            "duracion_estancia": "count"
        }).reset_index()

        fig_line = px.line(
            df_mes,
            x="fecha",
            y="gasto_diario",
            title="Gasto Total Acumulado por Mes",
            labels={"fecha": "Fecha", "gasto_diario": "Gasto ($)"},
            markers=True
        )
        st.plotly_chart(fig_line, use_container_width=True)
    else:
        st.warning("No hay datos disponibles para el filtro seleccionado.")

with tab2:
    st.subheader("Gasto Diario por Alojamiento y Motivo de Viaje")
    if not df_filtrado.empty:
        fig_box = px.box(
            df_filtrado,
            x="tipo_alojamiento",
            y="gasto_diario",
            color="motivo_viaje",
            title="Distribución Interactiva de Gasto Diario",
            labels={"tipo_alojamiento": "Tipo de Alojamiento", "gasto_diario": "Gasto Diario ($)"}
        )
        st.plotly_chart(fig_box, use_container_width=True)
    else:
        st.warning("No hay datos disponibles para el filtro seleccionado.")

with tab3:
    st.subheader("Exploración de Datos")
    st.dataframe(df_filtrado.head(100), use_container_width=True)

    st.markdown("### Generación y Descarga de Informes")
    col_report, col_audit = st.columns(2)

    with col_report:
        if st.button("📄 Generar Informe Ejecutivo (Excel)"):
            ruta_excel = exportar_informe_excel(df_filtrado)
            with open(ruta_excel, "rb") as file:
                st.download_button(
                    label="⬇️ Descargar Informe Excel",
                    data=file,
                    file_name="informe_ejecutivo.xlsx",
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                )

    with col_audit:
        if st.button("⚠️ Ejecutar Auditoría de Calidad"):
            ruta_errores = auditoria_calidad_datos(df_filtrado)
            st.success("Auditoría completada exitosamente.")
            with open(ruta_errores, "rb") as file:
                st.download_button(
                    label="⬇️ Descargar Reporte de Auditoría",
                    data=file,
                    file_name="reporte_errores_datos.xlsx",
                    mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                )