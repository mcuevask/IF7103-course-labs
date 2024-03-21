import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# Generar datos de entrenamiento
np.random.seed(0)
num_datos = 100
tamaño_vivienda = np.random.randint(80, 250, num_datos).reshape(-1, 1)  # Generar tamaños entre 80 y 250 m^2
precio_vivienda = 10000 + 300 * tamaño_vivienda + np.random.normal(0, 5000, (num_datos, 1))  # Generar precios con ruido

# Crear un modelo de regresión lineal
modelo = LinearRegression()

# Entrenar el modelo con los datos
modelo.fit(tamaño_vivienda, precio_vivienda)

# Coeficiente de regresión y término independiente
coeficiente = modelo.coef_[0]
intercepto = modelo.intercept_

# Imprimir los coeficientes
print(f"Coeficiente de regresión: {coeficiente}")
print(f"Término independiente: {intercepto}")

# Predecir el precio de una vivienda de 160 metros cuadrados
tamanio_nueva_vivienda = np.array([[160]])
precio_predicho = modelo.predict(tamanio_nueva_vivienda)

print(f"Precio predicho para una vivienda de 160 m^2: ${precio_predicho[0]}")

# Predicciones en los datos de entrenamiento
predicciones_entrenamiento = modelo.predict(tamaño_vivienda)

# Calcular el Error Cuadrático Medio (MSE)
mse = mean_squared_error(precio_vivienda, predicciones_entrenamiento)
print(f"Error Cuadrático Medio (MSE): {mse}")

# Calcular el coeficiente de determinación (R^2)
r2 = r2_score(precio_vivienda, predicciones_entrenamiento)
print(f"Coeficiente de determinación (R^2): {r2}")

# Graficar los datos y la línea de regresión
plt.scatter(tamaño_vivienda, precio_vivienda, color='black')
plt.plot(tamaño_vivienda, modelo.predict(tamaño_vivienda), color='blue', linewidth=2)
plt.xlabel('Tamaño de la vivienda (m^2)')
plt.ylabel('Precio de la vivienda ($)')
plt.title('Regresión Lineal Simple')
plt.show()
