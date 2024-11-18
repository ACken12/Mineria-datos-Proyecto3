import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def bivariate_analysis(df):
    """
    Realiza análisis bivariado del DataFrame.
    """
    print("\n=== Análisis Bivariado ===")
    
    numerical_cols = df.select_dtypes(include=[np.number]).columns
    categorical_cols = df.select_dtypes(exclude=[np.number]).columns
    
    # Correlaciones entre variables numéricas
    if len(numerical_cols) > 1:
        print("\nCorrelaciones entre variables numéricas:")
        correlation_matrix = df[numerical_cols].corr()
        print(correlation_matrix)
        
        # Mapa de calor de correlaciones
        plt.figure(figsize=(10, 8))
        sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
        plt.title("Mapa de calor de correlaciones")
        plt.show()
        
        # Identificar correlaciones fuertes
        strong_correlations = []
        for i in range(len(correlation_matrix.columns)):
            for j in range(i):
                if abs(correlation_matrix.iloc[i, j]) > 0.7:
                    strong_correlations.append((
                        correlation_matrix.index[i],
                        correlation_matrix.columns[j],
                        correlation_matrix.iloc[i, j]
                    ))
        
        if strong_correlations:
            print("\nCorrelaciones fuertes detectadas (|r| > 0.7):")
            for var1, var2, corr in strong_correlations:
                print(f"{var1} - {var2}: {corr:.3f}")
                
                # Crear scatter plot para correlaciones fuertes
                plt.figure(figsize=(8, 6))
                sns.scatterplot(data=df, x=var1, y=var2)
                plt.title(f"Scatter plot: {var1} vs {var2}")
                plt.show()
