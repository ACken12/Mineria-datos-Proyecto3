
from services.data_loader import load_and_clean_dataset
from visualizations.analysis import perform_analysis
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats

def analyze_outliers(df):
    """
    Realiza análisis de outliers utilizando métodos Z-score e IQR.
    Se integra con el análisis exploratorio existente.
    """
    print("\n=== Análisis de Valores Atípicos (Outliers) ===")
    
    numerical_cols = df.select_dtypes(include=[np.number]).columns # Solo incluimos los valores númericos
    outliers_summary = {}
    
    for column in numerical_cols:
        # Calcular estadísticas
        Q1 = df[column].quantile(0.25)
        Q3 = df[column].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        
        # Detectar outliers por IQR
        outliers_iqr = df[(df[column] < lower_bound) | (df[column] > upper_bound)][column]
        
        # Detectar outliers por Z-score
        z_scores = np.abs(stats.zscore(df[column]))
        outliers_zscore = df[column][z_scores > 3]
        
        # Guardar resultados
        outliers_summary[column] = {
            'iqr_count': len(outliers_iqr),
            'zscore_count': len(outliers_zscore),
            'bounds': {'lower': lower_bound, 'upper': upper_bound}
        }
        
        # Imprimir resultados
        print(f"\nAnálisis de outliers para {column}:")
        print(f"Método IQR (1.5 * IQR):")
        print(f"- Límite inferior: {lower_bound:.2f}")
        print(f"- Límite superior: {upper_bound:.2f}")
        print(f"- Número de outliers: {len(outliers_iqr)}")
        print(f"\nMétodo Z-score (|z| > 3):")
        print(f"- Número de outliers: {len(outliers_zscore)}")
        
        # Crear visualizaciones
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 5))
        
        # Boxplot
        sns.boxplot(y=df[column], ax=ax1)
        ax1.set_title(f'Boxplot de {column}')
        
        # Scatter plot con límites IQR
        sns.scatterplot(data=df.reset_index(), x='index', y=column, ax=ax2)
        ax2.axhline(y=upper_bound, color='r', linestyle='--', label='Límite Superior IQR')
        ax2.axhline(y=lower_bound, color='r', linestyle='--', label='Límite Inferior IQR')
        ax2.set_title(f'Scatter plot de {column} con límites IQR')
        ax2.legend()
        
        plt.tight_layout()
        plt.show()


url = "https://github.com/ACken12/Mineria-datos-Proyecto3/blob/main/csv/datos.csv"
df_limpio, df_original, encoders = load_and_clean_dataset(url)

analyze_outliers(df_limpio);
