import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from visualizations.botsplox import firtsbox,secondbox
from visualizations.histograms import firtshist,secondhist


def univariate_analysis(df):
    """
    Realiza análisis univariado del DataFrame y organiza los gráficos en una cuadrícula con 3 gráficos por fila.
    """
    print("\n=== Análisis Univariado ===")

   # Análisis de variables numéricas
    numerical_cols = df.select_dtypes(include=[np.number]).columns
    if len(numerical_cols) > 0:
        print("\nPágina 1: Histogramas y KDE (Primera mitad)")
        
        # Dividir las columnas numéricas en dos grupos
        mid_index = len(numerical_cols) // 2
        first_half = numerical_cols[:mid_index]
        second_half = numerical_cols[mid_index:]

        firtshist(first_half,df) # Primeros Graficos
        
        print("\nPágina 2: Histogramas y KDE (Segunda mitad)")

        secondhist(second_half,df)

        print("\nPágina 2: Diagramas de Caja (Primera mitad)")
        
        firtsbox(first_half,df)
        
        print("\nPágina 2: Diagramas de Caja (Segunda mitad)")
      
        secondbox(second_half,df)


    # Análisis de variables categóricas
    categorical_cols = df.select_dtypes(include=[np.number]).columns
    if len(categorical_cols) > 0:
        print("\nPágina 3: Gráficos de Barras")
        
        # Configuración del grid (3 gráficos por fila)
        rows = (len(categorical_cols) + 2) // 3
        fig, axes = plt.subplots(rows, 3, figsize=(18, 6 * rows))
        axes = axes.flatten()
        
        # Crear gráficos de barras
        for i, col in enumerate(categorical_cols):
            sns.countplot(data=df, x=col, ax=axes[i])
            axes[i].set_title(f"Diagrama de caja de {col}")
        
        # Ocultar ejes adicionales si hay menos gráficos que celdas
        for j in range(i + 1, len(axes)):
            axes[j].axis("off")
        
        plt.subplots_adjust(wspace=0.4, hspace=0.6) 
        plt.show()




