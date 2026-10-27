import logging
from src.config import LOGS_DIR

def obtener_logger(nombre: str) -> logging.Logger:
    """Configura y devuelve un logger con salida a consola y archivo de texto."""
    logger = logging.getLogger(nombre)
    logger.setLevel(logging.INFO)

    if not logger.handlers:
        # Formato de los mensajes de log
        formatter = logging.Formatter(
            "%(asctime)s [%(levelname)s] [%(name)s]: %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )

        # Handler para Consola
        stream_handler = logging.StreamHandler()
        stream_handler.setFormatter(formatter)
        logger.addHandler(stream_handler)

        # Handler para Archivo
        file_handler = logging.FileHandler(LOGS_DIR / "ejecucion.log", encoding="utf-8")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger