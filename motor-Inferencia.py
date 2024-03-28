import tkinter as tk
from tkinter import (Label, Button, Frame, messagebox,
                     filedialog, ttk, Scrollbar, VERTICAL, HORIZONTAL, font)
import json

# Importar las reglas de diagnóstico divididas por síntomas puntuales
with open("reglas.json", "r", encoding="utf-8") as archivo:
    rules = json.load(archivo)

#Metodo para evaluar los sintomas de json con las reglas
def evaluar_reglas(sintomas, reglas):
    diagnosticos = []
    explicaciones = []
    for regla in reglas:
        if all(sintomas.get(s, False) for s in regla["sintomas_presentes"]) and \
           not any(sintomas.get(s, False) for s in regla["sintomas_ausentes"]):
            diagnosticos.append(regla["diagnostico"])
            explicaciones.append(regla["explicacion"])
    return diagnosticos, explicaciones
def open_archive():
    archive = filedialog.askopenfilename(initialdir='/',
                                         title='Select archive',
                                         filetype=(('JSON files', '*.json'), ('All files', '*.*')))
    if archive:
        with open(archive, 'r') as f:
            # Cargar el contenido del archive JSON
            datos_json = json.load(f)
    # Actualizar el texto en el widget 'indica' con la ruta del archive seleccionado
    path['text'] = archive if archive else "No se seleccionó ningún archive"

def data_json():
    archive_json = path['text']  # Obtenemos la ubicación del archivo desde el Label
    try:
        # Abrir y cargar el archivo JSON
        with open(archive_json, 'r') as f:
            data = json.load(f)

        # Limpiar los resultados anteriores
        CleanResults()

        # Iterar sobre cada entrada en los datos
        for entry in data:
            symptoms = entry  # Los síntomas se toman directamente de la entrada
            # Evaluar las reglas para obtener diagnósticos y explicaciones
            diagnosis, explications = evaluar_reglas(symptoms, rules)
            # Agregar los resultados al Treeview de resultados
            if diagnosis:
                for diagnose, explication in zip(diagnosis, explications):
                    results.insert('', 'end', values=[diagnose, explication])
            else:
                results.insert('', 'end', values=["No se encontraron enfermedades", ""])

        # Mostrar los datos en la table
        table['column'] = list(data[0].keys())
        table['show'] = "headings"  # encabezado

        for column in table['column']:
            table.heading(column, text=column)

        for fila in data:
            table.insert('', 'end', values=list(fila.values()))
    except ValueError:
        messagebox.showerror('Informacion', 'Formato incorrecto')
    except FileNotFoundError:
        messagebox.showerror('Informacion', 'El archivo no se encontró')

#Metodo para eliminar los datos de la tabla
def CleanResults():
    results.delete(*results.get_children())
    table.delete(*table.get_children())

# GUI
root = tk.Tk()
root.configure(background='black')
root.geometry('1000x600')
root.minsize(width=600, height=400)
root.title('Motor de Inferencia')

root.columnconfigure(0, weight=25)
root.rowconfigure(0, weight=25)
root.columnconfigure(0, weight=1)
root.rowconfigure(1, weight=1)

frame1 = Frame(root, bg='gray')
frame1.grid(column=0, row=0, sticky='nsew')
frame1.columnconfigure(0, weight=1)
frame1.rowconfigure(0, weight=1)

frame2 = Frame(root, bg='dark gray')
frame2.grid(column=0, row=1, sticky='nsew')
frame2.columnconfigure(0, weight=1)
frame2.rowconfigure(0, weight=1)

# Tablas del GUI
results = ttk.Treeview(frame2, height=10)
results.grid(column=0, row=1, columnspan=4, sticky='nsew')

results['column'] = ['Diagnóstico', 'Explicación']
results['show'] = 'headings'

results.heading('Diagnóstico', text='Diagnóstico')
results.heading('Explicación', text='Explicación')

frame2.rowconfigure(1, weight=1)

table = ttk.Treeview(frame1, height=10)
table.grid(column=0, row=0, sticky='nsew')

ladox = Scrollbar(frame1, orient=HORIZONTAL, command=table.xview)
ladox.grid(column=0, row=1, sticky='ew')

ladoy = Scrollbar(frame1, orient=VERTICAL, command=table.yview)
ladoy.grid(column=1, row=0, sticky='ns')

table.configure(xscrollcommand=ladox.set, yscrollcommand=ladoy.set)

# Estilos del GUI
style = ttk.Style(frame1)
style.configure("Treeview", font=('Helvetica', 11), background="#272727",
                foreground="white", fieldbackground="black")
style.configure("Treeview.Heading", font=('Tahoma', 11, 'bold'), foreground="#4F4F4F")  # Encabezados de columna

# Botones del GUI
button1 = Button(frame2, text="Open", bg="#44C6DF", fg="black", command=open_archive, font=("Arial", 11, "bold"),
                 width=-10, height=1)
button1.grid(column=0, row=0, sticky='nsew', padx=10, pady=10)

button2 = Button(frame2, text='Show', bg='#EC8123', fg="black", command=data_json, font=("Arial", 11, "bold"))
button2.grid(column=1, row=0, sticky='nsew', padx=10, pady=10)

button3 = Button(frame2, text='Clean', bg='#FF3062', fg="black", command=CleanResults, font=("Arial", 11, "bold"))
button3.grid(column=2, row=0, sticky='nsew', padx=10, pady=10)

path = Label(frame2, fg='black', bg='dark gray', text='Ubicación del archivo', font=('Arial', 10, 'bold'))
path.grid(column=3, row=0,  sticky='nsew', padx=10, pady=10)

root.mainloop()