from services.data_loader import load_dataset
from services.data_loader import clean_dataset
from visualizations.analysis import perform_analysis
import sys
import os

def suppress_output(func, *args, **kwargs):
    """Suprime temporalmente la salida estándar mientras se ejecuta una función."""
    original_stdout = sys.stdout
    sys.stdout = open(os.devnull, 'w')
    try:
        return func(*args, **kwargs)  # Ejecución normal
    except Exception as e:
        # Restaurar stdout para mostrar errores
        sys.stdout.close()
        sys.stdout = original_stdout
        print(f"Error en la función '{func.__name__}': {e}")
        raise  # Relanzar el error para que el programa sepa que falló
    finally:
        # Restaurar la salida estándar al final
        if sys.stdout != original_stdout:
            sys.stdout.close()
            sys.stdout = original_stdout


def main():
    url = "https://github.com/ACken12/Mineria-datos-Proyecto3/blob/main/csv/datos.csv"
    # Suprimir cualquier impresión de load_dataset
    df_limpio, df_original, encoders = load_dataset(url)
    
    # Asegurarte de que no se imprima nada en clean_dataset
    df_limpio, df_original, encoders = suppress_output(clean_dataset, df_limpio)

    if df_limpio is not None:
        # Mostrar algunos datos de muestra del resultados
        perform_analysis(df_limpio,df_original)

       

if __name__ == "__main__":
    main()