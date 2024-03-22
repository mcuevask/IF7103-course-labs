import numpy as np  # Importa la biblioteca NumPy para manipulación de datos numéricos
from sklearn.linear_model import LinearRegression  # Importa la clase LinearRegression de scikit-learn
from sklearn.metrics import mean_squared_error  # Importa la función mean_squared_error para calcular el MSE
import matplotlib.pyplot as plt  # Importa matplotlib para visualización de datos
import pandas as pd  # Importa pandas para trabajar con datos en formato Excel

# Establece una semilla aleatoria para reproducibilidad de resultados
np.random.seed(0)

# Genera datos sintéticos para el ejemplo (entrenamiento)
X_train = np.linspace(0, 10, 100).reshape(-1, 1)  # Tamaño de vivienda 
y_train = 3 * X_train + 2 + np.random.normal(0, 1, size=X_train.shape) 

# Genera datos de prueba
X_test = np.linspace(0, 10, 20).reshape(-1, 1)  # Tamaño de vivienda para pruebas
y_test = 3 * X_test + 2 + np.random.normal(0, 1, size=X_test.shape)  # Precio de vivienda para pruebas

# Guarda los datos de entrenamiento y prueba en archivos Excel
train_df = pd.DataFrame({'Tamaño de vivienda': X_train.flatten(), 'Precio de vivienda': y_train.flatten()})
test_df = pd.DataFrame({'Tamaño de vivienda': X_test.flatten(), 'Precio de vivienda': y_test.flatten()})
train_df.to_csv('train_data.xlsx', index=False)
test_df.to_csv('test_data.xlsx', index=False)

# Crea un objeto de regresión lineal y entrena el modelo
model = LinearRegression()
model.fit(X_train, y_train)

# Realiza predicciones sobre los datos de prueba
y_pred = model.predict(X_test)

# Calcula el Error Cuadrático Medio (MSE) y el Coeficiente de Determinación (R^2)
mse = mean_squared_error(y_test, y_pred)
r2 = model.score(X_test, y_test)

# Visualiza los datos de entrenamiento y la línea de regresión
plt.scatter(X_train, y_train, color='blue', label='Entrenamiento')  # Puntos de entrenamiento
plt.scatter(X_test, y_test, color='green', label='Pruebas')  # Puntos de prueba
plt.plot(X_train, model.predict(X_train), color='red', linewidth=2, label='Regresión')  # Línea de regresión
plt.xlabel('Tamaño de vivienda')  # Etiqueta del eje x
plt.ylabel('Precio de vivienda')  # Etiqueta del eje y
plt.title('Regresión Lineal Simple')  # Título del gráfico
plt.legend()  # Muestra la leyenda
plt.show()  # Muestra el gráfico

# Imprime y guarda los resultados
print(f"Error Cuadrático Medio (MSE): {mse}")
print(f"Coeficiente de Determinación (R^2): {r2}")
results_df = pd.DataFrame({'Error Cuadrático Medio (MSE)': [mse], 'Coeficiente de Determinación (R^2)': [r2]})
results_df.to_csv('results.xlsx', index=False)
