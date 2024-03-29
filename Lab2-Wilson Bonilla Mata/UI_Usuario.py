import tkinter as tk
from tkinter import messagebox

# Se importan el archivos necesarios
import Database as db
import Motor_Inferencia as mi

def diagnosticar_enfermedades():
    # Obtener los síntomas ingresados
    sintomas = entrada_sintomas.get().split(",")

    # Convertir la lista en diccionario
    sintomas_dict = dict()
    for sintoma in sintomas:
        sintomas_dict[sintoma] = True

    # Se obtienen las reglas de la base de datos
    reglas = db.obtener_lista_reglas()
    
    # Se evaluan los sisntomas para brindar un diagnostico
    enfermedades, explicaciones = mi.motor_inferencias(reglas,sintomas_dict)

    mensaje = ""

    # Se muestra el diagnostico en caso de existir uno
    if enfermedades:
        for enfermedad, explicacion in zip(enfermedades, explicaciones):
            mensaje += f"Enfermedad: {enfermedad} \n"
            mensaje += f"Explicación: {explicacion} \n\n"
    else:
        mensaje += f"Enfermedad: Ninguna \n Explicación: No hay diagnostico \n\n"

    # Mostrar el mensaje del diagnóstico
    messagebox.showinfo("Diagnósticos de las Enfermedades en la Planta \n",mensaje)

# Crear la ventana principal
root = tk.Tk()
root.title("Diagnóstico de Enfermedad")

# Etiqueta y entrada para ingresar los síntomas
etiqueta_sintomas = tk.Label(root, text="Ingrese los síntomas (separados por coma): ")
etiqueta_sintomas.pack()
entrada_sintomas = tk.Entry(root, width=50)
entrada_sintomas.pack()

# Botón para diagnosticar la enfermedad
boton_diagnosticar = tk.Button(root, text="Diagnosticar Enfermedad", command=diagnosticar_enfermedades)
boton_diagnosticar.pack()

# Ejecutar el bucle de eventos de la root
root.mainloop()