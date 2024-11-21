import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from visualizations.boxplots import firtsbox,secondbox
from visualizations.histograms import firtshist,secondhist
from visualizations.barplots import first_bar,second_bar


def univariate_analysis(df):
    """
    Realiza análisis univariado del DataFrame y organiza los gráficos en una cuadrícula con 3 gráficos por fila.
    """
    print("\n=== Análisis Univariado ===")


    print("\nResumen general de las Estadísticas descriptivas:")
    print(df.describe())
    # Análisis de variables numéricas
    numerical_cols = df.select_dtypes(include=[np.number]).columns
    if len(numerical_cols) > 0:
        print("\nVariables Numéricas:")
        for col in numerical_cols:
            print(f"\nEstadísticas descriptivas para {col}:")
            stats = df[col].describe()
            print(stats)
            # Detectar asimetría y curtosis
            skewness = df[col].skew()
            kurtosis = df[col].kurtosis()
            print(f"Asimetría: {skewness:.2f}")
            print(f"Curtosis: {kurtosis:.2f}")

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
    categorical_cols = df.select_dtypes(include=['category']).columns  # Seleccionamos columnas categóricas
    if len(categorical_cols) > 0:
        print("\nPágina 3: Gráficos de Barras (Primera Parte)")
        
        # Dividimos las columnas en dos partes
        half = len(categorical_cols) // 2  # Dividimos por la mitad
        first_half = categorical_cols[:half]  # Primera mitad
        second_half = categorical_cols[half:]  # Segunda mitad
        
        first_bar(first_half,df)
        
        print("\nPágina 3: Gráficos de Barras (Segunda Parte)")
        
        second_bar(second_half,df)





