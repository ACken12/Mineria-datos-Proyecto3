import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def univariate_analysis(df):
    """
    Realiza análisis univariado del DataFrame, detecta sesgo y aplica transformaciones si es necesario.
    """
    print("\n=== Análisis Univariado ===")
    
    # Análisis de variables numéricas
    numerical_cols = df.select_dtypes(include=[np.number]).columns
    if len(numerical_cols) > 0:
        print("\nVariables Numéricas:")
        for col in numerical_cols:
            print(f"\nEstadísticas para {col}:")
            stats = df[col].describe()
            print(stats)
            
            # Detectar asimetría y curtosis
            skewness = df[col].skew()
            kurtosis = df[col].kurtosis()
            print(f"Asimetría: {skewness:.2f}")
            print(f"Curtosis: {kurtosis:.2f}")
            
            # Comprobar sesgo y aplicar transformaciones si es necesario
            if abs(skewness) > 1:  # Sesgo alto, aplicar transformación
                print(f"Transformación aplicada a {col}: Logaritmo")
                df[col] = np.log1p(df[col])  # Aplicar logaritmo (log(1 + x))
                print(f"Nuevo sesgo para {col}: {df[col].skew():.2f}")
            
            # Crear y mostrar histograma
            plt.figure(figsize=(10, 6))
            sns.histplot(data=df, x=col, kde=True)
            plt.title(f"Distribución de {col}")
            plt.show()
            
            # Crear y mostrar diagrama de caja
            plt.figure(figsize=(10, 6))
            sns.boxplot(data=df, x=col)
            plt.title(f"Diagrama de caja de {col}")
            plt.show()
    
    # Análisis de variables categóricas
    categorical_cols = df.select_dtypes(exclude=[np.number]).columns
    if len(categorical_cols) > 0:
        print("\nVariables Categóricas:")
        for col in categorical_cols:
            print(f"\nDistribución de frecuencias para {col}:")
            freq = df[col].value_counts()
            print(freq)
            print(f"Número de categorías únicas: {df[col].nunique()}")
            
            # Crear y mostrar gráfico de barras
            plt.figure(figsize=(10, 6))
            sns.countplot(data=df, x=col)
            plt.xticks(rotation=45)
            plt.title(f"Distribución de {col}")
            plt.show()