import sys
import time
from src.config import DATA_PATH
from src.carga import cargar_y_validar_datos
from src.visualizaciones import generar_boxplot_gasto, generar_tendencia_mensual
from src.reporte import exportar_informe_excel
from src.logger import obtener_logger

logger = obtener_logger("PipelineMain")

def ejecutar_pipeline():
    inicio = time.time()
    logger.info("========================================")
    logger.info("INICIANDO PIPELINE DE ANÁLISIS DE DATOS")
    logger.info("========================================")

    try:
        # 1. Carga y validación
        df = cargar_y_validar_datos(DATA_PATH)

        # 2. Generación de Visualizaciones
        generar_boxplot_gasto(df)
        generar_tendencia_mensual(df)

        # 3. Exportación de Informe
        exportar_informe_excel(df)

        tiempo_total = time.time() - inicio
        logger.info("========================================")
        logger.info("PIPELINE FINALIZADO EN %.2f SEGUNDOS", tiempo_total)
        logger.info("========================================")

    except Exception as e:
        logger.error("Error crítico durante la ejecución del pipeline: %s", str(e), exc_info=True)
        sys.exit(1)

if __name__ == "__main__":
    ejecutar_pipeline()