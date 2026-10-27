from pathlib import Path
import pandas as pd
from src.config import COLUMNAS_REQUERIDAS
from src.logger import obtener_logger

logger = obtener_logger("CargaDatos")

def cargar_y_validar_datos(ruta_archivo: Path) -> pd.DataFrame:
    """Carga el dataset desde un archivo CSV y valida su consistencia básica.

    Args:
        ruta_archivo (Path): Ruta absoluta o relativa del CSV.

    Returns:
        pd.DataFrame: DataFrame procesado y validado.
    """
    if not ruta_archivo.exists():
        logger.error("El archivo no existe en la ruta: %s", ruta_archivo)
        raise FileNotFoundError(f"Archivo no encontrado: {ruta_archivo}")

    logger.info("Cargando archivo desde: %s", ruta_archivo)
    df = pd.read_csv(ruta_archivo)

    # Validar presencia de columnas esenciales
    columnas_faltantes = set(COLUMNAS_REQUERIDAS) - set(df.columns)
    if columnas_faltantes:
        msg = f"El archivo no contiene las columnas requeridas: {columnas_faltantes}"
        logger.error(msg)
        raise ValueError(msg)

    # Conversión de tipos de datos
    df["fecha"] = pd.to_datetime(df["fecha"])
    
    logger.info("Carga exitosa: %d filas y %d columnas.", df.shape[0], df.shape[1])
    return df