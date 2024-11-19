import seaborn as sns
import matplotlib.pyplot as plt

def scatterP(strong_correlations,df):
     # Todos los gráficos (mapa de calor y scatter plots) en la misma página, subgráficos.
    if len(strong_correlations) > 0:
        rows = len(strong_correlations) // 2 + 1  # Número de filas
        cols = 2  # Número de columnas (para que quepan dos gráficos por fila)
        fig, axes = plt.subplots(rows, cols, figsize=(15, 8))  
        axes = axes.flatten()  

        for i, (var1, var2, corr) in enumerate(strong_correlations):
            sns.scatterplot(data=df, x=var1, y=var2, ax=axes[i])
            axes[i].set_title(f"Scatter plot: {var1} vs {var2} (Corr: {corr:.2f})")
        
        # Si hay menos gráficos que celdas, ocultar los ejes vacíos
        for j in range(i + 1, len(axes)):
            axes[j].axis("off")
        
        plt.tight_layout()
        return plt.show()