import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def univariate_analysis(df, graphs_per_page=4):
    """
    Realiza análisis univariado del DataFrame y muestra los gráficos en una sola página
    con botones para navegar entre páginas.
    """
    print("\n=== Análisis Univariado ===")
    figures = []  # Lista para almacenar las figuras (como imágenes estáticas)
    
    # Análisis de variables numéricas
    numerical_cols = df.select_dtypes(include=[np.number]).columns
    if len(numerical_cols) > 0:
        for col in numerical_cols:
            # Crear histograma
            fig, ax = plt.subplots(figsize=(10, 6))
            sns.histplot(data=df, x=col, kde=True, ax=ax)
            ax.set_title(f"Distribución de {col}")
            fig.tight_layout()
            figures.append(fig)  # Añadir figura a la lista
            plt.close(fig)  # Cerrar la figura para evitar demasiadas abiertas
            
            # Crear diagrama de caja
            fig, ax = plt.subplots(figsize=(10, 6))
            sns.boxplot(data=df, x=col, ax=ax)
            ax.set_title(f"Diagrama de caja de {col}")
            fig.tight_layout()
            figures.append(fig)  # Añadir figura a la lista
            plt.close(fig)  # Cerrar la figura para evitar demasiadas abiertas
    
    # Análisis de variables categóricas
    categorical_cols = df.select_dtypes(exclude=[np.number]).columns
    if len(categorical_cols) > 0:
        for col in categorical_cols:
            # Crear gráfico de barras
            fig, ax = plt.subplots(figsize=(10, 6))
            sns.countplot(data=df, x=col, ax=ax)
            ax.set_title(f"Distribución de {col}")
            plt.xticks(rotation=45)
            fig.tight_layout()
            figures.append(fig)  # Añadir figura a la lista
            plt.close(fig)  # Cerrar la figura para evitar demasiadas abiertas
    
    # Función para mostrar una página de gráficos
    def show_page(page_num):
        start_idx = page_num * graphs_per_page
        end_idx = start_idx + graphs_per_page
        figs_to_show = figures[start_idx:end_idx]
        
        # Crear una figura con subgráficos
        fig, axes = plt.subplots(1, len(figs_to_show), figsize=(15, 5))
        
        if len(figs_to_show) == 1:  # Para el caso de que haya solo un gráfico
            axes = [axes]
        
        for ax, figure in zip(axes, figs_to_show):
            ax.imshow(figure.canvas.renderer.buffer_rgba())
            ax.axis('off')  # Quitar los ejes
        
        plt.show()

    # Mostrar la primera página de gráficos
    current_page = 0
    show_page(current_page)
    
    # Aquí podrías agregar lógica para navegar entre las páginas, por ejemplo:
    # * Mostrar un botón de "Siguiente" que aumente el número de página y muestre los gráficos siguientes.
