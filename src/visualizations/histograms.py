import seaborn as sns
import matplotlib.pyplot as plt

def firtshist(first_half,df):
       # Configuración para la primera mitad
        rows = (len(first_half) + 2) // 3  # Número de filas necesarias
        fig, axes = plt.subplots(rows, 3, figsize=(18, 6 * rows))  # Ajustar tamaño
        axes = axes.flatten()  # Aplanar ejes para iterar fácilmente

        # Crear histogramas para la primera mitad
        for i, col in enumerate(first_half):
            sns.histplot(data=df, x=col, kde=True, ax=axes[i])
            axes[i].annotate(
                col,
                xy=(0.5, 0.9),
                xycoords="axes fraction",
                ha="center",
                va="center",
                fontsize=12,
                fontweight="bold",
                color="black",
                bbox=dict(boxstyle="round,pad=0.3", edgecolor="black", facecolor="white"),
            )

        # Ocultar celdas adicionales
        for j in range(i + 1, len(axes)):
            axes[j].axis("off")

        plt.tight_layout()
        return plt.show()

def secondhist(second_half,df):
     # Configuración para la segunda mitad
        rows = (len(second_half) + 2) // 3  # Número de filas necesarias
        fig, axes = plt.subplots(rows, 3, figsize=(18, 6 * rows))  # Ajustar tamaño
        axes = axes.flatten()  # Aplanar ejes para iterar fácilmente

        # Crear histogramas para la segunda mitad
        for i, col in enumerate(second_half):
            sns.histplot(data=df, x=col, kde=True, ax=axes[i])
            axes[i].annotate(
                col,
                xy=(0.5, 0.9),
                xycoords="axes fraction",
                ha="center",
                va="center",
                fontsize=12,
                fontweight="bold",
                color="black",
                bbox=dict(boxstyle="round,pad=0.3", edgecolor="black", facecolor="white"),
            )

        # Ocultar celdas adicionales
        for j in range(i + 1, len(axes)):
            axes[j].axis("off")

        plt.tight_layout()
        return plt.show()



