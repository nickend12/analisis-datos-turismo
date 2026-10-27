from pathlib import Path
import pandas as pd
from src.config import INFORMES_DIR, LOGS_DIR
from src.logger import obtener_logger

logger = obtener_logger("ReporteErrores")

def auditoria_calidad_datos(df: pd.DataFrame) -> Path:
    """Inspecciona el DataFrame en busca de anomalías en las filas y genera un reporte de errores de datos."""
    errores = []

    # 1. Chequeo de valores nulos
    filas_nulas = df[df.isnull().any(axis=1)]
    for idx, row in filas_nulas.iterrows():
        errores.append({
            "fila_index": idx,
            "tipo_error": "Valor Nulo / Faltante",
            "descripcion": f"Faltan datos en columnas: {list(row[row.isnull()].index)}"
        })

    # 2. Chequeo de rangos lógicos
    if "gasto_diario" in df.columns:
        gasto_invalido = df[df["gasto_diario"] <= 0]
        for idx in gasto_invalido.index:
            errores.append({
                "fila_index": idx,
                "tipo_error": "Rango Invalido",
                "descripcion": f"Gasto diario invalido: {df.loc[idx, 'gasto_diario']}"
            })

    if "duracion_estancia" in df.columns:
        estancia_invalida = df[df["duracion_estancia"] <= 0]
        for idx in estancia_invalida.index:
            errores.append({
                "fila_index": idx,
                "tipo_error": "Rango Invalido",
                "descripcion": f"Duracion de estancia invalida: {df.loc[idx, 'duracion_estancia']}"
            })

    # Guardar reporte si existen inconsistencias
    df_errores = pd.DataFrame(errores)
    ruta_salida = INFORMES_DIR / "reporte_errores_datos.xlsx"

    if not df_errores.empty:
        df_errores.to_excel(ruta_salida, index=False, sheet_name="Errores de Datos")
        logger.warning("Se encontraron %d anomalías de datos. Reporte guardado en: %s", len(df_errores), ruta_salida)
    else:
        # Crear reporte limpio indicando 0 errores
        pd.DataFrame([{"estado": "OK", "mensaje": "No se encontraron errores de calidad de datos."}]).to_excel(
            ruta_salida, index=False, sheet_name="Resumen"
        )
        logger.info("Auditoría de datos finalizada sin errores. Reporte guardado en: %s", ruta_salida)

    return ruta_salida


def extraer_reporte_ejecucion_log() -> Path:
    """Analiza el archivo de log de ejecución y consolida las fallas encontradas."""
    log_file = LOGS_DIR / "ejecucion.log"
    ruta_salida = INFORMES_DIR / "reporte_fallas_sistema.txt"

    if not log_file.exists():
        logger.warning("No se encontró el archivo de log para analizar.")
        return ruta_salida

    lineas_error = []
    with open(log_file, "r", encoding="utf-8") as file:
        for line in file:
            if "[ERROR]" in line or "[CRITICAL]" in line:
                lineas_error.append(line)

    with open(ruta_salida, "w", encoding="utf-8") as out:
        out.write("=== REPORTE DE ERRORES Y FALLAS DE EJECUCIÓN ===\n")
        out.write(f"Total de eventos con error detectados: {len(lineas_error)}\n\n")
        if lineas_error:
            out.writelines(lineas_error)
        else:
            out.write("No se registraron fallas o errores durante las ejecuciones analizadas.\n")

    logger.info("Reporte de fallas de ejecución generado en: %s", ruta_salida)
    return ruta_salida