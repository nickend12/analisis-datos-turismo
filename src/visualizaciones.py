from pathlib import Path
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns
import pandas as pd
from src.config import GRAFICOS_DIR
from src.logger import obtener_logger

logger = obtener_logger("Visualizaciones")

def generar_boxplot_gasto(df: pd.DataFrame) -> Path:
    """Genera y guarda el gráfico de caja sobre gasto diario."""
    plt.figure(figsize=(10, 6))
    sns.boxplot(
        data=df, 
        x="tipo_alojamiento", 
        y="gasto_diario", 
        hue="motivo_viaje"
    )
    plt.title("Distribución de Gasto Diario por Tipo de Alojamiento y Motivo")
    plt.tight_layout()

    ruta_salida = GRAFICOS_DIR / "vis1_gasto_alojamiento_box.png"
    plt.savefig(ruta_salida, dpi=300)
    plt.close()
    
    logger.info("Gráfico Seaborn guardado en: %s", ruta_salida)
    return ruta_salida

def generar_tendencia_mensual(df: pd.DataFrame) -> Path:
    """Genera y guarda el gráfico interactivo de tendencia mensual usando Plotly."""
    df_mes = df.set_index("fecha").resample("ME").agg({
        "gasto_diario": "sum",
        "duracion_estancia": "count"
    }).reset_index()

    fig = px.line(
        df_mes,
        x="fecha",
        y="gasto_diario",
        title="Tendencia Mensual del Gasto Total",
        labels={"fecha": "Fecha", "gasto_diario": "Gasto Total ($)"}
    )

    ruta_salida = GRAFICOS_DIR / "vis2_tendencia_mensual.html"
    fig.write_html(str(ruta_salida))
    
    logger.info("Gráfico Plotly guardado en: %s", ruta_salida)
    return ruta_salida