import tkinter as tk
from tkinter import ttk, messagebox
from pymongo import MongoClient

# Se importa el archivo para manejar la base de datos
import Database as db

# Función para limpiar los campos de entrada
def limpiar_campos():
    entrada_sintomas.delete(0, tk.END)
    entrada_enfermedad.delete(0, tk.END)
    entrada_explicacion.delete(0, tk.END)

# Función para agregar un nuevo regla
def agregar_regla():

    nuevo_regla = {
        "sintomas": entrada_sintomas.get().split(','),
        "enfermedad": entrada_enfermedad.get(),
        "explicacion": entrada_explicacion.get()
    }

    db.agregar_regla(nuevo_regla)
    
    messagebox.showinfo("Éxito", "Regla creada con éxito")
    limpiar_campos()
    mostrar_reglas()

# Función para eliminar un regla por su ID
def eliminar_regla(regla_id):
    db.eliminar_regla(regla_id)
    messagebox.showinfo("Éxito", "Regla eliminada correctamente")
    mostrar_reglas()

# Función para mostrar todos los reglas
def mostrar_reglas():
    reglas = db.obtener_reglas()
    # Limpiar la tabla antes de agregar nuevos datos
    for row in tabla.get_children():
        tabla.delete(row)
    # Insertar los reglas en la tabla
    for regla in reglas:
        tabla.insert("", "end", values=(regla['enfermedad'], ', '.join(regla['sintomas']), regla['explicacion']))

# Función para manejar la selección de la fila
def seleccionar_fila(event):
    reglas = db.obtener_reglas()
    item = tabla.selection()[0]
    id_seleccionado = reglas[tabla.index(item)]["_id"]
    eliminar_button.configure(command=lambda id=id_seleccionado: eliminar_regla(id))

# Configuración de la interfaz de usuario
root = tk.Tk()
root.title("CRUD MongoDB")
root.geometry("800x400")

# Etiquetas y campos de entrada
etiqueta_sintomas = tk.Label(root, text="Síntomas (separados por coma):")
etiqueta_sintomas.grid(row=0, column=0, padx=10, pady=5, sticky="w")
entrada_sintomas = tk.Entry(root, width=50)
entrada_sintomas.grid(row=0, column=1, padx=10, pady=5)

etiqueta_enfermedad = tk.Label(root, text="Enfermedad:")
etiqueta_enfermedad.grid(row=1, column=0, padx=10, pady=5, sticky="w")
entrada_enfermedad = tk.Entry(root, width=50)
entrada_enfermedad.grid(row=1, column=1, padx=10, pady=5)

etiqueta_explicacion = tk.Label(root, text="Explicación:")
etiqueta_explicacion.grid(row=2, column=0, padx=10, pady=5, sticky="w")
entrada_explicacion = tk.Entry(root, width=50)
entrada_explicacion.grid(row=2, column=1, padx=10, pady=5)

# Botón para agregar un nuevo regla
boton_agregar = tk.Button(root, text="Agregar regla", command=agregar_regla)
boton_agregar.grid(row=3, column=0, columnspan=2, padx=10, pady=5, sticky="we")

# Tabla para mostrar los reglas
tabla = ttk.Treeview(root, columns=("Enfermedad", "Síntomas", "Explicación"))

tabla.heading("#0", text="")
tabla.heading("Enfermedad", text="Enfermedad")
tabla.heading("Síntomas", text="Síntomas")
tabla.heading("Explicación", text="Explicación")

tabla.column("#0", width=0, stretch=tk.NO)
tabla.column("Enfermedad", anchor=tk.W, width=150)
tabla.column("Síntomas", anchor=tk.W, width=250)
tabla.column("Explicación", anchor=tk.W, width=250)
tabla.grid(row=4, column=0, columnspan=2, padx=10, pady=5, sticky="nsew")

# Configurar evento de selección de la fila
tabla.bind('<ButtonRelease-1>', seleccionar_fila)

# Crear un botón eliminar
eliminar_button = ttk.Button(root, text="Eliminar")
eliminar_button.grid(row=6, column=0, columnspan=2, padx=10, pady=5, sticky="we")

# Barra de desplazamiento
scrollbar = ttk.Scrollbar(root, orient="vertical", command=tabla.yview)
scrollbar.grid(row=4, column=2, sticky="ns")
tabla.configure(yscrollcommand=scrollbar.set)

mostrar_reglas()

# Iniciar la interfaz de usuario
root.mainloop()