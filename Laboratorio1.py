import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# Generar datos sintéticos para el ejemplo
np.random.seed(0)
X = 2 * np.random.rand(500, 1)  # Variable independiente (tamaño de la vivienda)
y = 5 + 3 * X + np.random.randn(500, 1)  # Variable dependiente (precio de la vivienda)

# Dividir los datos en conjunto de entrenamiento y conjunto de prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear y entrenar el modelo de regresión lineal
model = LinearRegression()
model.fit(X_train, y_train)

# Hacer predicciones con el conjunto de prueba
y_pred = model.predict(X_test)

# Calcular y mostrar el error cuadrático medio (MSE) y el coeficiente de determinación (R2)
print("MSE:", mean_squared_error(y_test, y_pred))
print("R2:", r2_score(y_test, y_pred))

# Visualizar los resultados en un gráfico
plt.scatter(X_test, y_test, color='red', label='Datos de prueba')
plt.plot(X_test, y_pred, color='black', label='Predicciones')
plt.title('Regresión Lineal Simple')
plt.xlabel('Tamaño de la vivienda')
plt.ylabel('Precio de la vivienda')
plt.legend()
plt.show()
