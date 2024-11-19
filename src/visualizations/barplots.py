import matplotlib.pyplot as plt
import seaborn as sns

def first_bar(first_half, df):
    # Primer conjunto de gráficos: Primera mitad
    rows = (len(first_half) + 2) // 3  # Número de filas necesarias
    fig, axes = plt.subplots(rows, 3, figsize=(18, 6 * rows))  # Ajustar tamaño
    axes = axes.flatten()  # Aplanar los ejes para iterar fácilmente
    
    # Crear gráficos de barras para la primera mitad
    for i, col in enumerate(first_half):
        sns.countplot(data=df, x=col, ax=axes[i])
        axes[i].set_title(f"{col}")  # Título de cada gráfico
    
    # Ocultar ejes adicionales si hay menos gráficos que celdas
    for j in range(i + 1, len(axes)):
        axes[j].axis("off")
    
    plt.subplots_adjust(hspace=0.5)  # Ajuste de espacio entre los gráficos
    return plt.show()


def second_bar(second_half, df):
# Segundo conjunto de gráficos: Segunda mitad
    rows = (len(second_half) + 2) // 3  # Número de filas necesarias
    fig, axes = plt.subplots(rows, 3, figsize=(18, 6 * rows))  # Ajustar tamaño
    axes = axes.flatten()  # Aplanar los ejes para iterar fácilmente
    
    # Crear gráficos de barras para la segunda mitad
    for i, col in enumerate(second_half):
        sns.countplot(data=df, x=col, ax=axes[i])
        axes[i].set_title(f"{col}")  # Título de cada gráfico
    
    # Ocultar ejes adicionales si hay menos gráficos que celdas
    for j in range(i + 1, len(axes)):
        axes[j].axis("off")
    
    plt.subplots_adjust(hspace=0.5)  # Ajuste de espacio entre los gráficos
    return plt.show()
