#Importar las bibliotecas
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt


#carga de datos
datos = pd.read_csv('datos.csv')


#Dividir los datos en conjuntos de entrenamiento y prueba:
X = datos['metros_cuadrados'].values.reshape(-1, 1)
y = datos['precio_vivienda'].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


#Crear y entrenar el modelo de regresión lineal:
modelo = LinearRegression()
modelo.fit(X_train, y_train)

#Realizar predicciones y evaluar el modelo:
predicciones = modelo.predict(X_test)
error = mean_squared_error(y_test, predicciones)
print('Error cuadrático medio:', error)


#Visualizar los resultados:
plt.scatter(X_test, y_test, color='blue')
plt.plot(X_test, predicciones, color='red', linewidth=3)
plt.xlabel('Metros cuadrados')
plt.ylabel('Precio vivienda')
plt.title('Modelo de regresión lineal')
plt.show()
