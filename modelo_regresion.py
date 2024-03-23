#Importar las bibliotecas
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error, r2_score


# Generar datos aleatorios para metros cuadrados y precio de vivienda
np.random.seed(0)  # Fijar la semilla para reproducibilidad
metros_cuadrados = np.random.randint(50, 300, 100)  # Generar 100 valores aleatorios entre 50 y 300
precio_vivienda = 1000 * metros_cuadrados + np.random.randint(-5000, 5000, 100)  # Generar precios aleatorios con algo de ruido

# Crear un DataFrame con los datos
datos = pd.DataFrame({'metros_cuadrados': metros_cuadrados, 'precio_vivienda': precio_vivienda})

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
print('Error cuadrático medio (MSE):', error)

# Calcular predicciones
predicciones = modelo.predict(X_test)

# Calcular el coeficiente de determinación (R²)
r2 = r2_score(y_test, predicciones)
print('Coeficiente de determinación (R²):', r2)

#Visualizar los resultados:
plt.scatter(X_test, y_test, color='blue')
plt.plot(X_test, predicciones, color='red', linewidth=3)
plt.xlabel('Metros cuadrados')
plt.ylabel('Precio vivienda')
plt.title('Modelo de regresión lineal')
plt.show()


