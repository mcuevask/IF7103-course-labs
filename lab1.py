# Importar las bibliotecas necesarias
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Generar datos de ejemplo
np.random.seed(0)
X = 2 * np.random.rand(100, 1)  # Tamaño de la vivienda (variable independiente)
y = 5 + 3 * X + np.random.randn(100, 1)  # Precio de la vivienda (variable dependiente)

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear un modelo de regresión lineal
model = LinearRegression()

# Entrenar el modelo
model.fit(X_train, y_train)

# Coeficientes del modelo
print("Intercepto (error cuadratico):", model.intercept_)
print("Coeficiente de determinación:", model.coef_[0])

# Hacer predicciones
y_pred = model.predict(X_test)

# Visualización de los datos y la línea de regresión
plt.scatter(X_test, y_test, color='black')
plt.plot(X_test, y_pred, color='blue', linewidth=3)
plt.xlabel('Tamaño de la vivienda')
plt.ylabel('Precio de la vivienda')
plt.title('Regresión Lineal Simple')
plt.show()
