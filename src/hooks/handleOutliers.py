import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats

def handle_outliers(df, method='iqr', threshold=3):
    """
    Maneja los outliers detectados según el método especificado.
    
    Args:
        df: DataFrame original
        method: 'iqr' o 'zscore'
        threshold: umbral para z-score (por defecto 3)
    
    Returns:
        DataFrame con outliers tratados
    """
    df_cleaned = df.copy()
    numerical_cols = df.select_dtypes(include=[np.number]).columns
    
    for column in numerical_cols:
        if method == 'iqr':
            Q1 = df[column].quantile(0.25)
            Q3 = df[column].quantile(0.75)
            IQR = Q3 - Q1
            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR
            
            # Recortar valores fuera de los límites
            df_cleaned[column] = df_cleaned[column].clip(lower_bound, upper_bound)
            
        elif method == 'zscore':
            z_scores = np.abs(stats.zscore(df[column]))
            df_cleaned[column] = df_cleaned[column].mask(z_scores > threshold, df[column].median())
    
    return df_cleaned