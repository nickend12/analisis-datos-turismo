from pathlib import Path

# Rutas principales del proyecto
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "datos"
OUTPUT_DIR = BASE_DIR / "output"
GRAFICOS_DIR = OUTPUT_DIR / "graficos"
INFORMES_DIR = OUTPUT_DIR / "informes"
LOGS_DIR = OUTPUT_DIR / "logs"

# Crear carpetas si no existen
for folder in [GRAFICOS_DIR, INFORMES_DIR, LOGS_DIR]:
    folder.mkdir(parents=True, exist_ok=True)

# Archivo de entrada por defecto
FILE_NAME = "datos_procesados_turismo.csv"
DATA_PATH = DATA_DIR / FILE_NAME

# Columnas requeridas para validación
COLUMNAS_REQUERIDAS = [
    "fecha", "pais", "ciudad", "latitud", "longitud", 
    "tipo_alojamiento", "duracion_estancia", "gasto_diario", 
    "valoracion", "transporte", "motivo_viaje"
]