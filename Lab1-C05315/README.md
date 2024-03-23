# IF7103-course-labs: LABORATORIOS SISTEMAS EXPERTOS PARA LA ADMINISTRACIÓN 
## Laboratorio 1: REGRESIÓN LINEAL SIMPLE
## Henry Moreno Calderon - C05315

# Funcionamiento de la Aplicación:
La aplicación realiza una regresión lineal simple para predecir el precio de las viviendas basándose en una variable independiente, en este caso, el número de habitaciones. El proceso se lleva a cabo en los siguientes pasos:

1. Generación de Datos Sintéticos: 
Se generan datos sintéticos para el número de habitaciones y el precio de las viviendas. Las habitaciones se generan aleatoriamente entre 1 y 5, y el precio se calcula basándose en el número de habitaciones, con un componente de aleatoriedad.

2. Visualización de los Datos: 
Los datos generados se visualizan utilizando un gráfico de dispersión para entender la relación entre el número de habitaciones y el precio de las viviendas.

3. División del Dataset: 
Se divide el conjunto de datos en un conjunto de entrenamiento y un conjunto de prueba, con un 80% de los datos para entrenamiento y un 20% para prueba. Esto nos permite evaluar el rendimiento del modelo en datos no vistos.

4. Creación y Entrenamiento del Modelo: 
Se crea una instancia de la clase LinearRegression de scikit-learn y se ajusta el modelo a los datos de entrenamiento. En este paso, el modelo aprende la relación entre el número de habitaciones y el precio de las viviendas.

5. Predicción y Evaluación: 
Se utilizan los datos de prueba para predecir los precios de las viviendas utilizando el modelo entrenado. Se calculan métricas de rendimiento, como el error cuadrático medio (MSE) y el coeficiente de determinación (R²), para evaluar el rendimiento del modelo.

6. Visualización de la Regresión: 
Se visualiza la línea de regresión generada por el modelo sobre los datos de prueba para entender cómo se ajusta el modelo a los datos y la relación entre el número de habitaciones y el precio de las viviendas.

# Decisiones de Diseño:
Uso de Datos Sintéticos: Para simplificar el ejemplo, se generaron datos sintéticos en lugar de utilizar un conjunto de datos de la vida real. Esto nos permite demostrar el proceso de regresión lineal simple de manera clara y reproducible.

* Visualización de Datos: Se utilizó un gráfico de dispersión para visualizar los datos y entender la relación entre las variables. Esto proporciona una forma intuitiva de interpretar los datos y la calidad del ajuste del modelo.

* División del Dataset: Se dividió el conjunto de datos en un conjunto de entrenamiento y un conjunto de prueba para evaluar el rendimiento del modelo en datos no vistos. Esto ayuda a evitar el sobreajuste y proporciona una estimación realista del rendimiento del modelo en situaciones reales.

* Evaluación del Modelo: Se utilizaron métricas de rendimiento estándar, como el error cuadrático medio (MSE) y el coeficiente de determinación (R²), para evaluar el rendimiento del modelo. Estas métricas proporcionan una medida cuantitativa de la calidad de las predicciones del modelo.

* Visualización de la Regresión: Se visualizó la línea de regresión sobre los datos de prueba para entender cómo se ajusta el modelo a los datos y la relación entre las variables. Esto proporciona una forma intuitiva de interpretar el modelo y comunicar los resultados.

## Al seguir estas decisiones de diseño y pasos de funcionamiento, la aplicación proporciona una demostración clara y concisa del proceso de regresión lineal simple y su aplicación en la predicción del precio de las viviendas basándose en el número de habitaciones.