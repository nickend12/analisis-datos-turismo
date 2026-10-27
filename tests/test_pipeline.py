import pytest
import pandas as pd
from src.config import DATA_PATH
from src.carga import cargar_y_validar_datos

def test_cargar_y_validar_datos():
    df = cargar_y_validar_datos(DATA_PATH)
    assert isinstance(df, pd.DataFrame)
    assert not df.empty
    assert "fecha" in df.columns
    assert pd.api.types.is_datetime64_any_dtype(df["fecha"])