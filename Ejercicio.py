# Importar las bibliotecas necesarias
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Generar datos de ejemplo
np.random.seed(0)
tamaño_vivienda = np.random.randint(1000, 3000, 100).reshape(-1, 1)
precio_vivienda = 50 * tamaño_vivienda + np.random.normal(0, 20000, 100).reshape(-1, 1)

# Dividir los datos en conjunto de entrenamiento y conjunto de prueba
X_train, X_test, y_train, y_test = train_test_split(tamaño_vivienda, precio_vivienda, test_size=0.2, random_state=0)

# Crear el modelo de regresión lineal
modelo = LinearRegression()
# Entrenar el modelo con los datos de entrenamiento
modelo.fit(X_train, y_train)

# Realizar predicciones sobre el conjunto de prueba
y_pred = modelo.predict(X_test)

# Calcular el error cuadrático medio entre las predicciones y los valores reales
mse = mean_squared_error(y_test, y_pred)
r_squared = modelo.score(X_test, y_test)

print("R^2:", r_squared)
print("MSE:", mse)

# Visualizar los resultados
plt.scatter(X_test, y_test, color='blue')
plt.plot(X_test, y_pred, color='red', linewidth=2)
plt.title('Regresión Lineal Simple')
plt.xlabel('Tamaño de la Vivienda')
plt.ylabel('Precio de la Vivienda')
plt.show()