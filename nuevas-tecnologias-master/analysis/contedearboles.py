import pandas as pd

from data.generators.conteodearboles import generarDatosConteoArboles

def construirArbolFrame():
    datosArbol=generarDatosConteoArboles()


    #generamos el dataframe
    arbolDataFrame=pd.DataFrame(datosArbol,columns=['nombre','comuna','correo','fecha','direccion','decibeliosdiurnos','decibeliosnosturnos','encuesta'])


    print(arbolDataFrame)
    
generarDatosConteoArboles()
