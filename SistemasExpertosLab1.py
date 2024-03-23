# Importar las bibliotecas necesarias
#numpy nos permite trabajar con matrices y operaciones matemáticas de forma eficiente.
import numpy as np

#train_test_split de la biblioteca sklearn (Scikit-Learn) y es una función que nos permite dividir nuestro conjunto de datos en dos partes: una para entrenar nuestro modelo y otra para probarlo. 
from sklearn.model_selection import train_test_split

# sklearn.metrics. mean_squared_error calcula el error cuadrático medio, 
#que es una medida de qué tan cerca están las predicciones de los valores reales. 
#r2_score calcula el coeficiente de determinación (R cuadrado), que es una medida de qué tan bien el modelo se ajusta a los datos observados.
from sklearn.metrics import mean_squared_error, r2_score  # Agregar r2_score

# La regresión lineal es un método para modelar la relación entre una variable dependiente y una o más variables independientes ajustando una línea recta a los datos.
# La variable que estamos tratando de predecir se llama la variable dependiente
#  las variables que usamos para predecirla se llaman variables independientes.
from sklearn.linear_model import LinearRegression

# matplotlib es una biblioteca para crear visualizaciones en Python, y pyplot 
# es un módulo dentro de matplotlib que proporciona una interfaz similar a la de MATLAB 
# para trazar gráficos. 
import matplotlib.pyplot as plt

#La línea np.random.seed(0) establece la semilla para el generador de 
#números aleatorios de la biblioteca NumPy en 0
np.random.seed(0)
x = 2* np.random.randn(100,1)
y = 5 + 3 * x + np.random.randn(100,1)


# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(x,y, test_size=0.2, random_state=42)

# Crear el modelo de regresión lineal
modelo = LinearRegression()
# Entrenar el modelo con los datos de entrenamiento
modelo.fit(X_train, y_train)

# Hacer predicciones sobre el conjunto de prueba
predicciones = modelo.predict(X_test)

y_pred = modelo.predict(x)

print("MSE:", mean_squared_error(y,y_pred))
print("R2:", r2_score(y,y_pred))

# Visualización de los resultados
#crea un gráfico de dispersión (scatter plot) donde cada punto representa una observación de nuestros datos de prueba. 
plt.scatter(X_test, y_test, color='blue')

#Esta línea traza una línea sobre el gráfico de dispersión
plt.plot(X_test, predicciones, color='red')

#Establece el título del gráfico como "Regresión Lineal Simple".
plt.title('Regresión Lineal Simple')

#Establece la etiqueta del eje x como "Tamaño de la vivienda (pies cuadrados)"
plt.xlabel('Tamaño de la vivienda (pies cuadrados)')

# Establece la etiqueta del eje y como "Precio de la vivienda".
plt.ylabel('Precio de la vivienda')

#Muestra el grafico
plt.show()

