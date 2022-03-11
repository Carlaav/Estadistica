import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
data= pd.DataFrame({"Valor":[3,19,10,15,14,12,9,8,11,12,11,12,13,11,14,16],"Media":[11.875,11.875,11.875,11.875,11.875,11.875,11.875,11.875,11.875,11.875,11.875,11.875,11.875,11.875,11.875,11.875],"Desviacion":[-8.875,7.125,-1.875,3.125,2.125,0.125,-2.875,-3.875,-0.875,0.125,-0.875,0.125,1.125,-0.875,2.125,4.125],"Desviacion al cuadrado":[78.765625,50.765625,3.515625,9.765625,4.515625,0.015625,8.265625,15.015625,0.765625,0.015625,0.765625,0.015625,1.265625,0.765625,4.515625,17.015625]})


def ejercicioFrutero(data):
    #Quitamos la fila con el valor mas bajo, en este caso la primera 
    data = data.drop([0])

    #Mostramos la desviacion tipica de 
    desviacion = data["Valor"].std()
    
    prop = (18-11.875)/desviacion
    
    
    #Mostramos en lineas donde estaria dicho valor en la graficad de distribucion normal
    plt.figure(figsize=(8, 8))
    sns.histplot(data=data, x= "Desviacion")
    plt.axvline(prop, color = "red")
    plt.axvline(-prop, color = "red")