import random

def generarDatosContaminacionSonora():  
    listaDatos=[]
    for i in range(1000):
        nombre=random.choice(['Camila P','Luciana M','Marthe D','Jose B','Karen F'])
        comuna = random.randint(1,14)
        correo=random.choice(['notiene@correo.com','notiene1@correo.com','notiene2@correo.com','notiene3@correo.com'])
        fecha=random.choice(['2024-05-15','2024-05-16','2024-05-17'])
        direccion = random.choice(['Calle 10 #45-67, Medellín, Antioquia','Carrera 15 #23-45, Medellín, Antioquia','Avenida 7 #12-34, Medellín, Antioquia','Carrera 4 #12-56, Medellín, Antioquia'])
        decibeliosdiurnos = random.randint(0,120)
        decibeliosnocturnos = random.randint(0,180)
        encuesta=[nombre,comuna,correo,fecha,direccion,decibeliosdiurnos,decibeliosnocturnos]
        
        listaDatos.append(encuesta)
    return listaDatos
