# Importar las bibliotecas necesarias
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Generar datos de ejemplo
np.random.seed(0)
num_observaciones = 27
size = np.random.uniform(40, 200, (num_observaciones, 1))  # Tamaño de vivienda entre 40 y 200 metros cuadrados
price = 100 + 0.6 * size + np.random.normal(0, 20, (num_observaciones, 1)) # Precio de la vivienda

# Dividir los datos en conjuntos de entrenamiento y prueba
size_train, size_test, price_train, price_test = train_test_split(size, price, test_size=0.2, random_state=0)

# Mostrar los datos de entrenamiento en un gráfico de dispersión
plt.scatter(size_train, price_train, color='blue')
plt.title('Datos de Entrenamiento')
plt.xlabel('Tamaño de la vivienda')
plt.ylabel('Precio de la vivienda')
plt.show()

# Mostrar los datos de prueba en un gráfico de dispersión
plt.scatter(size_test, price_test, color='blue')
plt.title('Datos de Prueba')
plt.xlabel('Tamaño de la vivienda')
plt.ylabel('Precio de la vivienda')
plt.show()

# Crear el modelo de regresión lineal
modelo = LinearRegression()

# Entrenar el modelo con los datos de entrenamiento
modelo.fit(size_train, price_train)

# Realizar predicciones utilizando el conjunto de prueba
price_pred = modelo.predict(size_test)

# Calcular el MSE y R^2
mse = mean_squared_error(price_test, price_pred)
r2 = r2_score(price_test, price_pred)

print("Mean Squared Error (MSE):", mse)
print("Coefficient of determination (R^2):", r2)

# Visualizar los resultados
plt.scatter(size_test, price_test, color='blue')
plt.plot(size_test, price_pred, color='red')
plt.title('Regresión Lineal Simple')
plt.xlabel('Tamaño de la vivienda')
plt.ylabel('Precio de la vivienda')
plt.text(0.95, 0.05, f"MSE: {mse:.2f}\nR²: {r2:.2f}", fontsize=12, color='red', transform=plt.gca().transAxes, ha='right')

plt.show()
