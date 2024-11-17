# src/services/data_loader.py
import pandas as pd

def load_dataset(url):
    """Carga el dataset desde una URL y devuelve un DataFrame de pandas."""
    try:
        df = pd.read_csv(url)
        print("Dataset cargado con éxito")
        return df
    except Exception as e:
        print(f"Error al cargar el dataset: {e}")
        return None

