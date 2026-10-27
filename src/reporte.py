from pathlib import Path
import pandas as pd
from src.config import INFORMES_DIR
from src.logger import obtener_logger

logger = obtener_logger("Reporte")

def exportar_informe_excel(df: pd.DataFrame) -> Path:
    """Exporta agregaciones y estadísticos ejecutivos a un libro de Excel."""
    resumen_alojamiento = df.groupby("tipo_alojamiento").agg(
        gasto_promedio=("gasto_diario", "mean"),
        estancia_promedio=("duracion_estancia", "mean"),
        total_registros=("valoracion", "count")
    ).reset_index()

    ruta_salida = INFORMES_DIR / "informe_ejecutivo.xlsx"

    with pd.ExcelWriter(ruta_salida, engine="openpyxl") as writer:
        resumen_alojamiento.to_excel(writer, sheet_name="Resumen Alojamiento", index=False)
        df.describe().to_excel(writer, sheet_name="Estadísticas Generales")

    logger.info("Informe Excel generado en: %s", ruta_salida)
    return ruta_salida