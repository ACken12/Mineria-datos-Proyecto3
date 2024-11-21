import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler, MinMaxScaler, RobustScaler

class DataProcessor:
    def __init__(self, df):
        self.df = df.copy()
        self.numeric_columns = self.df.select_dtypes(include=[np.number]).columns
        self.categorical_columns = self.df.select_dtypes(include=['object']).columns
        
        # Columnas que necesitan normalización/estandarización
        self.normalize_columns = [
            'totaldayminutes', 'totaldaycharge', 
            'totaleveminutes', 'totalevecharge',
            'totalnightminutes', 'totalnightcharge',
            'totalintlminutes', 'totalintlcharge'
        ]
        
        # Columnas que necesitan escalado
        self.scale_columns = [
            'accountlength', 'numbervmailmessages',
            'totaldaycalls', 'totalevecalls',
            'totalnightcalls', 'totalintlcalls',
            'numbercustomerservicecalls'
        ]
        
    def process_data(self):
        """
        Procesa los datos aplicando las transformaciones necesarias.
        
        Justificación de transformaciones:
        1. Estandarización (StandardScaler):
           - Para variables continuas con distribuciones aproximadamente normales
           - Se aplica a minutos y cargos que tienen diferentes escalas
           - Útil para variables que se usarán en modelos sensibles a la escala
        
        2. Escalado Robusto (RobustScaler):
           - Para variables discretas que pueden tener outliers
           - Se aplica a conteos que pueden tener valores atípicos
           - Mejor manejo de distribuciones no normales y valores atípicos
        """
        # Crear copias de los datos originales
        self.original_data = self.df.copy()
        
        # Estandarización para variables continuas
        standard_scaler = StandardScaler()
        self.df[self.normalize_columns] = standard_scaler.fit_transform(
            self.df[self.normalize_columns]
        )
        
        # Escalado robusto para variables discretas
        robust_scaler = RobustScaler()
        self.df[self.scale_columns] = robust_scaler.fit_transform(
            self.df[self.scale_columns]
        )
        
        # Guardar los scaler para posible uso posterior
        self.standard_scaler = standard_scaler
        self.robust_scaler = robust_scaler
        
        return self.df
    
    def get_transformation_stats(self):
        """Retorna estadísticas de las transformaciones aplicadas."""
        stats = {}
        
        # Estadísticas para variables normalizadas
        for col in self.normalize_columns:
            stats[col] = {
                'original_mean': self.original_data[col].mean(),
                'original_std': self.original_data[col].std(),
                'transformed_mean': self.df[col].mean(),
                'transformed_std': self.df[col].std()
            }
            
        # Estadísticas para variables escaladas
        for col in self.scale_columns:
            stats[col] = {
                'original_median': self.original_data[col].median(),
                'original_iqr': self.original_data[col].quantile(0.75) - 
                               self.original_data[col].quantile(0.25),
                'transformed_median': self.df[col].median(),
                'transformed_iqr': self.df[col].quantile(0.75) - 
                                 self.df[col].quantile(0.25)
            }
            
        return stats