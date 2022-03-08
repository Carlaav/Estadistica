import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.DataFrame({"Opinion xi": [5,4,3,2,1,0], "Cantidad de volantes (Ni)": [40,99,145,133,96,40],"Productos(Ni*xi)": [200,396,435,266,96,0], "Ni*((xi-media)^2)":[246.21,217.14,33.54,35.82,221.50,253.81]})

def media_ponderada(data):
    suma = 0
    for i in range(len(data["Cantidad de volantes (Ni)"])):
        suma = suma + data["Cantidad de volantes (Ni)"][i] * data["Opinion xi"][i]
    
    count=0
    for i in data["Cantidad de volantes (Ni)"]:
        count= count+ i
    
    media= suma/count
    return media

def varianza(data):
    count=0
    for i in data["Ni*((xi-media)^2)"]:
        count= count+i
    
    varianza = count/data["Cantidad de volantes (Ni)"].sum()
    return varianza

def visualizacion(media, desviacion):
    print("el 68% de los datos estan entre:", media-desviacion, "y", media+desviacion)
    print("el 95% de los datos estan entre:", media-2*desviacion, "y", media+2*desviacion)
    print("el 99.7% de los datos estan entre:", media-3*desviacion, "y", media+3*desviacion)
    
    
def grafica(data):
    plt.figure(figsize = ((10,10)))
    sns.barplot(data = data, x = "Opinion xi", y="Cantidad de volantes (Ni)", color = "Blue")
    sns.lineplot(data = data, x = "Opinion xi", y="Cantidad de volantes (Ni)", color = "Orange")

media_ponderada(data)
x=varianza(data)
desviacion= x**0.5
visualizacion(media_ponderada(data), desviacion)
grafica(data)