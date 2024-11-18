from matplotlib.widgets import Button
from modules.univariate import univariate_analysis
from modules.bivariate import bivariate_analysis
from classes.VisualizerData import InteractiveVisualizer


def perform_analysis(df):
    """Realiza el análisis exploratorio completo con visualizaciones interactivas."""
    print("\n=== Iniciando Análisis Exploratorio de Datos ===")
    
    # Realizar análisis univariado y bivariado
    print("\n=== Análisis automático después de limpieza ===")

    print("\nAnálisis univariado:")
    univariate_analysis(df)

    print("\nAnálisis bivariado:")
    bivariate_analysis(df)
    # Iniciar visualizador interactivo

    print("\nIniciando visualizador interactivo...")
    visualizer = InteractiveVisualizer(df)
    
    return visualizer
