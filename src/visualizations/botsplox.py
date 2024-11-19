import seaborn as sns
import matplotlib.pyplot as plt

def firtsbox(first_half,df):
    rows = (len(first_half) + 2) // 3
    # Configuración del grid (3 gráficos por fila)
    fig, axes = plt.subplots(rows, 3, figsize=(18, 6 * rows))  # Ajustar tamaño del grid
    axes = axes.flatten()

    # Crear histogramas para la primera mitad
    for i, col in enumerate(first_half):
        sns.boxplot(data=df, x=col, ax=axes[i])
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

def secondbox(second_half,df):
    rows = (len(second_half) + 2) // 3
    # Configuración del grid (3 gráficos por fila)
    fig, axes = plt.subplots(rows, 3, figsize=(18, 6 * rows))  # Ajustar tamaño del grid
    axes = axes.flatten()

    # Crear histogramas para la primera mitad
    for i, col in enumerate(second_half):
        sns.boxplot(data=df, x=col, ax=axes[i])
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
