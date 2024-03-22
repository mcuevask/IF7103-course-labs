import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# Paso 2: Generar datos de ejemplo
np.random.seed(0)
tamano_vivienda = 2 * np.random.rand(100, 1)
precio_vivienda = 3 + 4 * tamano_vivienda + np.random.randn(100, 1)

# Paso 3: Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(tamano_vivienda, precio_vivienda, test_size=0.2, random_state=42)

# Paso 4: Crear y entrenar el modelo de regresión lineal
model = LinearRegression()
model.fit(X_train, y_train)

# Paso 5: Hacer predicciones
y_pred = model.predict(X_test)

# Paso 6: Calcular el error cuadrático medio
mse = mean_squared_error(y_test, y_pred)
print("Error Cuadrático Medio:", mse)

# Paso 7: Calcular el coeficiente de determinación (R-cuadrado)
r2 = r2_score(y_test, y_pred)
print("Coeficiente de Determinación (R-cuadrado):", r2)

# Paso 8: Visualizar los resultados
plt.scatter(X_test, y_test, color='blue')
plt.plot(X_test, y_pred, color='red')
plt.title('Regresión Lineal Simple')
plt.xlabel('Tamaño Vivienda')
plt.ylabel('Precio Vivienda')
plt.show()
