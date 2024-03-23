# Paso 1: Importar las bibliotecas necesarias
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

# Paso 2: Generar datos de ejemplo
np.random.seed(0)
X = 2 * np.random.rand(100, 1)  # Variables independientes
y = 3 + 4 * X + np.random.randn(100, 1)  # Variable dependiente

# Paso 3: Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Paso 4: Crear y entrenar el modelo de regresión lineal
model = LinearRegression()
model.fit(X_train, y_train)

# Paso 5: Hacer predicciones
y_pred = model.predict(X_test)

# Paso 6: Calcular el error cuadrático medio y el coeficiente de determinación (R^2)
mse = mean_squared_error(y_test, y_pred)
print("Error Cuadrático Medio:", mse)
r_squared = model.score(X_test, y_test)
print("Coeficiente de determinación (R^2):", r_squared)

# Paso 7: Visualizar los resultados
plt.scatter(X_test, y_test, color='blue')
plt.plot(X_test, y_pred, color='red')
plt.title('Regresión Lineal Simple')
plt.xlabel('Tamaño casa')
plt.ylabel('Precio Casa')
plt.show()
