import pandas as pd
from data.generators.generadorAire import generarDatosCalidadAire

def construirAireDataFrame():
    dataAire = generarDatosCalidadAire()
    # Generamos el DataFrame
    aireDataFrame = pd.DataFrame(dataAire, columns=['nombre', 'comuna', 'ica', 'fecha', 'correo'])
    return aireDataFrame

# Llamar a la función para construir el DataFrame
aire_df = construirAireDataFrame()
print(aire_df)