## Importación de Librerías

![](resources/librerias.png)
- **Numpy (np)**: Es una biblioteca fundamental para la computación científica en Python. Proporciona soporte para matrices multidimensionales, junto con una amplia variedad de funciones matemáticas.
- **scikit-learn (sklearn)**: Scikit-learn es una biblioteca de aprendizaje automático (machine learning) para Python que proporciona herramientas simples y eficientes para el análisis predictivo de datos. Incluye una variedad de algoritmos de aprendizaje supervisado y no supervisado.
- **matplotlib.pyplot (plt)**: Matplotlib es una biblioteca de visualización en Python que se utiliza comúnmente para crear gráficos estáticos, gráficos interactivos y visualizaciones de datos.

## Generación de datos de ejemplo
![](resources/datos_ejemplo.png)
- **np.random.seed(0)**: Establece la semilla para el generador de números aleatorios de NumPy.
- **tamano_vivienda**: Representa la variable independiente del modelo.
- **precio_vivienda**: Representa la variable dependiente del modelo, es decir cambiará en función a la variable independiente.

## Dividir los datos en conjuntos de entrenamiento y prueba
![](resources/dividir.png)
- **train_test_split**: Divide un conjunto de datos en conjuntos de entrenamiento y prueba.
- **test_size**: Especifica el tamaño que tendrá el conjunto de prueba. Es decir, el porcentaje de datos que se utilizarán como conjunto de prueba y el restante como conjunto de entrenamiento.
- **random_state**: Esto establece la semilla para el generador de números aleatorios que se utiliza internamente en la función. La misma semilla representa que se obtendrán los mismos datos en caso de replicar.
- **X_train**: Variables independientes de entrenamiento.
- **X_test**: Variables independientes de prueba.
- **Y_train**: Variables dependientes de entrenamiento.
- **Y_test**: Variables dependientes de prueba.

## Crear y entrenar el modelo (Regresión Lineal)
![](resources/crear_modelo.png)
- **model = LinearRegression()**: Esto crea una instancia del modelo de regresión lineal.
- **model.fit()**: Esta línea de código entrena el modelo utilizando los datos de entrenamiento. El método 'fit()' ajusta el modelo a los datos de entrenamiento, es decir, encuentra los coeficientes óptimos para la línea o hiperplano.

## Hacer predicciones
![](resources/predicciones.png)
- **model.predict()**: Utiliza el método 'predict()' del modelo de regresión lineal ('model') para realizar predicciones sobre los valores independientes de prueba (X_test).
- **y_pred**: Las predicciones resultantes se asignan a la variable 'y_pred'. 

## Calcular el error cuadrático medio
![](resources/error_cuadratico.png)
- **mean_squared_error()**: Este es un método de la biblioteca scikit-learn (sklearn) que calcula el Error Cuadrático Medio (MSE) entre los valores reales dependientes del conjunto de prueba y las predicciones del modelo.
- **mse**: El valor del MSE se almacena en esta variable.

## Calcular el coeficiente de determinación
![](resources/coeficiente_determinacion.png)
- **r2_score**: Este es un método de la biblioteca scikit-learn que calcula el Coeficiente de Determinación (R-Cuadrado), esta es una medida de qué tan bien las predicciones del modelo se ajustan a los datos reales y varía entre 0 y 1. Entre más cercano a 1 indica un mejor ajuste del modelo a los datos.
- **r2**: Almacena el valor del Coeficiente de Determinación.

## Visualizar los resultados
![](resources/resultados.png)
- **plt.scatter**: Este comando traza un diagrama de dispersión de los datos de prueba. Cada punto en el gráfico representa una observación del conjunto de prueba, el eje x siendo el tamaño de la vivienda y el eje y el precio de la vivienda.
- **plt.plot**: Este comando traza la línea de regresión lineal sobre los datos de prueba. 
- **plt.title()**: Este comando establece el título del gráfico.
- **plt.xlabel()**: Este comando establece la etiqueta del eje x.
- **plt.ylabel()**: Este comando establece la etiqueta del eje y.
- **plt.show()**: Este comando muestra el gráfico completo con todas las características configuradas.

## Gráfica
![](resources/grafica.png)

- **Línea Roja**: Representa las predicciones realizadas con el modelo y los datos de entrenamiento, en términos simples cuando el tamaño de la vivienda aumenta también lo hará el precio.
- **Puntos Azules**: Representa los datos reales tomados de los datos de prueba, entre más alejados estén de la línea roja mayor diferencia habrá entre los datos reales y las predicciones.
