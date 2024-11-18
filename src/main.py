from services.data_loader import load_and_clean_dataset
from analysis import perform_analysis

def main():
    url = "https://github.com/ACken12/Mineria-datos-Proyecto3/blob/main/csv/datos.csv"
    df_limpio, df_original, encoders = load_and_clean_dataset(url)
    
    if df_limpio is not None:
        # Mostrar algunos datos de muestra del resultado
        print("\n=== Muestra de datos procesados ===")
        perform_analysis(df_limpio)
       

if __name__ == "__main__":
    main()