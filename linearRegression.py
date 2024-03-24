# Paso 1: Importar las bibliotecas necesarias
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Paso 2: Cargar el dataset
# Supongamos que tienes un archivo CSV llamado 'datos.csv' con dos columnas: 'tamaño_vivienda' y 'precio_vivienda'
data = pd.read_excel('datosGenerados.xlsx')

# Paso 3: Explorar y visualizar los datos
plt.scatter(data['tamanioVivienda'], data['precioVivienda'])
plt.xlabel('Tamaño de la vivienda')
plt.ylabel('Precio de la vivienda')
plt.title('Relación entre el tamaño y el precio de la vivienda')
plt.show()

# Paso 4: Dividir el dataset en conjunto de entrenamiento y conjunto de prueba
X = data['tamanioVivienda'].values.reshape(-1, 1)  # Variable independiente
y = data['precioVivienda'].values.reshape(-1, 1)  # Variable dependiente

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Paso 5: Construcción del Modelo
model = LinearRegression()
model.fit(X_train, y_train)

# Paso 6: Evaluación del Modelo
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print("Error cuadrático medio (MSE):", mse)
print("Coeficiente de determinación (R²):", r2)

# Paso 7: Visualización
plt.scatter(X_test, y_test)
plt.plot(X_test, y_pred, color='red')
plt.xlabel('Tamaño de la vivienda')
plt.ylabel('Precio de la vivienda')
plt.title('Predicción de precios de vivienda utilizando regresión lineal')
plt.show()




