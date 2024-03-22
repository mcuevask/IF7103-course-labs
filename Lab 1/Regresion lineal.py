import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error, r2_score  
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Datos de ejemplo (tamaño de la vivienda y precio)
np.random.seed(0)
X= 2*np.random.rand(100,1)
Y= 5+3*X+np.random.rand(100,1)


# Dividir los datos en conjunto de entrenamiento y conjunto de prueba
X_train, X_test, y_train, y_test = train_test_split(X,Y, test_size=0.2, random_state=42)

# Crear el modelo de regresión lineal
modelo = LinearRegression()

# Entrenar el modelo
modelo.fit(X_train, y_train)

# Hacer predicciones
y_pred = modelo.predict(X_test)



# Evaluar el modelo
mse = mean_squared_error(y_test, y_pred)
print("Error cuadrático medio:", mse)
print("R2:", r2_score(y_test, y_pred))

# Visualización de los datos y el modelo
plt.scatter(X_test, y_test, color='blue')
plt.plot(X_test, y_pred, color='red')
plt.title('Regresión Lineal Simple')
plt.xlabel('Tamaño de la vivienda (pies cuadrados)')
plt.ylabel('Precio de la vivienda ($)')
plt.show()
