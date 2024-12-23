import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.widgets import Button


class InteractiveVisualizer:
    def __init__(self, df):
        self.df = df
        self.current_section = 0
        self.current_page = 0
        self.plots_per_page = 9
        self.prepare_all_data()
        self.fig = plt.figure(figsize=(20, 16))
        self.create_buttons()
        self.plot_current_view()
        plt.show()
    
    def prepare_all_data(self):
        """Prepara los datos para todas las secciones de gráficos."""
        # Preparar listas para cada tipo de gráfico
        columnas_numericas = self.df.select_dtypes(include=[np.number]).columns
        columnas_categoricas = self.df.select_dtypes(include=['object', 'category']).columns
        
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
        
        # Datos para boxplots por categoría
        self.category_boxplot_data = []
        for cat_col in columnas_categoricas:
            for num_col in columnas_numericas:
                self.category_boxplot_data.append({
                    'data': self.df,
                    'category': cat_col,
                    'numeric': num_col
                })
        
        # Lista de todas las secciones y sus títulos
        self.sections = [
            (self.histogram_data, "Histogramas", self.plot_histogram),
            (self.boxplot_data, "Boxplots", self.plot_boxplot),
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
        ax.set_title(f"{data['numeric']} por {data['category']}")
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