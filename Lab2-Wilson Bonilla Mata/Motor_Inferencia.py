# Importación de librerias
import pandas as pd
import tkinter as tk
from tkinter import ttk

# Se importa el archivo para obtener los datos
import Database as db

# Leer el archivo Excel
df = pd.read_excel("entradas_plantas.xlsx")

# Función del motor de inferencias
def motor_inferencias(reglas, entrada):
    enfermedades = []
    explicaciones = []
    for regla in reglas:
        cumple = True
        for sintoma in regla['sintomas']:
            if not entrada.get(sintoma):
                cumple = False
                break
        if cumple:
            enfermedades.append(regla['enfermedad'])
            explicaciones.append(regla['explicacion'])
    return enfermedades, explicaciones

# Crear ventana principal
root = tk.Tk()
root.title("Diagnósticos de Enfermedades en Plantas")

# Crear una tabla
tabla = ttk.Treeview(root, columns=("Entrada", "Diagnostico", "Explicacion"), show="headings")

tabla.heading("Entrada", text="Entrada")
tabla.heading("Diagnostico", text="Diagnóstico")
tabla.heading("Explicacion", text="Explicación")

tabla.column("Entrada", width=50)
tabla.column("Diagnostico", width=200)
tabla.column("Explicacion", width=500)

tabla.grid(row=0, column=0, padx=10, pady=10)

# Iterar sobre las entradas y mostrar los diagnósticos en la tabla
for index, row in df.iterrows():
    reglas = db.obtener_lista_reglas()
    entrada = row.to_dict()
    enfermedades, explicaciones = motor_inferencias(reglas, entrada)
    if enfermedades:
        for enfermedad, explicacion in zip(enfermedades, explicaciones):
            tabla.insert("", "end", values=(index + 1, enfermedad, explicacion))
    else:
        tabla.insert("", "end", values=(index + 1, "Ninguno", "No hay diagnóstico"))  

# Función para cerrar la aplicación
def cerrar_app():
    root.destroy()

# Botón para cerrar la aplicación
boton_cerrar = tk.Button(root, text="Cerrar", command=cerrar_app)
boton_cerrar.grid(row=1, column=0, padx=10, pady=10)

# Ejecutar el bucle de eventos principal
root.mainloop()