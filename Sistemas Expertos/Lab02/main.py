import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
import openpyxl

def cargar_datos():
    ruta_archivo = filedialog.askopenfilename(filetypes=[("Archivos Excel", "*.xlsx")])
    if ruta_archivo:
        wb = openpyxl.load_workbook(ruta_archivo)
        hoja = wb.active
        datos = []
        for fila in hoja.iter_rows(min_row=2, values_only=True):
            sintomas = [str(valor) for valor in fila[0:] if valor in ("YES", "NO")]
            datos.append(sintomas)
        return datos
    else:
        return None


def evaluar_reglas(sintomas, reglas_diagnostico):
    diagnósticos = []
    explicaciones = []
    
    for síntomas_planta in sintomas:
        diagnóstico_planta = []
        explicación_planta = []
        for síntoma in síntomas_planta:
            if síntoma in reglas_diagnostico:
                diagnóstico, explicación = reglas_diagnostico[síntoma]
                diagnóstico_planta.append(diagnóstico)
                explicación_planta.append(explicación)
        diagnósticos.append(diagnóstico_planta)
        explicaciones.append(explicación_planta)
    
    return diagnósticos, explicaciones


def evaluar_sintomas():
    sintomas = cargar_datos()
    if sintomas:
        diagnósticos, explicaciones = evaluar_reglas(sintomas, reglas_diagnostico)
        mostrar_resultados(sintomas, diagnósticos, explicaciones)

def mostrar_resultados(plantas, diagnósticos, explicaciones):
    for i, (sintomas, diagnóstico, explicación) in enumerate(zip(plantas, diagnósticos, explicaciones)):
        planta = ', '.join(sintomas)
        label_planta = tk.Label(root, text=f"Planta {i+1}: {planta}")
        label_planta.grid(row=i+1, column=0, sticky="w", padx=10, pady=5)

        label_diagnóstico = tk.Label(root, text=f"Diagnóstico: {diagnóstico}")
        label_diagnóstico.grid(row=i+1, column=1, sticky="w", padx=10, pady=5)

        label_explicación = tk.Label(root, text=f"Explicación: {explicación}")
        label_explicación.grid(row=i+1, column=2, sticky="w", padx=10, pady=5)

# Definición de la ventana principal de Tkinter
root = tk.Tk()
root.title("Diagnóstico de Enfermedades en Plantas")

# Botón para cargar datos desde un archivo Excel
boton_cargar = ttk.Button(root, text="Cargar Datos", command=evaluar_sintomas)
boton_cargar.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

# Reglas de diagnóstico
reglas_diagnostico = {
    "MANCHAS OSCURAS": ("Posible atracnosis.", "Las manchas oscuras pueden ser un signo de atracnosis."),
    "MANCHAS NEGRAS": ("Posible Mancha de asfalto.", "Las manchas negras podrían indicar mancha de asfalto."),
    "NECROSIS": ("Posible Pudricion del cogollo.", "La necrosis podria indicar muerte del cogollo."),
    "PUSTULAS NARANJAS": ("Posible roya del cafe", "Las pústulas naranjas podrían ser causadas por roya del cafe."),
    "MARCHITEZ": ("Posible marchitez por fusarium.", "La marchitez puede ser causada por marchitez por fusarium."),
    "DECOLORACION TALLO": ("Posible fusariosis.", "La decoloración del tallo puede ser fusariosis."),
    "MANCHAS AMARILLAS": ("Posible Mancha angular.", "Las manchas amarillas podrían indicar mancha angular."),
    "PUDRICION": ("Posible podredumbre.", "La pudrición puede ser causada por podredumbre negra."),
    "POLVO BLANCO": ("Posible oídio.", "El polvo blanco es un síntoma común de una infección por oídio."),
    "MANCHA MOSAICO": ("Posible infección viral o virosis.", "La mancha mosaico es un síntoma común de una infección viral."),
    "CAIDA HOJAS": ("Posible infeccion de mancha negra.", "La caída de las hojas puede ser causada por infeccion de mancha negra."),
    "DEFORMACION": ("Posible daño por virosis.", "La deformación puede ser causada por infecciones virales."),
}

# Iniciar el bucle principal de Tkinter
root.mainloop()

