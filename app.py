import pandas as pd

lista_cargada = [21, 29, 19, 22, 23, 19, 30, 19, 19, 19, 20, 20, 20, 18, 22, 19, 34, 34, 21, 21, 22, 28, 29, 19, 20, 19, 25, 28, 21, 22]

# * Definir la función para el análisis estadístico
def analisis_estadistico(list, name):
    try:
        # * Verificar si la lista está vacía
        if list == []:
            raise Exception("El primer parametro no es una lista o esta vacia")
        
        # * Verificar si la columna de edades contiene valores no numéricos
        for i in list:
            if not str(i).isnumeric():
                raise Exception("La columna de edades contiene valores no numéricos")

        # * Crear una Serie con los valores de la columna de edades
        serie = pd.DataFrame(list, columns=[name])

        # * Crear un DataFrame vacío para almacenar los resultados del análisis
        analisis = pd.DataFrame()
        
        # * Crear las columnas del DataFrame de resultados del analisis estadistico
        analisis[name] = serie.iloc[:, 0].value_counts().index
        analisis["fi"] = serie.iloc[:, 0].value_counts().values
        analisis["Fi"] = analisis["fi"].cumsum()
        analisis["ri"] = analisis["fi"] / analisis["fi"].sum()
        analisis["Ri"] = analisis["ri"].cumsum()
        analisis["pi%"] = analisis["ri"] * 100
        analisis["Pi%"] = analisis["Ri"] * 100
        
        return analisis
    # * Manejar excepciones en caso de que haya valores no numericos u otros errores en general
    except Exception as e:
        return e

# * Llamar a la función que realiza el análisis estadístico y mostrarlo
analisis = analisis_estadistico(lista_cargada, "edades")
print(type(analisis))
print(analisis)