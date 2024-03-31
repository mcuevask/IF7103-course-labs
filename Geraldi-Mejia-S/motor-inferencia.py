import pandas as pd
import tkinter as tk
from tkinter import ttk

# Datos de entrada
def cargar_datos_prueba():
    data_excel = pd.read_excel("./Geraldi-Mejia-S/pruebas.xlsx")

    sintomas_entrada=[]
    for row in data_excel.iterrows():
        sintoma = {
            "manchas_oscuras_hojas_frutos": row[1]["manchas_oscuras_hojas_frutos"],
            "pudricion": row[1]["pudricion"],
            "manchas_negra_alargadas_en_hojas": row[1]["manchas_negra_alargadas_en_hojas"],
            "reduccion_area_foliar": row[1]["reduccion_area_foliar"],
            "marchitez": row[1]["marchitez"],
            "necrosis_del_cogollo": row[1]["necrosis_del_cogollo"],
            "hojas_jovenes_cerradas": row[1]["hojas_jovenes_cerradas"],
            "pustulas_naranjas_parte_inferior_hojas": row[1]["pustulas_naranjas_parte_inferior_hojas"],
            "manchas_negras_circulares_frutas_hojas": row[1]["manchas_negras_circulares_frutas_hojas"],
            "caida_prematura_hojas": row[1]["caida_prematura_hojas"],
            "decoloracion_tallos_raices": row[1]["decoloracion_tallos_raices"],
            "perdida_vigor": row[1]["perdida_vigor"],
            "manchas_oscuras_base_fruto": row[1]["manchas_oscuras_base_fruto"],
            "pudricion_acuosa": row[1]["pudricion_acuosa"],
            "manchas_amarillasmarrones_hojas": row[1]["manchas_amarillasmarrones_hojas"],
            "lesiones": row[1]["lesiones"],
            "polvo_blanco_hojas": row[1]["polvo_blanco_hojas"],
            "tallos_deformes": row[1]["tallos_deformes"],
            "manchas_negras_hojas": row[1]["manchas_negras_hojas"],
            "patrones_mosaico_hojas": row[1]["patrones_mosaico_hojas"],
            "deformacion_hojas_frutos": row[1]["deformacion_hojas_frutos"]
    }
        sintomas_entrada.append(sintoma)
    
    return sintomas_entrada

# Reglas para considerar la presencia o ausencia de síntomas
def cargar_reglas():
    reglas = [
        {
            "nombre": "Antracnosis",
            "sintomas_presentes": ["manchas_oscuras_hojas_frutos","pudricion" ],
            "sintomas_ausentes": [""],
            "diagnostico": "La planta sufre de Antracnosis.",
            "explicacion": "Detectadas manchas oscuras en hojas y frutos, además de pudrición."
        },
        {
            "nombre": "Sigatoka Negra",
            "sintomas_presentes": ["manchas_negra_alargadas_en_hojas", "reduccion_area_foliar"],
            "sintomas_ausentes": ["manchas_negras_circulares_frutas_hojas"],
            "diagnostico": "La planta sufre de Sigatoka Negra.",
            "explicacion": "Presencia de manchas negras alargadas y reduccion del area foliar."
        },
        {
            "nombre": "Pudricion del cogollo",
            "sintomas_presentes": ["marchitez", "necrosis_del_cogollo","hojas_jovenes_cerradas"],
            "sintomas_ausentes": [],
            "diagnostico": "La planta sufre de Pudrición del cogollo.",
            "explicacion": "Detectada marchitez, necrosis en el cogollo y hojas jovenes cerradas."
        },
        {
            "nombre": "Roya del café",
            "sintomas_presentes": ["pustulas_naranjas_parte_inferior_hojas"],
            "sintomas_ausentes": [],
            "diagnostico": "La planta sufre de Roya del café.",
            "explicacion": "Detectadas pústulas naranjas en la parte inferior de las hojas."
        },
        {
            "nombre": "Mancha de asfalto",
            "sintomas_presentes": ["manchas_negras_circulares_frutas_hojas","caida_prematura_hojas"],
            "sintomas_ausentes": ["manchas_negra_alargadas_en_hojas"],
            "diagnostico": "La planta sufre de Mancha de asfalto.",
            "explicacion": "Se prensentan manchas negras circulares en frutas y hojas, además de caida de hojas prematura."
        },
        {
            "nombre": "Manchitez por fusarium",
            "sintomas_presentes": ["marchitez","decoloracion_tallos_raices","perdida_vigor"],
            "sintomas_ausentes": [],
            "diagnostico": "La planta sufre de Marchitez por fusarium.",
            "explicacion": "Se prensenta marchitez, decoloracion de tallos y raices y una perdida de vigor."
        },
        {
            "nombre": "Podredumbre Negra",
            "sintomas_presentes": ["manchas_oscuras_base_fruto","pudricion_acuosa"],
            "sintomas_ausentes": ["manchas_oscuras_hojas_frutos"],
            "diagnostico": "La planta sufre de Podredumbre Negra.",
            "explicacion": "Se prensentan manchas oscuras en la base del fruto y pudricion acuosa."
        },
        {
            "nombre": "Mancha Angular",
            "sintomas_presentes": ["manchas_amarillasmarrones_hojas","lesiones"],
            "sintomas_ausentes": [],
            "diagnostico": "La planta sufre de Mancha Angular.",
            "explicacion": "Se prensentan manchas amarrillas o marrones en hojas y lesiones."
        },
        {
            "nombre": "Oidio",
            "sintomas_presentes": ["polvo_blanco_hojas","tallos_deformes"],
            "sintomas_ausentes": [],
            "diagnostico": "La planta sufre de Oídio .",
            "explicacion": "La planta presenta polvo blanco y tallos deformes."
        },
        {
            "nombre": "Mancha negra",
            "sintomas_presentes": ["manchas_negras_hojas","caida_prematura_hojas"],
            "sintomas_ausentes": ["manchas_negras_circulares_frutas_hojas","manchas_negra_alargadas_en_hojas"],
            "diagnostico": "La planta sufre Mancha negra .",
            "explicacion": "La planta presenta manchas negras de cualquier forma y caida prematura de hojas."
        },
        {
            "nombre": "Virosis",
            "sintomas_presentes": ["patrones_mosaico_hojas","deformacion_hojas_frutos"],
            "sintomas_ausentes": [],
            "diagnostico": "La planta sufre Virosis.",
            "explicacion": "La planta presenta patrones de mosaico en sus hojas y deformación de hojas y frutos."
        },
        {
            "nombre": "Fusariosis",
            "sintomas_presentes": ["marchitez","decoloracion_tallos_raices"],
            "sintomas_ausentes": ["perdida_vigor"],
            "diagnostico": "La planta sufre de Fusarium.",
            "explicacion": "La planta presenta marchitez y decoloración de sus tallos y raices."
        }
    ]
    return reglas

def evaluar_reglas(sintomas, reglas):
    diagnosticos = []
    explicaciones = []
    for regla in reglas:
        if all(sintomas.get(s, False) for s in regla["sintomas_presentes"]) and \
           not any(sintomas.get(s, False) for s in regla["sintomas_ausentes"]):
            diagnosticos.append(regla["diagnostico"])
            explicaciones.append(regla["explicacion"])
    if not diagnosticos:
        diagnosticos.append("No se detectó ninguna enfermedad en la planta")
        explicaciones.append("N/A")

    return diagnosticos, explicaciones

# Evaluación de síntomas y obtención de diagnósticos y explicaciones
def diagnosticar_plantas(sintomas_entrada, reglas):
    todos_diagnosticos = []
    todas_explicaciones = []
    for sintomas in sintomas_entrada:
        diagnosticos, explicaciones = evaluar_reglas(sintomas, reglas)
        todos_diagnosticos.extend(diagnosticos)
        todas_explicaciones.extend(explicaciones)
    return todos_diagnosticos,todas_explicaciones

class TablaApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Tabla con Tkinter")

        self.datos = []

        self.tabla = ttk.Treeview(root, columns=("Planta #", "Diagnóstico", "Explicación"), show="headings")
        self.tabla.heading("Planta #", text="Planta #")
        self.tabla.heading("Diagnóstico", text="Diagnóstico")
        self.tabla.heading("Explicación", text="Explicación")
        self.tabla.pack(padx=10, pady=10)
        
        self.tabla.column("Planta #", width=65)
        self.tabla.column("Diagnóstico", width=280)
        self.tabla.column("Explicación", width=600)

        self.refresh_button = tk.Button(root, text="Refresh", command=self.refresh_tabla)
        self.refresh_button.pack(padx=10, pady=(0, 10))

        self.llenar_tabla()

    def llenar_tabla(self):
        datos_prueba = cargar_datos_prueba()
        reglas = cargar_reglas()
        diagnosticos, explicaciones = diagnosticar_plantas(datos_prueba,reglas)
        self.datos.clear()
        id = 1
        for diag,exp in zip(diagnosticos,explicaciones):
            self.datos.append({"ID": id, "Diagnóstico": diag, "Explicación": exp})
            id+=1
          
        for dato in self.datos:
            self.tabla.insert("", "end", values=(dato["ID"], dato["Diagnóstico"], dato["Explicación"]))

    def limpiar_tabla(self):
        for row in self.tabla.get_children():
            self.tabla.delete(row)

    def refresh_tabla(self):
        self.limpiar_tabla()
        self.llenar_tabla()

root = tk.Tk()
app = TablaApp(root)
root.mainloop()
