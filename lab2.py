# Import necessary libraries
import pandas as pd
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk

# Define diagnostic rules for plant diseases
rules = {
    "Antracnosis": (["presente", "presente", "ausente", "ausente", "ausente", "ausente", "ausente", "ausente", "ausente", "ausente", "ausente", "ausente", "ausente", "ausente", "ausente", "ausente", "ausente", "ausente", "ausente", "ausente", "ausente", "ausente"], [], "La planta observda presenta Antracnosis porque presenta Manchas oscuras en hojas y frutos, Pudrición"),
    "Sigatoka Negra (en banano)": (['ausente', 'ausente', 'presente', 'presente', 'ausente', 'ausente', 'ausente', 'ausente', 'ausente', 'ausente', 'ausente', 'ausente', 'ausente', 'ausente', 'ausente', 'ausente', 'ausente', 'ausente', 'ausente', 'ausente', 'ausente', 'ausente'], [], "La planta observda presenta Sigatoka Negra porque presenta Manchas negras alargadas en hojas, Reducción del área foliar"),
    "Pudrición del Cogollo (en palma aceitera)": (['ausente', 'ausente', 'ausente', 'ausente', 'presente', 'presente', 'presente', 'ausente', 'ausente', 'ausente', 'ausente', 'ausente', 'ausente', 'ausente', 'ausente', 'ausente', 'ausente', 'ausente', 'ausente', 'ausente', 'ausente', 'ausente'], [], "La planta observda presenta Pudrición del Cogollo porque presenta Marchitez, Necrosis del cogollo, Hojas jovenes no se abren"),
    "Roya del café": (['ausente', 'ausente', 'ausente', 'ausente', 'ausente', 'ausente', 'ausente', 'presente', 'ausente', 'ausente', 'ausente', 'ausente', 'ausente', 'ausente', 'ausente', 'ausente', 'ausente', 'ausente', 'ausente', 'ausente', 'ausente', 'ausente'], [], "La planta observda presenta Roya del café porque presenta Pústulas de color naranja en la parte inferior de las hojas"),
    "Mancha del asfalto (en cítricos)": (['ausente', 'ausente', 'ausente', 'ausente', 'ausente', 'ausente', 'ausente', 'ausente', 'presente', 'presente', 'ausente', 'ausente', 'ausente', 'ausente', 'ausente', 'ausente', 'ausente', 'ausente', 'ausente', 'ausente', 'ausente', 'ausente'], [], "La planta observda presenta Mancha del asfalto porque presenta Manchas negras circulares en frutos y hojas, Caída prematura de frutos"),
    "Marchitez por Fusarium (en tomates)": (['ausente', 'ausente', 'ausente', 'ausente', 'presente', 'ausente', 'ausente', 'ausente', 'ausente', 'ausente', 'presente', 'presente', 'ausente', 'ausente', 'ausente', 'ausente', 'ausente', 'ausente', 'ausente', 'ausente', 'ausente', 'ausente'], [], "La planta observda presenta Marchitez por Fusarium porque presenta Marchitez, Decoloración de tallos y raíces, Pérdida de vigor"),
    "Podredumbre negra (en piña)": (['ausente', 'ausente', 'ausente', 'ausente', 'ausente', 'ausente', 'ausente', 'ausente', 'ausente', 'ausente', 'ausente', 'ausente', 'presente', 'presente', 'ausente', 'ausente', 'ausente', 'ausente', 'ausente', 'ausente', 'ausente', 'ausente'], [], "La planta observda presenta Podredumbre negra porque presenta Manchas oscuras en la base del fruto, Pudrición acuosa"),
    "Mancha angular (en frijoles)": (['ausente', 'ausente', 'ausente', 'ausente', 'ausente', 'ausente', 'ausente', 'ausente', 'ausente', 'ausente', 'ausente', 'ausente', 'ausente', 'ausente', 'presente', 'presente', 'ausente', 'ausente', 'ausente', 'ausente', 'ausente', 'ausente'], [], "La planta observda presenta Mancha angular porque presenta Manchas amarillas o marrones en hojas, Formación de lesiones"),
    "Oídio": (['ausente', 'ausente', 'ausente', 'ausente', 'ausente', 'ausente', 'ausente', 'ausente', 'ausente', 'ausente', 'ausente', 'ausente', 'ausente', 'ausente', 'ausente', 'ausente', 'presente', 'presente', 'ausente', 'ausente', 'ausente', 'ausente'], [], "La planta observda presenta Oídio porque presenta Polvo blanco o gris en hojas, Tallos deformes"),
    "Mancha negra": (['ausente', 'ausente', 'ausente', 'ausente', 'ausente', 'ausente', 'ausente', 'ausente', 'ausente', 'ausente', 'ausente', 'ausente', 'ausente', 'ausente', 'ausente', 'ausente', 'ausente', 'ausente', 'presente', 'presente', 'ausente', 'ausente'], [], "La planta observda presenta Mancha negra porque presenta Manchas negras en las hojas, Caída prematura de las hojas"),
    "Virosis (Virus del mosaico)": (['ausente', 'ausente', 'ausente', 'ausente', 'ausente', 'ausente', 'ausente', 'ausente', 'ausente', 'ausente', 'ausente', 'ausente', 'ausente', 'ausente', 'ausente', 'ausente', 'ausente', 'ausente', 'ausente', 'ausente', 'presente', 'presente'], [], "La planta observda presenta Virosis porque presenta Patrones de mosaico en las hojas, Deformación de hojas y frutos"),
    "Fusariosis (Fusarium)": (['ausente', 'ausente', 'ausente', 'ausente', 'presente', 'ausente', 'ausente', 'ausente', 'ausente', 'ausente', 'presente', 'ausente', 'ausente', 'ausente', 'ausente', 'ausente', 'ausente', 'ausente', 'ausente', 'ausente', 'ausente', 'ausente'], [], "La planta observda presenta Fusariosis porque presenta Marchitez, Decoloración de tallos y raíces")
}

# Function to diagnose diseases based on symptoms
def diagnosticar_enfermedad(sintomas):
    enfermedades_diagnosticadas = []
    for enfermedad, (sintomas_presentes, sintomas_ausentes, diagnostico) in rules.items():
        print(f"Regla de diagnóstico para {enfermedad}:")
        print("Síntomas presentes esperados:", sintomas_presentes)
        print("Síntomas presentes recibidos:", sintomas)
        if sintomas_presentes == sintomas:
            enfermedades_diagnosticadas.append(diagnostico)
    return enfermedades_diagnosticadas

# Function to load data from Excel file and perform diagnosis
def cargar_datos():
    filepath = filedialog.askopenfilename(filetypes=[("Archivos Excel", "*.xlsx")])
    print("Ruta del archivo seleccionado:", filepath)
    
    try:
        df = pd.read_excel(filepath, header=0)
        diagnosticos = []
        for index, row in df.iterrows():
            sintomas_planta = [str(value).lower() for value in row.tolist()[1:]]  # Se omite la columna 'Planta'
            print("\nSíntomas de la planta:", sintomas_planta)
            resultado_diagnostico = diagnosticar_enfermedad(sintomas_planta)
            print("Diagnóstico obtenido:", resultado_diagnostico)
            diagnosticos.append(resultado_diagnostico)
        
        print("\nDiagnósticos obtenidos:")
        print(diagnosticos)
        
        mostrar_diagnosticos(diagnosticos)
    
    except Exception as e:
        print("Error al leer el archivo:", e)

# Function to display diagnoses in a GUI window
def mostrar_diagnosticos(diagnosticos):
    root = tk.Tk()
    root.title("Diagnósticos de Enfermedades en Plantas")
    
    frame = ttk.Frame(root)
    frame.pack(padx=10, pady=10, expand=True, fill=tk.BOTH)
    
    tree = ttk.Treeview(frame, columns=("Planta", "Diagnóstico"), show="headings")
    tree.heading("Planta", text="Planta")
    tree.heading("Diagnóstico", text="Diagnóstico")
    
    for idx, planta_diagnostico in enumerate(diagnosticos, start=1):
        planta = f"Planta {idx}"
        diagnóstico = ", ".join(planta_diagnostico) if planta_diagnostico else "No se encontraron diagnósticos"
        tree.insert("", "end", values=(planta, diagnóstico))
    
    tree.column("Planta", width=100)
    tree.column("Diagnóstico", width=800)
    tree.pack(side="left", expand=True, fill=tk.BOTH)
    
    scrollbar = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
    scrollbar.pack(side="right", fill="y")
    tree.configure(yscrollcommand=scrollbar.set)
    
    root.mainloop()

# Call the function to load data and perform diagnosis
cargar_datos()
