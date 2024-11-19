import numpy as np
from visualizations.heatmap import heatM
from visualizations.scatterplots import scatterP
def bivariate_analysis(df):
    """
    Realiza análisis bivariado del DataFrame.
    """
    print("\n=== Análisis Bivariado ===")
    
    numerical_cols = df.select_dtypes(include=[np.number]).columns
    categorical_cols = df.select_dtypes(exclude=[np.number]).columns
    
    # Correlaciones entre variables numéricas
    strong_correlations = heatM(numerical_cols,df)
    scatterP(strong_correlations,df)
    
   
