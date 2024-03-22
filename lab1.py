# Importar las bibliotecas necesarias
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Generar datos sintéticos para el ejemplo
np.random.seed(0)
X = 2 * np.random.rand(100, 1)  # Variable independiente (tamaño de la vivienda)
y = 5 + 3 * X + np.random.randn(100, 1)  # Variable dependiente (precio de la vivienda)

# Dividir los datos en conjunto de entrenamiento y conjunto de prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear un modelo de regresión lineal
model = LinearRegression()

# Entrenar el modelo con el conjunto de entrenamiento
model.fit(X_train, y_train)

# Hacer predicciones con el conjunto de prueba
y_pred = model.predict(X_test)

print("MSE:", mean_squared_error(y_test, y_pred))
print("R2:", r2_score(y_test, y_pred))

# Visualizar los resultados
plt.scatter(X_test, y_test, color='blue')
plt.plot(X_test, y_pred, color='red')
plt.title('Regresión Lineal Simple')
plt.xlabel('Tamaño de la vivienda')
plt.ylabel('Precio de la vivienda')
plt.show()

