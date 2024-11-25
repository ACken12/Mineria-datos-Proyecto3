import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder

"""
CustomerChurn -  para representar si un cliente se da de baja.
AccountLength - Duración de la cuenta.
HasInternationalPlan - Indica si tiene un plan internacional.
HasVoicemailPlan - Indica si tiene un plan de correo de voz.
VoicemailMessageCount - Número de mensajes de correo de voz.
DayMinutes - Minutos utilizados durante el día.
DayCalls - Llamadas realizadas durante el día.
DayCharges - Costos totales de llamadas diurnas.
EveningMinutes - Minutos utilizados durante la tarde/noche.
EveningCalls - Llamadas realizadas durante la tarde/noche.
EveningCharges - Costos totales de llamadas nocturnas.
NightMinutes - Minutos utilizados durante la noche.
NightCalls - Llamadas realizadas durante la noche.
NightCharges - Costos totales de llamadas nocturnas.
InternationalMinutesCalls - Minutos utilizados en llamadas internacionales.
InternationalCalls - Llamadas internacionales realizadas.
InternationalCharges - Costos de llamadas internacionales.
CustomerServiceCalls - Número de llamadas al servicio al cliente.

"""

def load_dataset(url):
    """
    Lee un archivo CSV desde GitHub y retorna el DataFrame.

    """
    # Convertir la URL normal de GitHub a la URL raw
    raw_url = url.replace('github.com', 'raw.githubusercontent.com')
    raw_url = raw_url.replace('/blob/', '/')
    
    try:
        # Leer el CSV con pandas
        df = pd.read_csv(raw_url)
        df.rename(columns=
        {
        "churn": "CustomerChurn", 
        "accountlength": "AccountLength",
        "internationalplan" : "HasInternationalPlan",
        "voicemailplan": "HasVoicemailPlan",
        "numbervmailmessages": "VoicemailMessageCount",
        "totaldayminutes": "DayMinutes",
        "totaldaycalls": "DayCalls",
        "totaldaycharge": "DayCharges",
        "totaleveminutes":"EveningMinutes",
        "totalevecalls" : "EveningCalls",
        "totalevecharge": "EveningCharges",
        "totalnightminutes" : "NightMinutes",
        "totalnightcalls" : "NightCalls",
        "totalnightcharge" : "NightCharges",
        "totalintlminutes" : "InternationalMinutesCalls",
        "totalintlcalls": "InternationalCalls",
        "totalintlcharge" : "InternationalCharges",
        "numbercustomerservicecalls":"CustomerServiceCalls"
        }, 
        inplace=True)
        df_original = df.copy()
        # Retornamos None como tercer elemento para mantener consistencia con clean_dataset
        return df, df_original, None
        
    except Exception as e:
        print(f"Error al cargar el archivo: {e}")
        return None, None, None

def clean_dataset(df, df_original=None):
    """
    Realiza una limpieza completa del DataFrame.
    
    """
    if df is None:
        return None, None, None
    
    try:
        # Crear copia para no modificar el original si no se proporciona uno
        if df_original is None:
            df_original = df.copy()
        df = df.copy()



        """
        Examples: How to rename the columns, if you want to rename some columns
        , you can use this method
        """
        # df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6]})
        # df.rename(columns={"A": "a", "B": "c"})

        # 1. Mostrar información inicial
        print("=== Información inicial del dataset ===")
        print(f"\nDimensiones del dataset: {df.shape}")
        print("\nColumnas originales:")
        print(df.columns.tolist())
        print("\nTipos de datos:")
        print(df.dtypes)
        print("\nValores nulos por columna:")
        print(df.isnull().sum())
        print("\nPrimeras 5 filas del dataset:")
        print(df.head())
        
        # 2. Cambiar nombres de columnas
        df.columns = df.columns.str.replace(' ', '_')
        
        # 3. Eliminar duplicados
        duplicados_originales = df.duplicated().sum()
        if duplicados_originales > 0:
            df = df.drop_duplicates()
            print(f"\nFilas duplicadas eliminadas: {duplicados_originales}")
        else:
            print("\nNo se encontraron filas duplicadas")
        
        # 4. Tratar valores nulos
        print("\n=== Tratamiento de valores nulos ===")
        for columna in df.columns:
            nulos = df[columna].isnull().sum()
            if nulos > 0:
                print(f"\nColumna '{columna}': {nulos} valores nulos")
                if df[columna].dtype in ['int64', 'float64']:
                    mediana = df[columna].median()
                    df[columna] = df[columna].fillna(mediana)
                    print(f"  - Rellenados con la mediana: {mediana}")
                else:
                    moda = df[columna].mode()[0]
                    df[columna] = df[columna].fillna(moda)
                    print(f"  - Rellenados con la moda: {moda}")
        
        # 5. Detectar y tratar valores atípicos
        print("\n=== Tratamiento de valores atípicos ===")
        columnas_numericas = df.select_dtypes(include=[np.number]).columns
        for col in columnas_numericas:
            Q1 = df[col].quantile(0.25)
            Q3 = df[col].quantile(0.75)
            IQR = Q3 - Q1
            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR
            
            outliers = df[(df[col] < lower_bound) | (df[col] > upper_bound)].shape[0]
            if outliers > 0:
                print(f"\nColumna '{col}': {outliers} valores atípicos encontrados")
                print(f"  - Rango válido: [{lower_bound:.2f}, {upper_bound:.2f}]")
                df[col] = df[col].clip(lower=lower_bound, upper=upper_bound)
        
        # 6. Convertir tipos de datos
        print("\n=== Conversión de tipos de datos ===")
        posibles_fechas = [col for col in df.columns if any(x in col.lower() for x in ['fecha', 'date', 'time'])]
        
        if posibles_fechas:
            print("\nColumnas identificadas como posibles fechas:")
            for col in posibles_fechas:
                try:
                    df[col] = pd.to_datetime(df[col], format='infer')
                    print(f"  - '{col}' convertida a datetime")
                except Exception as e:
                    print(f"  - No se pudo convertir '{col}' a fecha: {str(e)}")
        
        # 7. Codificar variables categóricas
        print("\n=== Codificación de variables categóricas ===")
        label_encoders = {}
        columnas_categoricas = df.select_dtypes(include=['object']).columns
        columnas_binarias = ['CustomerChurn','HasInternationalPlan', 'HasVoicemailPlan']
    
        for col in columnas_categoricas:
            if not pd.api.types.is_datetime64_any_dtype(df[col]):
                print(f"\nColumna '{col}':")
                print("  Valores únicos originales:", df[col].unique())
                
                # Primero limpiamos y estandarizamos los valores
                df[col] = df[col].astype(str).str.strip().str.lower()
                
                # Si la columna es binaria (yes/no)
                if col in columnas_binarias:
                    # Creamos un mapping más completo para manejar diferentes casos
                    mapping = {
                        'yes': 1,
                        'no': 0,
                        'y': 1,
                        'n': 0,
                        'true': 1,
                        'false': 0,
                        '1': 1,
                        '0': 0
                    }
                    
                    # Aplicamos la transformación y manejamos valores no encontrados
                    df[col] = df[col].map(mapping)
                    
                    # Verificamos si hay valores que no se pudieron mapear
                    valores_no_mapeados = df[col].isna().sum()
                    if valores_no_mapeados > 0:
                        print(f"  Advertencia: {valores_no_mapeados} valores no pudieron ser mapeados en '{col}'")
                    
                    # Convertimos a entero (los NA se convertirán en 0)
                    df[col] = df[col].fillna(0).astype(int)
                    print(f"  Valores codificados para {col}:", np.unique(df[col]))
                
                else:
                    # Para el resto de variables categóricas usamos LabelEncoder
                    label_encoders[col] = LabelEncoder()
                    df[col] = label_encoders[col].fit_transform(df[col])
                    print(f"  Valores codificados para {col}:", np.unique(df[col]))

        # 8. Mostrar información final
        print("\n=== Información final del dataset ===")
        print(f"\nDimensiones finales: {df.shape}")
        print("\nTipos de datos finales:")
        print(df.dtypes)
        print("\nValores nulos restantes:")
        print(df.isnull().sum())
        print("\nPrimeras 5 filas del dataset limpio:")
        print(df.head(12))
        return df, df_original, label_encoders
        
    except Exception as e:
        print(f"Error al limpiar el dataset: {e}")
        return None, None, None
