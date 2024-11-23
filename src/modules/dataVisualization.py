from visualizations.barplots import plot_categorical_bars
from visualizations.lineplots import plot_line_trends
from visualizations.scatterplots import plot_dispersion_charts
from visualizations.boxplots import plot_density_charts

def data_visualization(df):
    """
    Realiza una Visualización de los datos del DataFrame
    """
    print("\n=== Visualización de los datos ===")
    print("\nResumen general de la Visualización de los datos:")
    print("\nGráficos de barras por categoria:")
    plot_categorical_bars(df)
    print("\nGráficos de lineas de datos temporales:")
    plot_line_trends(df)
    print("\Diagramas de dispersión de variables continuas:")
    plot_dispersion_charts(df)
    print("\Gráficos de densidad de los datos:")
    plot_density_charts(df)