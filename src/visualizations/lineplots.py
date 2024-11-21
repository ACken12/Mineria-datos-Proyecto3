import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def plot_line_trends(df):
    """
    Crea gráficos de líneas paginados, mostrando 9 gráficos por página.
    
    Parameters:
    -----------
    df : pandas.DataFrame
        DataFrame que contiene los datos a visualizar
    """
    # Configurar el estilo
    sns.set_style("whitegrid")
    sns.set_context("talk")
    
    # Lista de columnas numéricas para analizar
    numeric_columns = [
        'totaldayminutes', 'totaldaycalls', 'totaldaycharge', 
        'totaleveminutes', 'totalevecalls', 'totalevecharge',
        'totalnightminutes', 'totalnightcalls', 'totalnightcharge',
        'totalintlminutes', 'totalintlcalls', 'totalintlcharge',
        'numbercustomerservicecalls', 'numbervmailmessages'
    ]
    
    # Calcular número de páginas necesarias
    plots_per_page = 9
    num_pages = (len(numeric_columns) + plots_per_page - 1) // plots_per_page
    
    for page in range(num_pages):
        # Crear nueva figura para cada página
        fig, axes = plt.subplots(3, 3, figsize=(15, 15))
        axes = axes.flatten()
        
        # Calcular índices para esta página
        start_idx = page * plots_per_page
        end_idx = min(start_idx + plots_per_page, len(numeric_columns))
        
        # Crear gráficos para esta página
        for idx, column_idx in enumerate(range(start_idx, end_idx)):
            column = numeric_columns[column_idx]
            
            # Ordenar por account length para ver tendencias
            df_sorted = df.sort_values('accountlength')
            df_sorted['account_length_bins'] = pd.cut(df_sorted['accountlength'], bins=20)
            grouped_data = df_sorted.groupby('account_length_bins')[column].mean().reset_index()
            
            # Plotear línea de tendencia
            axes[idx].plot(range(len(grouped_data)), grouped_data[column], 
                          marker='o', linestyle='-', color='darkgreen', 
                          linewidth=2, markersize=6)
            
            axes[idx].set_title(f"Tendencia de {column}\npor Longitud de Cuenta", 
                               fontsize=12, pad=10)
            axes[idx].set_xlabel("Rangos de Longitud de Cuenta", fontsize=10)
            axes[idx].set_ylabel(f"Promedio de {column}", fontsize=10)
            
            # Configurar ejes x
            axes[idx].set_xticks(range(0, len(grouped_data), max(1, len(grouped_data)//5)))
            axes[idx].set_xticklabels(
                [str(bin.left)[:5] for bin in grouped_data['account_length_bins'][::max(1, len(grouped_data)//5)]], 
                rotation=45, ha='right', fontsize=8
            )
            
            axes[idx].grid(True, linestyle='--', alpha=0.7)
            axes[idx].tick_params(labelsize=8)
        
        # Ocultar axes vacíos en la última página
        for idx in range(end_idx - start_idx, plots_per_page):
            axes[idx].set_visible(False)
        
        plt.suptitle(f'Página {page + 1} de {num_pages}', fontsize=16, y=0.95)
        plt.tight_layout()
        plt.show()