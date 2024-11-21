import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

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
    
def plot_dispersion_charts(df):
    """
    Creates scatter plot matrix for continuous variables with improved formatting
    and compact layout.
    
    Args:
        df (pandas.DataFrame): DataFrame containing the data to visualize
    """
    # Define continuous variables for analysis
    continuous_columns = [
        'totaldayminutes', 'totaldaycharge',
        'totaleveminutes', 'totalevecharge',
        'totalnightminutes', 'totalnightcharge', 
        'totalintlminutes', 'totalintlcharge',
        'numbercustomerservicecalls',
        'numbervmailmessages'
    ]
    
    # Create all possible pairs
    pairs = []
    for i in range(len(continuous_columns)):
        for j in range(i + 1, len(continuous_columns)):
            pairs.append((continuous_columns[i], continuous_columns[j]))
    
    # Configure plots per page
    plots_per_page = 9
    total_pages = int(np.ceil(len(pairs) / plots_per_page))
    
    # Set style and font sizes
    sns.set_style("whitegrid")
    TITLE_SIZE = 9  # Reduced from 10
    LABEL_SIZE = 8  # Reduced from 9
    TICK_SIZE = 7   # Reduced from 8
    
    # Set the default figure DPI for better resolution
    plt.rcParams['figure.dpi'] = 100
    
    # Iterate through pages
    for page in range(total_pages):
        # Create figure with smaller size
        fig, axes = plt.subplots(3, 3, figsize=(12, 10))  # Reduced from (15, 15)
        axes = axes.flatten()
        
        # Get indices for current page
        start_idx = page * plots_per_page
        end_idx = min(start_idx + plots_per_page, len(pairs))
        
        # Create scatter plots for this page
        for plot_idx, pair_idx in enumerate(range(start_idx, end_idx)):
            x_col, y_col = pairs[pair_idx]
            
            # Format variable names for labels (simplified)
            x_label = x_col.replace('total', '').replace('minutes', 'Minutes').replace('charge', 'Charge')
            y_label = y_col.replace('total', '').replace('minutes', 'Minutes').replace('charge', 'Charge')
            
            # Create scatter plot with smaller points
            sns.scatterplot(
                data=df,
                x=x_col,
                y=y_col,
                color='purple',
                alpha=0.4,
                s=15,  # Reduced point size from 25
                ax=axes[plot_idx]
            )
            
            # Customize labels and title
            axes[plot_idx].set_xlabel(f"{x_label}", fontsize=LABEL_SIZE)
            axes[plot_idx].set_ylabel(f"{y_label}", fontsize=LABEL_SIZE)
            axes[plot_idx].tick_params(labelsize=TICK_SIZE)
            
            # Add title with "vs"
            axes[plot_idx].set_title(f"{y_label} vs {x_label}", 
                                   fontsize=TITLE_SIZE, 
                                   pad=8)  # Reduced padding
            
            # Adjust grid appearance
            axes[plot_idx].grid(True, linestyle='--', alpha=0.5)
            
            # Rotate x-axis labels slightly
            plt.setp(axes[plot_idx].get_xticklabels(), rotation=30, ha='right')
            
            # Remove top and right spines for cleaner look
            axes[plot_idx].spines['top'].set_visible(False)
            axes[plot_idx].spines['right'].set_visible(False)
            
        # Remove empty subplots
        for idx in range(end_idx - start_idx, plots_per_page):
            fig.delaxes(axes[idx])
        
        # Adjust layout with less padding
        plt.tight_layout(pad=1.5, h_pad=1.5, w_pad=1.5)
        
        # Show current page
        plt.show()