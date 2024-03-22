# IF7103-course-labs
LAB 1
JAFETH MATAMOROS CORDERO
 C04657

 ## Introducción
Este documento describe el proceso de construcción de un modelo de regresión lineal simple en Python utilizando la biblioteca scikit-learn. El objetivo principal es predecir el precio de una vivienda basándose en su tamaño, utilizando datos sintéticos generados para este propósito.


## Pasos del Ejercicio

### 1. Preparación de los Datos
- **Importar Bibliotecas:**
  - Se importaron las bibliotecas necesarias, incluyendo NumPy, pandas, scikit-learn y matplotlib para manipulación de datos, creación del modelo, evaluación del modelo y visualización de resultados.
  

```python
import numpy as np  # Importa la biblioteca NumPy para manipulación de datos numéricos
from sklearn.linear_model import LinearRegression  # Importa la clase LinearRegression de scikit-learn
from sklearn.metrics import mean_squared_error  # Importa la función mean_squared_error para calcular el MSE
import matplotlib.pyplot as plt  # Importa matplotlib para visualización de datos
import pandas as pd  # Importa pandas para trabajar con datos en formato Excel

```

- **Generación de Datos :**
  - Se generaron datos  para el tamaño de la vivienda (variable independiente) y el precio de la vivienda  para el conjunto de entrenamiento y prueba.

- **Guardado de Datos:**
  - Los datos de entrenamiento y prueba se guardaron en archivos Excel ("train_data.xlsx" y "test_data.xlsx") utilizando pandas.Esto para tener un registro de la prueba.

```python

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
```



### 2. Preprocesamiento de Datos
- **División del Dataset:**
  - Se dividió el dataset en un conjunto de entrenamiento y un conjunto de prueba utilizando la función `train_test_split` de scikit-learn.

- Al utilizar la función train_test_split de scikit-learn, se divide el dataset en dos conjuntos: uno para entrenamiento y otro para prueba. Esto es fundamental para evaluar la capacidad de generalización del modelo.
### 3. Construcción del Modelo
- **Creación del Modelo:**
  - Se importó y utilizó la clase `LinearRegression` de scikit-learn para crear el modelo de regresión lineal simple.

- **Entrenamiento del Modelo:**
  - El modelo se entrenó utilizando los datos de entrenamiento.
```python
# Crea un objeto de regresión lineal y entrena el modelo
model = LinearRegression()
model.fit(X_train, y_train)
```
### 4. Evaluación del Modelo
- **Predicción y Métricas de Rendimiento:**
  - Se realizaron predicciones sobre los datos de prueba y se calcularon métricas de rendimiento como el Error Cuadrático Medio (MSE) y el Coeficiente de Determinación (R²) para evaluar el modelo.
``` python
  # Realiza predicciones sobre los datos de prueba
y_pred = model.predict(X_test)

# Calcula el Error Cuadrático Medio (MSE) y el Coeficiente de Determinación (R^2)
mse = mean_squared_error(y_test, y_pred)
r2 = model.score(X_test, y_test)
```

### 5. Visualización
- **Visualización de Resultados:**
  - Se visualizó la línea de regresión sobre los datos de prueba para comprender cómo el modelo se ajusta a los datos.

- Y se guarda en un archivo de excel los datos de Error Cuadrático Medio (MSE) y Coeficiente de Determinación.

``` python

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


```