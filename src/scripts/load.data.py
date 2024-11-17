from src.services.data_loader import load_dataset

# Ejecutar la carga de datos
if __name__ == "__main__":
    df = load_dataset('https://raw.githubusercontent.com/usuario/repositorio/main/dataset.csv')
    if df is not None:
        print("El dataset se cargó con éxito:")
        print(df.head())
    else:
        print("Hubo un error al cargar el dataset.")
