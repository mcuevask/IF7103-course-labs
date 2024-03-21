# Importación de librerias
import pandas as pd
import tkinter as tk
from tkinter import ttk

# Definición de las reglas
reglas = [
    {
        "sintomas": ["manchas_oscuras_hojas", "manchas_oscuras_frutos", "pudricion"],
        "enfermedad": "Antracnosis",
        "explicacion": "Se detectan manchas oscuras en hojas y frutos y prudición"
    },
    {
        "sintomas": ["manchas_oscuras_frutos", "pudricion_acuosa"],
        "enfermedad": "Podredumbre Negra",
        "explicacion": "Se detectan manchas oscuras en frutos y prudición acuosa"
        
    },
    {
        "sintomas": ["manchas_negras_hojas", "reduccion_area_foliar"],
        "enfermedad": "Sigatoka Negra",
        "explicacion": "Se detectan manchas negras en hojas y reducción del area foliar"
    },
    {
        "sintomas": ["manchas_negras_frutos", "manchas_negras_hojas", "defoliacion"],
        "enfermedad": "Mancha de Asfalto",
        "explicacion": "Se detectan manchas negras en frutos y hojas y defoliación"
    },
    {
        "sintomas": ["manchas_negras_hojas", "deformacion_hojas", "deformacion_frutos"],
        "enfermedad": "Mancha Negra",
        "explicacion": "Se detectan manchas negras en hojas y deformación en hojas y frutos"
    },
    {
        "sintomas": ["manchas_amarrilas_hojas", "formacion_lesiones"],
        "enfermedad": "Mancha Angular",
        "explicacion": "Se detectan manchas amarillas o marrones en hojas y formación de lesiones"
    },
    {
        "sintomas": ["marchitez", "necrosis_cogollo", "hojas_sin_abrir"],
        "enfermedad": "Pudricion del Cogollo",
        "explicacion": "Se detecta marchitez, necrosis del cogollo y hojas sin abrir"
    },
    {
        "sintomas": ["marchitez", "decoloracion", "perdida_vigor"],
        "enfermedad": "Marchitez por Fusarium",
        "explicacion": "Se detecta marchitez, decoloración de tallos y raices y perdida de vigor"
    },
    {
        "sintomas": ["marchitez", "decoloracion"],
        "enfermedad": "Fusariosis",
        "explicacion": "Se detecta marchitez, decoloración de tallos y raices"
    },
    {
        "sintomas": ["pustulas_naranjas", "defoliacion"],
        "enfermedad": "Roya del Cafe",
        "explicacion": "Se detectan pustulas naranjas y defoliacion"
    },
    {
        "sintomas": ["patrones_mosaico_hojas", "deformacion_hojas", "deformacion_frutos"],
        "enfermedad": "Virosis",
        "explicacion": "Se detectan patrones de mosaico en hojas y deformación de hojas y frutos"
    },
    {
        "sintomas": ["polvo_blanco_hojas", "deformidad_tallos"],
        "enfermedad": "Oidio",
        "explicacion": "Se detecta polvo blanco o gris en hojas y deformidad de tallos"
    }
]

# Leer el archivo Excel
df = pd.read_excel("entradas_plantas.xlsx")

# Función del motor de inferencias
def motor_inferencias(reglas, entrada):
    enfermedades = []
    explicaciones = []
    for regla in reglas:
        cumple = True
        for sintoma in regla["sintomas"]:
            if not entrada.get(sintoma):
                cumple = False
                break
        if cumple:
            enfermedades.append(regla["enfermedad"])
            explicaciones.append(regla["explicacion"])
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
    entrada = row.to_dict()
    enfermedades, explicaciones = motor_inferencias(reglas, entrada)
    if enfermedades:
        for enfermedad, explicacion in zip(enfermedades, explicaciones):
            tabla.insert("", "end", values=(index + 1, enfermedad, explicacion))
    else:
        tabla.insert("", "end", values=(index + 1, "Ninguna", "No hay diagnóstico"))

# Función para cerrar la aplicación
def cerrar_app():
    root.destroy()

# Botón para cerrar la aplicación
boton_cerrar = tk.Button(root, text="Cerrar", command=cerrar_app)
boton_cerrar.grid(row=1, column=0, padx=10, pady=10)

# Ejecutar el bucle de eventos principal
root.mainloop()