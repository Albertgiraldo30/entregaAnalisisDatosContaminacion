import random

def contadordeArboles():  
    listaDatos=[]
    for i in range(1000):
        nombre=random.choice(['Camila P','Luciana M','Marthe D','Jose B','Karen F'])
        corregimiento = random.randint(1,14)
        correo=random.choice(['notiene@correo.com','notiene1@correo.com','notiene2@correo.com','notiene3@correo.com'])
        fecha=random.choice(['2024-05-15','2024-05-16','2024-05-17'])
        hectareassembradas = random.choice(0,120)
        especiesembrada=random.choice(['Pino','Naranja','Manzana'])
        encuesta =[nombre,corregimiento,correo,fecha,hectareassembradas,especiesembrada]

   
    
        
        listaDatos.append(encuesta)
    return listaDatos
