import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd


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

def plot_categorical_bars(df):
    """
    Dibuja gráficos de barras para las categorías churn, internationalplan y voicemailplan
    """
    # Configuración básica
    sns.set_style("whitegrid")
    categorical_columns = ['churn', 'internationalplan', 'voicemailplan']
    
    # Crear subplots (1 fila, 3 columnas)
    fig, axes = plt.subplots(1, 3, figsize=(15, 5))
    
    # Crear gráficos
    for idx, column in enumerate(categorical_columns):
        value_counts = df[column].value_counts()
        value_counts.plot(kind='bar', ax=axes[idx], color='steelblue', edgecolor='black')
        
        axes[idx].set_title(f"Distribución de {column}")
        axes[idx].set_xlabel(column)
        axes[idx].set_ylabel('Frecuencia')
        
        # Rotar etiquetas
        plt.setp(axes[idx].get_xticklabels(), rotation=45, ha='right')
        
        # Añadir valores sobre las barras
        for i, v in enumerate(value_counts):
            axes[idx].text(i, v, str(v), ha='center', va='bottom')
    
    plt.tight_layout()
    plt.show()