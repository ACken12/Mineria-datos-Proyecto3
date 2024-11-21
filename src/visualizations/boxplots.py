import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import math

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

def categoryBoxplots(df):
    """
    Creates and displays categorical boxplots for specific variable relationships.
    
    Parameters:
    df (pandas.DataFrame): DataFrame containing the data
    
    Returns:
    None: Displays the plots directly
    """
    # Define the relationships to plot
    relationships = [
        {'category': 'churn', 'numeric': 'totaldayminutes',
         'title': 'Distribución de Total Day Minutes por Churn'},
        {'category': 'internationalplan', 'numeric': 'totalintlminutes',
         'title': 'Distribución de Total Intl Minutes por International Plan'},
        {'category': 'voicemailplan', 'numeric': 'numbervmailmessages',
         'title': 'Distribución de Number Vmail Messages por Voicemail Plan'}
    ]
    
    # Create figure with subplots
    fig, axes = plt.subplots(1, 3, figsize=(20, 6))
    fig.suptitle('Análisis de Variables Categóricas vs Numéricas', fontsize=16, y=1.05)
    
    # Create each boxplot
    for i, plot_data in enumerate(relationships):
        sns.boxplot(data=df, 
                   x=plot_data['category'], 
                   y=plot_data['numeric'],
                   palette='Set3', 
                   ax=axes[i])
        
        axes[i].set_title(plot_data['title'], fontsize=10, pad=10)
        axes[i].set_xlabel(plot_data['category'], fontsize=9)
        axes[i].set_ylabel(plot_data['numeric'], fontsize=9)
        axes[i].tick_params(labelsize=8)
        plt.setp(axes[i].xaxis.get_majorticklabels(), rotation=45)
    
    plt.tight_layout()
    plt.show()


def plot_density_charts(df):
    """
    Crea gráficos de densidad combinados con histogramas, mostrando un máximo de 9 gráficos por página
    
    Args:
        df: DataFrame con los datos a visualizar
    """
    # Obtener las columnas numéricas
    numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns
    
    # Calcular el número total de páginas necesarias
    graphs_per_page = 9
    total_graphs = len(numeric_columns)
    total_pages = math.ceil(total_graphs / graphs_per_page)
    
    # Configurar el layout para cada página
    rows = 3
    cols = 3
    
    # Configurar el estilo de seaborn
    sns.set_style("whitegrid")
    
    # Iterar sobre cada página
    for page in range(total_pages):
        # Crear una nueva figura para cada página con más espacio entre subplots
        fig = plt.figure(figsize=(20, 20))
        fig.suptitle(f'Distribución de Variables - Página {page + 1}/{total_pages}', 
                    y=0.95, fontsize=16, fontweight='bold')
        
        # Obtener las columnas para la página actual
        start_idx = page * graphs_per_page
        end_idx = min((page + 1) * graphs_per_page, total_graphs)
        page_columns = numeric_columns[start_idx:end_idx]
        
        # Crear los gráficos para cada columna en la página actual
        for i, column in enumerate(page_columns):
            # Crear subplot con más espacio
            ax = plt.subplot(rows, cols, i + 1)
            
            # Crear el histograma y gráfico de densidad combinados
            sns.histplot(data=df, x=column, stat="density", alpha=0.4, color='skyblue', label='Histograma')
            sns.kdeplot(data=df[column], color='red', lw=2, label='Densidad')
            
            # Personalizar el gráfico
            plt.title(f'Distribución de {column}', pad=20, fontsize=12, fontweight='bold')
            plt.xlabel(column, labelpad=10)
            plt.ylabel('Densidad', labelpad=10)
            plt.legend()
            
            # Ajustar los márgenes del subplot
            plt.margins(x=0.1)
            
            # Rotar las etiquetas del eje x si son muy largas
            plt.xticks(rotation=45 if len(str(column)) > 10 else 0)
        
        # Ocultar los subplots vacíos restantes
        for j in range(len(page_columns), graphs_per_page):
            ax = plt.subplot(rows, cols, j + 1)
            ax.set_visible(False)
        
        # Ajustar el layout con más espacio entre subplots
        plt.tight_layout(pad=3.0, w_pad=2.0, h_pad=3.0)
        
        # Mostrar la página
        plt.show()