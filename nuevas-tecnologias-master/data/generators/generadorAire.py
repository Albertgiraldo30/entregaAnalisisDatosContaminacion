import random

def generarDatosCalidadAire():

    listaDatos=[]
    for  i in range(1000):
    
        nombre=random.choice(['ana perez','jose jimenez','martha lucrecia','marco polo','alfonso parra','karen andrea'])
        comuna=random.randint(1,14)
        fecha=random.choice(['2024-05-16','2024-06-17','20204-05-15'])
        correo=random.choice(['correo1@correo.com','correo2@correo.com','correo3@correo.com','correo@correo4.com','correo5@correo.com'])
        ica=random.choice()
        encuesta=random.choice([nombre,comuna,ica,fecha,correo])

        listaDatos.append(encuesta)
       
#comuna
#ICA
#fecha
#correo

    return listaDatos
    





