import pandas as pd

# Leer el archivo CSV original, ignorando la primera fila que contiene los nombres de las columnas
data_frame = pd.read_csv("edades-30Alumnos.csv", delimiter=",", header=None)

# Definir la función para el análisis estadístico
def analisis_estadistico(df):
    try:
        # Verificar si el DataFrame está vacío
        if df.empty:
            raise Exception("El DataFrame está vacío")
        
        # Verificar si la columna de edades contiene valores no numéricos
        for i in df.iloc[:, 1]:
            if not str(i).isnumeric():
                raise Exception("La columna de edades contiene valores no numéricos")
        
        # Crear un DataFrame vacío para almacenar los resultados del análisis
        analisis = pd.DataFrame()
        
        # Crear las columnas del DataFrame de resultados del analisis estadistico
        analisis["edades"] = df.iloc[:, 1].value_counts().index
        analisis["fi"] = df.iloc[:, 1].value_counts().values
        analisis["Fi"] = analisis["fi"].cumsum()
        analisis["ri"] = analisis["fi"] / analisis["fi"].sum()
        analisis["Ri"] = analisis["ri"].cumsum()
        analisis["pi%"] = analisis["ri"] * 100
        analisis["Pi%"] = analisis["Ri"] * 100
        
        return analisis
    # Manejar excepciones en caso de que haya valores no numericos u otros errores en general
    except Exception as e:
        return e

# Llamar a la función con el DataFrame que contiene los datos originales
print(analisis_estadistico(data_frame))
