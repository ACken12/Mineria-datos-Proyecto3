import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from ipywidgets import widgets, interact

 


def univariate_analysis(df):
    """
    Realiza análisis univariado del DataFrame con navegación paginada entre gráficos.
    """
    print("\n=== Análisis Univariado ===")
    figures = []  # Lista para almacenar las figuras
    
    # Análisis de variables numéricas
    numerical_cols = df.select_dtypes(include=[np.number]).columns
    if len(numerical_cols) > 0:
        for col in numerical_cols:
            # Crear histograma
            fig1, ax1 = plt.subplots(figsize=(10, 6))
            sns.histplot(data=df, x=col, kde=True, ax=ax1)
            ax1.set_title(f"Distribución de {col}")
            figures.append(fig1)
            
            # Crear diagrama de caja
            fig2, ax2 = plt.subplots(figsize=(10, 6))
            sns.boxplot(data=df, x=col, ax=ax2)
            ax2.set_title(f"Diagrama de caja de {col}")
            figures.append(fig2)
    
    # Análisis de variables categóricas
    categorical_cols = df.select_dtypes(exclude=[np.number]).columns
    if len(categorical_cols) > 0:
        for col in categorical_cols:
            # Crear gráfico de barras
            fig, ax = plt.subplots(figsize=(10, 6))
            sns.countplot(data=df, x=col, ax=ax)
            ax.set_title(f"Distribución de {col}")
            plt.xticks(rotation=45)
            figures.append(fig)
    
    # Función para mostrar una figura específica
    def display_figure(index):
        for fig in figures:  # Cerrar todas las figuras anteriores
            plt.close(fig)
        figures[index].show()  # Mostrar figura seleccionada
    
    # Crear slider interactivo
    interact(display_figure, index=widgets.IntSlider(min=0, max=len(figures) - 1, step=1, description="Página"))