import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

class resolver:
    def __init__(self, data):
        self.data = data
        
    
    def media_ponderada(self):
        suma = 0
        for i in range(len(self.data["Cantidad de volantes (Ni)"])):
            suma = suma + self.data["Cantidad de volantes (Ni)"][i] * self.data["Opinion xi"][i]
        
        count=0
        for i in self.data["Cantidad de volantes (Ni)"]:
            count= count+ i
        
        media= suma/count
        return media

    def varianza(self):
        count=0
        for i in self.data["Ni*((xi-media)^2)"]:
            count= count+i
        
        varianza = count/self.data["Cantidad de volantes (Ni)"].sum()
        return varianza

    def porcent(media, desviacion):
        print("el 68% de los datos estan entre:", media-desviacion, "y", media+desviacion)
        print("el 95% de los datos estan entre:", media-2*desviacion, "y", media+2*desviacion)
        print("el 99.7% de los datos estan entre:", media-3*desviacion, "y", media+3*desviacion)
        
        
    def grafica(self):
        plt.figure(figsize = ((10,10)))
        sns.barplot(data = self.data, x = "Opinion xi", y="Cantidad de volantes (Ni)", color = "Blue")
        sns.lineplot(data = self.data, x = "Opinion xi", y="Cantidad de volantes (Ni)", color = "Orange")



    def ejerPeliculas(self):
        self.media_ponderada(self.data)
        x=self.varianza(self.data)
        desviacion= x**0.5
        self.porcent(self.media_ponderada(self.data), desviacion)
        self.grafica(self.data)