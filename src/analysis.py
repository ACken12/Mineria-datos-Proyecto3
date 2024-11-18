import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.widgets import Button

def univariate_analysis(df):
    """
    Realiza análisis univariado del DataFrame.
    """
    print("\n=== Análisis Univariado ===")
    
    # Análisis de variables numéricas
    numerical_cols = df.select_dtypes(include=[np.number]).columns
    if len(numerical_cols) > 0:
        print("\nVariables Numéricas:")
        for col in numerical_cols:
            print(f"\nEstadísticas para {col}:")
            stats = df[col].describe()
            print(stats)
            
            # Detectar asimetría y curtosis
            skewness = df[col].skew()
            kurtosis = df[col].kurtosis()
            print(f"Asimetría: {skewness:.2f}")
            print(f"Curtosis: {kurtosis:.2f}")
            
            # Crear y mostrar histograma
            plt.figure(figsize=(10, 6))
            sns.histplot(data=df, x=col, kde=True)
            plt.title(f"Distribución de {col}")
            plt.show()

def bivariate_analysis(df):
    """
    Realiza análisis bivariado del DataFrame.
    """
    print("\n=== Análisis Bivariado ===")
    
    numerical_cols = df.select_dtypes(include=[np.number]).columns
    
    # Correlaciones entre variables numéricas
    if len(numerical_cols) > 1:
        print("\nCorrelaciones entre variables numéricas:")
        correlation_matrix = df[numerical_cols].corr()
        print(correlation_matrix)
        
        # Mapa de calor de correlaciones
        plt.figure(figsize=(10, 8))
        sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='.2f')
        plt.title("Mapa de calor de correlaciones")
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
        
        if strong_correlations:
            print("\nCorrelaciones fuertes detectadas (|r| > 0.7):")
            for var1, var2, corr in strong_correlations:
                print(f"{var1} - {var2}: {corr:.3f}")
                
                # Crear scatter plot para correlaciones fuertes
                plt.figure(figsize=(8, 6))
                sns.scatterplot(data=df, x=var1, y=var2)
                plt.title(f"Scatter plot: {var1} vs {var2}")
                plt.show()

    # Análisis específico de variables categóricas vs numéricas
    print("\nAnálisis de variables categóricas vs numéricas específicas:")
    plt.figure(figsize=(12, 15))
    
    # Boxplot de 'totaldayminutes' por 'churn'
    plt.subplot(3, 1, 1)
    sns.boxplot(x='churn', y='totaldayminutes', data=df)
    plt.title('Distribución de Total Day Minutes por Churn')
    plt.xlabel('Churn')
    plt.ylabel('Total Day Minutes')
    
    # Boxplot de 'totalintlminutes' por 'internationalplan'
    plt.subplot(3, 1, 2)
    sns.boxplot(x='internationalplan', y='totalintlminutes', data=df)
    plt.title('Distribución de Total Intl Minutes por International Plan')
    plt.xlabel('International Plan')
    plt.ylabel('Total Intl Minutes')
    
    # Boxplot de 'numbervmailmessages' por 'voicemailplan'
    plt.subplot(3, 1, 3)
    sns.boxplot(x='voicemailplan', y='numbervmailmessages', data=df)
    plt.title('Distribución de Number Vmail Messages por Voicemail Plan')
    plt.xlabel('Voicemail Plan')
    plt.ylabel('Number Vmail Messages')
    
    plt.tight_layout()
    plt.show()

class InteractiveVisualizer:
    def __init__(self, df):
        self.df = df
        self.current_section = 0
        self.current_page = 0
        self.plots_per_page = 9
        
        # Preparar datos para todas las secciones
        self.prepare_all_data()
        
        # Configurar la figura principal
        self.fig = plt.figure(figsize=(20, 16))
        self.create_buttons()
        self.plot_current_view()
        plt.show()
    
    def prepare_all_data(self):
        """Prepara los datos para todas las secciones de gráficos."""
        # Preparar listas para cada tipo de gráfico
        columnas_numericas = self.df.select_dtypes(include=[np.number]).columns
        
        # Datos para histogramas
        self.histogram_data = [{'data': self.df, 'column': col} 
                             for col in columnas_numericas]
        
        # Datos para boxplots
        self.boxplot_data = [{'data': self.df, 'column': col} 
                            for col in columnas_numericas]
        
        # Datos para gráficos de dispersión
        self.scatter_data = []
        for i in range(len(columnas_numericas)):
            for j in range(i + 1, len(columnas_numericas)):
                self.scatter_data.append({
                    'data': self.df,
                    'x': columnas_numericas[i],
                    'y': columnas_numericas[j]
                })
        
        # Datos específicos para boxplots por categoría
        self.category_boxplot_data = [
            {'data': self.df, 'category': 'churn', 'numeric': 'totaldayminutes',
             'title': 'Distribución de Total Day Minutes por Churn'},
            {'data': self.df, 'category': 'internationalplan', 'numeric': 'totalintlminutes',
             'title': 'Distribución de Total Intl Minutes por International Plan'},
            {'data': self.df, 'category': 'voicemailplan', 'numeric': 'numbervmailmessages',
             'title': 'Distribución de Number Vmail Messages por Voicemail Plan'}
        ]
        
        # Lista de todas las secciones y sus títulos
        self.sections = [
            (self.histogram_data, "Histogramas de Distribución", self.plot_histogram),
            (self.boxplot_data, "Boxplots de Distribución", self.plot_boxplot),
            (self.scatter_data, "Gráficos de Dispersión", self.plot_scatter),
            (self.category_boxplot_data, "Boxplots por Categoría", self.plot_category_boxplot)
        ]
    
    def create_buttons(self):
        """Crea los botones de navegación."""
        # Botones para navegación entre secciones
        self.btn_prev_section = Button(plt.axes([0.2, 0.02, 0.15, 0.04]), '← Sección Anterior')
        self.btn_next_section = Button(plt.axes([0.65, 0.02, 0.15, 0.04]), 'Siguiente Sección →')
        
        # Botones para navegación entre páginas
        self.btn_prev_page = Button(plt.axes([0.4, 0.02, 0.1, 0.04]), '← Página')
        self.btn_next_page = Button(plt.axes([0.5, 0.02, 0.1, 0.04]), 'Página →')
        
        # Conectar eventos
        self.btn_prev_section.on_clicked(self.prev_section)
        self.btn_next_section.on_clicked(self.next_section)
        self.btn_prev_page.on_clicked(self.prev_page)
        self.btn_next_page.on_clicked(self.next_page)
    
    def plot_histogram(self, data, ax):
        """Dibuja un histograma."""
        sns.histplot(data=data['data'], x=data['column'], 
                    kde=True, color='skyblue', edgecolor='black', ax=ax)
        ax.set_title(f"Histograma de {data['column']}")
    
    def plot_boxplot(self, data, ax):
        """Dibuja un boxplot."""
        sns.boxplot(data=data['data'], y=data['column'], 
                   color='lightgreen', width=0.5, ax=ax)
        ax.set_title(f"Boxplot de {data['column']}")
    
    def plot_scatter(self, data, ax):
        """Dibuja un gráfico de dispersión."""
        sns.scatterplot(data=data['data'], x=data['x'], y=data['y'],
                       alpha=0.6, color='purple', ax=ax)
        ax.set_title(f"{data['x']} vs {data['y']}")
    
    def plot_category_boxplot(self, data, ax):
        """Dibuja un boxplot por categoría."""
        sns.boxplot(data=data['data'], x=data['category'], y=data['numeric'],
                   palette='Set3', ax=ax)
        ax.set_title(data['title'])
        plt.setp(ax.xaxis.get_majorticklabels(), rotation=45)
    
    def plot_current_view(self):
        """Actualiza la vista actual con los gráficos correspondientes."""
        # Limpiar figura
        plt.clf()
        self.create_buttons()
        
        # Obtener datos de la sección actual
        current_data, section_title, plot_function = self.sections[self.current_section]
        
        # Calcular índices para la página actual
        start_idx = self.current_page * self.plots_per_page
        end_idx = min(start_idx + self.plots_per_page, len(current_data))
        
        # Actualizar título principal
        total_pages = (len(current_data) + self.plots_per_page - 1) // self.plots_per_page
        self.fig.suptitle(f"{section_title} - Página {self.current_page + 1} de {total_pages}",
                         fontsize=16, y=0.98)
        
        # Crear y llenar los subplots
        for i, idx in enumerate(range(start_idx, end_idx)):
            ax = plt.subplot(3, 3, i + 1)
            plot_function(current_data[idx], ax)
        
        plt.tight_layout(rect=[0, 0.08, 1, 0.95])
        self.fig.canvas.draw_idle()
    
    def next_section(self, event):
        """Avanza a la siguiente sección."""
        if self.current_section < len(self.sections) - 1:
            self.current_section += 1
            self.current_page = 0
            self.plot_current_view()
    
    def prev_section(self, event):
        """Retrocede a la sección anterior."""
        if self.current_section > 0:
            self.current_section -= 1
            self.current_page = 0
            self.plot_current_view()
    
    def next_page(self, event):
        """Avanza a la siguiente página."""
        current_data = self.sections[self.current_section][0]
        total_pages = (len(current_data) + self.plots_per_page - 1) // self.plots_per_page
        if self.current_page < total_pages - 1:
            self.current_page += 1
            self.plot_current_view()
    
    def prev_page(self, event):
        """Retrocede a la página anterior."""
        if self.current_page > 0:
            self.current_page -= 1
            self.plot_current_view()

def perform_analysis(df):
    """Realiza el análisis exploratorio completo con visualizaciones interactivas."""
    print("\n=== Iniciando Análisis Exploratorio de Datos ===")
    
    # Realizar análisis univariado y bivariado
    print("\n=== Análisis automático después de limpieza ===")
    print("\nAnálisis univariado:")
    univariate_analysis(df)
    print("\nAnálisis bivariado:")
    bivariate_analysis(df)
    
    # Iniciar visualizador interactivo
    print("\nIniciando visualizador interactivo...")
    visualizer = InteractiveVisualizer(df)
    
    return visualizer