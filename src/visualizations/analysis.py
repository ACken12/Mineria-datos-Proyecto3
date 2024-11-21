from matplotlib.widgets import Button
from modules.univariate import univariate_analysis
from modules.bivariate import bivariate_analysis
from modules.dataVisualization import data_visualization
from modules.outliers import analyze_outliers
from hooks.handleOutliers import handle_outliers
from classes.DataProcessor import DataProcessor
import pandas as pd
import os

def clear_screen():
    """Limpia la pantalla de la consola."""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_menu():
    """Imprime el menú principal."""
    
    print("\n=== MENÚ DE ANÁLISIS DE DATOS ===")
    print("1. Realizar análisis univariado")
    print("2. Realizar análisis bivariado")
    print("3. Analizar outliers")
    print("4. Visualizar datos")
    print("5. Normalizar datos")
    print("0. Salir")
    print("================================")

def wait_for_user():
    """Espera a que el usuario presione Enter para continuar."""
    input("\nPresione Enter para continuar...")

def perform_analysis(df):
        """Maneja el menú interactivo para el análisis de datos."""
        while True:
            print_menu()
            option = input("\nSeleccione una opción (0-6): ")
            
            if option == "0":
                print("\n¡Hasta luego!")
                break
                
            elif option == "1":
                clear_screen()
                print("\n=== ANÁLISIS UNIVARIADO ===")
                univariate_analysis(df)
                wait_for_user()
                
            elif option == "2":
                clear_screen()
                print("\n=== ANÁLISIS BIVARIADO ===")
                bivariate_analysis(df)
                wait_for_user()
                
            elif option == "3":
                clear_screen()
                print("\n=== ANÁLISIS DE OUTLIERS ===")
                outliers = analyze_outliers(df)
                print("\n¿Desea manejar los outliers detectados?")
                print("1. Sí")
                print("2. No")
                handle_option = input("\nSeleccione una opción (1-2): ")
                
                if handle_option == "1":
                    df_cleaned = handle_outliers(outliers, method='iqr')
                    print("\nOutliers manejados exitosamente.")
                wait_for_user()
                
            elif option == "4":
                print("\n=== VISUALIZACIÓN DE DATOS ===")
                data_visualization(df)
                
            elif option == "5":
                print("\n=== NORMALIZACIÓN DE DATOS ===")
                processor = DataProcessor(df)
                datos_procesados = processor.process_data()
                
                print("\nDatos procesados (primeras 5 filas):")
                print(datos_procesados.head())
                
                print("\nEstadísticas de las transformaciones:")
                stats = processor.get_transformation_stats()
                for columna, estadisticas in stats.items():
                    print(f"\nColumna: {columna}")
                    for metrica, valor in estadisticas.items():
                        print(f"    {metrica}: {valor:.4f}")
                
                save_option = input("\n¿Desea guardar los datos normalizados? (s/n): ")
                if save_option.lower() == 's':
                    filename = input("Ingrese el nombre del archivo (default: 'datos_procesados.csv'): ")
                    if not filename:
                        filename = 'datos_procesados.csv'
                    datos_procesados.to_csv(filename, index=False)
                    print(f"\nDatos guardados en {filename}")
                wait_for_user()