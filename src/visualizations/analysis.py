from matplotlib.widgets import Button
from modules.univariate import univariate_analysis
from modules.bivariate import bivariate_analysis
from modules.outliers import analyze_outliers
from hooks.handleOutliers import handle_outliers
from classes.VisualizerData import InteractiveVisualizer



def perform_analysis(df):
    """Realiza el análisis exploratorio completo con visualizaciones interactivas."""
    print("\n=== Iniciando Análisis Exploratorio de Datos ===")
    """
    """
    print("\nAnálisis univariado:")
    univariate_analysis(df)
    
    """"
 
    print("\nAnálisis bivariado:")
    bivariate_analysis(df)
    # Análisis de outliers
    print("\n=== Resumen de Outliers ===")
    outliers = analyze_outliers(df)
    
    # Tratar outliers
    df_cleaned = handle_outliers(outliers, method='iqr')
    
    print("\nIniciando visualizador interactivo...")
    visualizer = InteractiveVisualizer(df_cleaned)
    
    return visualizer
    """