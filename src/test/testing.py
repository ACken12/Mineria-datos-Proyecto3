import pandas as pd
import numpy as np

# Ejemplo de datos
data = {
    'CustomerChurn': ['No', 'Yes', 'No', 'Yes'],
    'HasInternationalPlan': ['no', 'yes', 'no', 'yes'],
    'HasVoicemailPlan': ['yes', 'no', 'yes', 'no']
}
df = pd.DataFrame(data)

columnas_categoricas = ['CustomerChurn', 'HasInternationalPlan', 'HasVoicemailPlan']

for col in columnas_categoricas:
    if not pd.api.types.is_datetime64_any_dtype(df[col]):
        print(f"\nColumna '{col}':")
        print("  Valores únicos originales:", df[col].unique())

        # Normalizar a minúsculas
        df[col] = df[col].str.lower()
        
        # Aplicar el mapeo si los valores son "yes"/"no"
        if set(df[col].unique()) == {"yes", "no"}:
            df[col] = df[col].map({"no": 0, "yes": 1}).astype(int)
            print("  Mapeo aplicado: 'no' -> 0, 'yes' -> 1")
        else:
            print("  Mapeo no aplicable a esta columna.")
        
        print("  Valores codificados:", df[col].unique())
