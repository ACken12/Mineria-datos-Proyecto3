import seaborn as sns
import matplotlib.pyplot as plt

def heatM(numerical_cols,df):
     if len(numerical_cols) > 1:
        print("\nCorrelaciones entre variables numéricas:")
        correlation_matrix = df[numerical_cols].corr()
        print(correlation_matrix)
        
        # Mapa de calor de correlaciones
        plt.figure(figsize=(10, 8))
        sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
        plt.title("Mapa de calor de correlaciones")
        plt.tight_layout()
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
        return strong_correlations