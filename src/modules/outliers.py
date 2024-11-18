import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

def analyze_outliers(df):
    """
    Realiza análisis de outliers utilizando métodos Z-score e IQR.
    Devuelve un resumen de los outliers detectados en cada columna numérica y grafica resultados clave.
    """
    numerical_cols = df.select_dtypes(include=[np.number]).columns  # Solo valores numéricos
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
        
        # Graficar resultados
        plt.figure(figsize=(12, 6))
        
        # Boxplot con límites
        plt.subplot(1, 2, 1)
        plt.boxplot(df[column], vert=False, patch_artist=True)
        plt.axvline(lower_bound, color='red', linestyle='--', label='Límite Inferior (IQR)')
        plt.axvline(upper_bound, color='green', linestyle='--', label='Límite Superior (IQR)')
        plt.title(f'Boxplot de {column}')
        plt.legend()
        
        # Conteo de outliers
        plt.subplot(1, 2, 2)
        plt.bar(['IQR', 'Z-score'], [len(outliers_iqr), len(outliers_zscore)], color=['blue', 'orange'])
        plt.title(f'Conteo de outliers en {column}')
        plt.ylabel('Cantidad')
        
        plt.tight_layout()
        plt.show()
    
    return outliers_summary
