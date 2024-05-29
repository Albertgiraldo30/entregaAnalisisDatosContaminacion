import pandas as pd
from data.generators.contaminacionIndustrial import contaminacionIndustrial

def construirContaminacionIndustrialDataFrame():
    dataContaminacionIndustri = contaminacionIndustrial()
    # Generamos el DataFrame
    contaminacionIndustrialDataframe = pd.DataFrame(dataContaminacionIndustri, columns=['nombre_empresa','sector','comuna','actividad','emisiones_ton_año','vertimientos_m3_año','residuos_ton_año','fecha_revision'])
    return dataContaminacionIndustri

# Llamar a la función para construir el DataFrame
aire_industri_df = construirContaminacionIndustrialDataFrame()
print(aire_industri_df)