import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from resolverEjers import resolver

data = pd.DataFrame({"Opinion xi": [5,4,3,2,1,0], "Cantidad de volantes (Ni)": [40,99,145,133,96,40],"Productos(Ni*xi)": [200,396,435,266,96,0], "Ni*((xi-media)^2)":[246.21,217.14,33.54,35.82,221.50,253.81]})

solution = resolver(data)

solution.ejerPeliculas()
