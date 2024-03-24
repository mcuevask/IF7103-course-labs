#Sistemas Expertos
#Laboratorio 2
#Milena Rojas Leiva B76703

#Este código fue escrito con ayuda de ChatGPT

import tkinter as tk
from tkinter import filedialog
import pandas as pd

#Definimos las reglas para dar un diagnostico
reglas_diagnostico = {
    "Antracnosis":{
        "sintomas_presentes": ["manchas_oscuras_hojas_frutos", "pudricion"],
        "sintomas_ausentes": ["manchas_negras_alargadas", "reduccion_foliar",
                             "marchitez", "necrosis_cogollo", "hojas_jovenes_sin_abrir","pustulas_naranjas",
                             "manchas_negras_circulares_frutos_hojas", "caida_prematura_hojas", "decoloracion_tallos_raices",
                             "perdida_vigor","manchas_oscuras_base_fruto", "pudricion_acuosa","manchas_amarillas_marrones_hojas",
                             "formacion_lesiones","polvo_blanco_hojas", "tallo_deforme", "patron_mosaico_hoja", "deformacion_hoja_fruto","mancha_negra_hojas"],
        "diagnostico": "Antracnosis",
        "explicacion": "Presencia de manchas oscuras en hojas y frutos, en algunos casos se presenta pudrición."
    },
    "Sigatoka Negra":{
        "sintomas_presentes": ["manchas_negras_alargadas", "reduccion_foliar"],
        "sintomas_ausentes": ["manchas_oscuras_hojas_frutos", "pudricion","marchitez", "necrosis_cogollo", "hojas_jovenes_sin_abrir","pustulas_naranjas",
                             "manchas_negras_circulares_frutos_hojas", "caida_prematura_hojas", "decoloracion_tallos_raices",
                             "perdida_vigor","manchas_oscuras_base_fruto", "pudricion_acuosa","manchas_amarillas_marrones_hojas",
                             "formacion_lesiones","polvo_blanco_hojas", "tallo_deforme", "patron_mosaico_hoja", "deformacion_hoja_fruto","mancha_negra_hojas",],
        "diagnostico": "Sigatoka Negra",
        "explicacion": "Presencia de manchas negras alargadas en hojas y reducción del área foliar."
    },
    "Pudricción del Cogollo": {
        "sintomas_presentes": ["marchitez", "necrosis_cogollo", "hojas_jovenes_sin_abrir"],
        "sintomas_ausentes": ["manchas_oscuras_hojas_frutos", "pudricion","manchas_negras_alargadas", "reduccion_foliar","pustulas_naranjas",
                             "manchas_negras_circulares_frutos_hojas", "caida_prematura_hojas", "decoloracion_tallos_raices",
                             "perdida_vigor","manchas_oscuras_base_fruto", "pudricion_acuosa","manchas_amarillas_marrones_hojas",
                             "formacion_lesiones","polvo_blanco_hojas", "tallo_deforme", "patron_mosaico_hoja", "deformacion_hoja_fruto","mancha_negra_hojas",],
        "diagnostico": "Pudrición del Cogollo",
        "explicacion": "Presenta marchitez, necrosis del cogollo y hojas verdes que no se abren."
    },
    "Royal del Café": {
        "sintomas_presentes": ["pustulas_naranjas"],
        "sintomas_ausentes": ["manchas_oscuras_hojas_frutos", "pudricion","manchas_negras_alargadas", "reduccion_foliar",
                             "marchitez", "necrosis_cogollo", "hojas_jovenes_sin_abrir",
                             "manchas_negras_circulares_frutos_hojas", "caida_prematura_hojas", "decoloracion_tallos_raices",
                             "perdida_vigor","manchas_oscuras_base_fruto", "pudricion_acuosa","manchas_amarillas_marrones_hojas",
                             "formacion_lesiones","polvo_blanco_hojas", "tallo_deforme", "patron_mosaico_hoja", "deformacion_hoja_fruto","mancha_negra_hojas",],
        "diagnostico": "Royal del Café",
        "explicacion": "Presenta pústulas de color naranja en la parte inferior de las hojas."
    },
    "Mancha de Asfalto":{
        "sintomas_presentes":["manchas_negras_circulares_frutos_hojas", "caida_prematura_hojas"],
        "sintomas_ausentes":["manchas_oscuras_hojas_frutos", "pudricion","manchas_negras_alargadas", "reduccion_foliar",
                             "marchitez", "necrosis_cogollo", "hojas_jovenes_sin_abrir","pustulas_naranjas","decoloracion_tallos_raices",
                             "perdida_vigor","manchas_oscuras_base_fruto", "pudricion_acuosa","manchas_amarillas_marrones_hojas",
                             "formacion_lesiones","polvo_blanco_hojas", "tallo_deforme", "patron_mosaico_hoja", "deformacion_hoja_fruto","mancha_negra_hojas",],
        "diagnostico": "Mancha de Asfalto",
        "explicacion": "Presenta manchas negra circulares en frutos y hojas, además presenta caída prematura de hojas."
    },
    "Marchitez por Fusarium":{
        "sintomas_presentes": ["marchitez", "decoloracion_tallos_raices", "perdida_vigor"],
        "sintomas_ausentes": ["manchas_oscuras_hojas_frutos", "pudricion","manchas_negras_alargadas", "reduccion_foliar",
                              "necrosis_cogollo", "hojas_jovenes_sin_abrir","pustulas_naranjas","manchas_negras_circulares_frutos_hojas",
                              "caida_prematura_hojas","manchas_oscuras_base_fruto", "pudricion_acuosa","manchas_amarillas_marrones_hojas",
                              "formacion_lesiones","polvo_blanco_hojas", "tallo_deforme", "patron_mosaico_hoja", "deformacion_hoja_fruto", "mancha_negra_hojas",],
        "diagnostico": "Marchitez por Fusarium",
        "explicacion": "Presenta marchitez, decoloracion de tallos y raíces, además presenta pérdida de vigor."
    },
    "Podredumbre Negra":{
        "sintomas_presentes": ["manchas_oscuras_base_fruto", "pudricion_acuosa"],
        "sintomas_ausentes": ["manchas_oscuras_hojas_frutos", "pudricion","manchas_negras_alargadas", "reduccion_foliar",
                              "marchitez", "necrosis_cogollo", "hojas_jovenes_sin_abrir","pustulas_naranjas",
                              "manchas_negras_circulares_frutos_hojas", "caida_prematura_hojas", "decoloracion_tallos_raices",
                              "perdida_vigor","manchas_amarillas_marrones_hojas","formacion_lesiones","polvo_blanco_hojas", "tallo_deforme", "patron_mosaico_hoja", "deformacion_hoja_fruto","mancha_negra_hojas",],
        "diagnostico": "Podredumbre Negra",
        "explicacion": "Presenta manchas oscuras en la base del fruto y pudrición acuosa."
    },
    "Mancha Angular":{
        "sintomas_presentes": ["manchas_amarillas_marrones_hojas", "formacion_lesiones"],
        "sintomas_ausentes": ["manchas_oscuras_hojas_frutos", "pudricion","manchas_negras_alargadas", "reducción_foliar",
                              "marchitez", "necrosis_cogollo", "hojas_jovenes_sin_abrir","pustulas_naranjas",
                              "manchas_negras_circulares_frutos_hojas", "caida_prematura_hojas", "decoloracion_tallos_raices",
                              "perdida_vigor","manchas_oscuras_base_fruto", "pudricion_acuosa","polvo_blanco_hojas", "tallo_deforme", "patron_mosaico_hoja", "deformacion_hoja_fruto","mancha_negra_hojas",],
        "diagnostico": "Mancha Angular",
        "explicacion": "Presenta manchas amarillas o marrones en hojas y formación de lesiones."
    },
    "Oídio":{
        "sintomas_presentes": ["polvo_blanco_hojas", "tallo_deforme"],
        "sintomas_ausentes": ["manchas_oscuras_hojas_frutos", "pudricion","manchas_negras_alargadas", "reduccion_foliar",
                              "marchitez", "necrosis_cogollo", "hojas_jovenes_sin_abrir","pustulas_naranjas",
                              "manchas_negras_circulares_frutos_hojas", "caida_prematura_hojas", "decoloracion_tallos_raices",
                              "perdida_vigor","manchas_oscuras_base_fruto", "pudricion_acuosa","manchas_amarillas_marrones_hojas",
                              "formacion_lesiones","patron_mosaico_hoja", "deformacion_hoja_fruto""mancha_negra_hojas"],
        "diagnostico": "Oídio",
        "explicacion": "Presenta polvo blanco en las hojas y tallos deformes."
    },
    "Mancha Negra":{
        "sintomas_presentes": ["mancha_negra_hojas", "caida_prematura_hojas"],
        "sintomas_ausentes": ["manchas_oscuras_hojas_frutos", "pudricion","manchas_negras_alargadas", "reduccion_foliar",
                             "marchitez", "necrosis_cogollo", "hojas_jovenes_sin_abrir","pustulas_naranjas",
                             "manchas_negras_circulares_frutos_hojas", "decoloracion_tallos_raices",
                             "perdida_vigor","manchas_oscuras_base_fruto", "pudricion_acuosa","manchas_amarillas_marrones_hojas",
                             "formacion_lesiones","polvo_blanco_hojas", "tallo_deforme"],
        "diagnostico": "Mancha Negra",
        "explicacion": "Presenta manchas negras en las hojas y caida prematura de las hojas"
    },
    "Virosis":{
        "sintomas_presentes": ["patron_mosaico_hoja", "deformacion_hoja_fruto"],
        "sintomas_ausentes": ["manchas_oscuras_hojas_frutos", "pudricion","manchas_negras_alargadas", "reduccion_foliar",
                              "marchitez", "necrosis_cogollo", "hojas_jovenes_sin_abrir","pustulas_naranjas",
                              "manchas_negras_circulares_frutos_hojas", "caida_prematura_hojas", "decoloracion_tallos_raices",
                              "perdida_vigor","manchas_oscuras_base_fruto", "pudricion_acuosa","manchas_amarillas_marrones_hojas",
                              "formacion_lesiones","polvo_blanco_hojas", "tallo_deforme", "mancha_negra_hojas"],
        "diagnostico": "Virosis",
        "explicacion": "Presenta patrones de mosaico en las hojas y deformación de hojas y frutos."
    },
    "Fusariosis":{
        "sintomas_presentes": ["marchitez", "decoloracion_tallo_raices"],
        "sintomas_ausentes": ["manchas_oscuras_hojas_frutos", "pudricion","manchas_negras_alargadas", "reduccion_foliar",
                               "necrosis_cogollo", "hojas_jovenes_sin_abrir","pustulas_naranjas","manchas_negras_circulares_frutos_hojas",
                              "caida_prematura_hojas","perdida_vigor","manchas_oscuras_base_fruto", "pudricion_acuosa",
                              "manchas_amarillas_marrones_hojas","formacion_lesiones","polvo_blanco_hojas", "tallo_deforme", "patron_mosaico_hoja", "deformacion_hoja_fruto","mancha_negra_hojas",],
        "diagnostico": "Fusariosis",
        "explicacion": "Presenta marchitez, y decoloración de los tallos y las raíces."
    }
}

def evaluar_reglas(sintomas, reglas):
    diagnosticos= []
    for enfermedad, regla in reglas.items():
        if set(regla["sintomas_presentes"]).issubset(sintomas) and not set(regla["sintomas_ausentes"]).intersection(sintomas):
            diagnosticos.append((enfermedad, regla["diagnostico"], regla["explicacion"]))
    return diagnosticos

def cargar_datos_excel():
    filename = filedialog.askopenfilename(title="Seleccionar archivo Excel", filetypes=(("Archivos Excel", "*.xlsx"),("Todos los archivos", "*.*")))

    # Verificar si se seleccionó un archivo
    if filename:
        # Cargar datos desde el archivo Excel
        df = pd.read_excel(filename)

        # Obtener síntomas y valores de las plantas desde el DataFrame
        sintomas = df.columns.tolist()
        valores = df.values.tolist()

        # Evaluar las reglas de diagnóstico para cada planta
        resultados = {}
        for i, planta in enumerate(valores):
            sintomas_planta = [sintoma for j, sintoma in enumerate(sintomas) if planta[j] == "yes"]
            diagnosticos = evaluar_reglas(sintomas_planta, reglas_diagnostico)
            resultados[f"Planta {i+1}"] = diagnosticos

        # Mostrar los diagnósticos en la GUI
        mostrar_diagnosticos(resultados)

def mostrar_diagnosticos(resultados):
    for widget in root.winfo_children():
        widget.destroy()

    # Crear un frame para contener los diagnósticos
    frame = tk.Frame(root)
    frame.pack(fill="both", expand=True)


    # Crear un widget de texto para mostrar los diagnósticos
    text_widget = tk.Text(frame, wrap="word", font=("Arial", 12))
    text_widget.pack(side="left", fill="both", expand=True)

    # Agregar una barra de desplazamiento vertical
    scrollbar = tk.Scrollbar(frame, orient="vertical", command=text_widget.yview)
    scrollbar.pack(side="right", fill="y")

    # Configurar el widget de texto para que sea desplazable
    text_widget.config(yscrollcommand=scrollbar.set)

    text_widget.insert("end", "Diagnósticos\n\n",  "center bold")
    for planta, diagnosticos in resultados.items():
        text_widget.insert("end", f"Planta: {planta}\n", "bold")
        for diagnostico in diagnosticos:
            text_widget.insert("end", f"Enfermedad: {diagnostico[1]}\n")
            text_widget.insert("end", f"Explicación: {diagnostico[2]}\n")
        text_widget.insert("end", "\n")  # Espacio entre cada conjunto de diagnósticos

    # Establecer el estilo para el texto centrado y en negrita
    text_widget.tag_configure("center", justify="center")
    text_widget.tag_configure("bold", font=("Arial", 12, "bold"))


    # Ajustar la altura de la ventana para mostrar todos los resultados
    total_height = min(text_widget.winfo_height() + 20, 500)  # Altura máxima de la ventana
    total_height = max(total_height, 200)  # Altura mínima de la ventana

    # Establecer la geometría del frame y de la ventana
    frame.update_idletasks()  # Actualizar el frame para calcular correctamente su tamaño
    frame.config(width=600, height=total_height)  # Establecer el tamaño del frame

# Crear la ventana principal de la aplicación
root = tk.Tk()
root.title("Diagnóstico de Enfermedades en Plantas")

# Botón para cargar datos desde Excel
cargar_datos_button = tk.Button(root, text="Seleccione el archivo Excel", command=cargar_datos_excel, borderwidth=2, bg="#ADD8E6", font=("Arial", 14), padx=15, pady=7)
cargar_datos_button.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Establecer la geometría de la ventana en el centro de la pantalla
ancho_ventana = 800  # Ancho mínimo de la ventana
alto_ventana = 600  # Alto de la ventana

# Obtener dimensiones de la pantalla
ancho_pantalla = root.winfo_screenwidth()
alto_pantalla = root.winfo_screenheight()

# Calcular las coordenadas para centrar la ventana
x = (ancho_pantalla - ancho_ventana) // 2
y = (alto_pantalla - alto_ventana) // 2  # Posicionar la ventana en la parte superior de la pantalla

# Establecer la geometría de la ventana y centrarla
geometry_string = f"{ancho_ventana}x{alto_ventana}+{x}+{y}"
root.geometry(geometry_string)

# Ejecutar el bucle principal de la aplicación
root.mainloop()