import numpy as np
from visualizations.heatmap import heatM
from visualizations.scatterplots import scatterP
from visualizations.boxplots import categoryBoxplots
def bivariate_analysis(df):
    """
    Realiza análisis bivariado del DataFrame.
    """
    print("\n=== Análisis Bivariado ===")
    print("Tipo del conjunto de datos: " + str(type(df)))
    numerical_cols = df.select_dtypes(include=[np.number]).columns
    categorical_cols = df.select_dtypes(exclude=[np.number]).columns
    
    # Correlaciones entre variables numéricas

    # Correlación Heatmap
    strong_correlations = heatM(numerical_cols,df)
    # Correlación Gráficos de dispersión
    scatterP(strong_correlations,df)

    categoryBoxplots(df)
    
   
