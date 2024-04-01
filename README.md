# IF7103-course-labs: LABORATORIOS SISTEMAS EXPERTOS PARA LA ADMINISTRACIÓN 
## Laboratorio 2: Implementación de un Motor de Inferencia

## Objetivos
- Desarrollar habilidades en la programación con Python para el manejo de interfaces gráficas de usuario (GUI) con Tkinter y la manipulación de datos con Pandas.
- Comprender y aplicar conceptos básicos de sistemas expertos, específicamente en lo que respecta al diseño y funcionamiento de un motor de inferencia.
- Aprender a definir y utilizar reglas de inferencia.
- Practicar la lectura de datos desde archivos externos, en este caso, un archivo Excel, para el uso dentro de aplicaciones Python.

## Descripción

En este laboratorio, crearás una aplicación de escritorio que funcione como un sistema experto simplificado para el diagnóstico de enfermedades en plantas. Utilizando Tkinter para la interfaz de usuario, Pandas para el manejo de datos y un conjunto de reglas de diagnóstico definidas, la aplicación evaluará la información de sintomatología extraída de un archivo Excel y presentará los diagnósticos correspondientes al usuario.

## Requisitos Previos
- Instalación de Python en tu computadora.
- Conocimientos básicos de programación en Python, incluyendo el manejo de listas, diccionarios, y estructuras de control.
- Familiaridad con las bibliotecas Tkinter y Pandas.
- Asegúrate de tener instaladas las bibliotecas necesarias: Tkinter (usualmente viene con Python), Pandas, y Openpyxl. Puedes instalar Pandas y Openpyxl con el comando `pip install pandas openpyxl`.

## Parte 1: Configuración Inicial
1. Crea un archivo Python nuevo y asegúrate de que tienes acceso a un ambiente de desarrollo adecuado para ejecutar código Python.
2. Instala las dependencias necesarias mencionadas en los requisitos previos, si aún no lo has hecho.

## Parte 2: Diseño del Motor de Inferencia
1. Define un conjunto de reglas de diagnóstico para diferentes enfermedades en plantas. Cada regla debe incluir un conjunto de síntomas presentes y ausentes, y un diagnóstico con su explicación correspondiente.
2. Implementa una función `evaluar_reglas` que reciba como entrada los síntomas de una planta y las reglas de diagnóstico, y retorne los diagnósticos y explicaciones aplicables basados en los síntomas proporcionados.

## Parte 3: Interfaz Gráfica de Usuario
1. Utiliza Tkinter para crear una interfaz gráfica que muestre los diagnósticos de enfermedades en plantas. La interfaz debe incluir un componente para listar las plantas evaluadas junto con sus diagnósticos y explicaciones.
2. Implementa la funcionalidad necesaria para cargar los síntomas de las plantas desde un archivo Excel y actualizar la interfaz gráfica con los resultados del diagnóstico.

## Parte 4: Pruebas y Experimentación
1. Crea un archivo Excel con datos de prueba, que incluya los síntomas observados en diferentes plantas, siguiendo el formato esperado por tu aplicación.
2. Ejecuta tu aplicación, carga los datos desde el archivo Excel y verifica que los diagnósticos se generen y muestren correctamente en la interfaz gráfica.

## Parte 5: Reflexión y Mejoras
- Reflexiona sobre el proceso de implementación del motor de inferencia y la GUI. ¿Qué desafíos encontraste y cómo los superaste?
- Considera posibles mejoras para tu aplicación. Algunas ideas incluyen agregar la capacidad de modificar las reglas de diagnóstico directamente desde la interfaz gráfica o implementar funcionalidades adicionales para manejar diferentes tipos de plantas.

## Entrega
- Código fuente.
- Documentación que describa el funcionamiento de la aplicación y las decisiones de diseño tomadas durante el desarrollo.
- Archivo Excel utilizado para las pruebas, incluyendo una breve explicación de cada conjunto de datos de prueba.
