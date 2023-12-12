import tkinter as tk
from tkinter import ttk

class SistemaExpertoLenguajes:
    def __init__(self):
        self.reglas = []

    def agregar_regla(self, condicion, accion):
        self.reglas.append({"condicion": condicion, "accion": accion})

    def obtener_sugerencia(self, preferencias):
        for regla in self.reglas:
            if all(preferencias[cond] == regla["condicion"][cond] for cond in regla["condicion"]):
                return regla["accion"]
        return "No se encontró ninguna sugerencia"

# Crear una instancia del sistema experto de lenguajes
sistema_experto_lenguajes = SistemaExpertoLenguajes()
base_de_datos = [
    {"Nombre": "Python", "Paradigma": "Multiparadigma", "Popularidad": "Alta", "Usabilidad": "Amigable para principiantes"},
    {"Nombre": "JavaScript", "Paradigma": "Multiparadigma", "Popularidad": "Alta", "Usabilidad": "Intermedio"},
    {"Nombre": "Java", "Paradigma": "Orientado a Objetos", "Popularidad": "Alta", "Usabilidad": "Intermedio"},
    {"Nombre": "C++", "Paradigma": "Orientado a Objetos", "Popularidad": "Moderada", "Usabilidad": "Avanzado"},
    {"Nombre": "Swift", "Paradigma": "Orientado a Objetos", "Popularidad": "Moderada", "Usabilidad": "Intermedio"},
    {"Nombre": "Ruby", "Paradigma": "Multiparadigma", "Popularidad": "Baja", "Usabilidad": "Amigable para principiantes"},
    {"Nombre": "PHP", "Paradigma": "Multiparadigma", "Popularidad": "Baja", "Usabilidad": "Intermedio"},
    {"Nombre": "C#", "Paradigma": "Orientado a Objetos", "Popularidad": "Alta", "Usabilidad": "Avanzado"},
    {"Nombre": "TypeScript", "Paradigma": "Multiparadigma", "Popularidad": "Moderada", "Usabilidad": "Intermedio"},
    {"Nombre": "Go", "Paradigma": "Imperativo", "Popularidad": "Moderada", "Usabilidad": "Avanzado"},
    
    {"Nombre": "Python2", "Paradigma": "Imperativo", "Popularidad": "Alta", "Usabilidad": "Amigable para principiantes"},
    {"Nombre": "JavaScript2", "Paradigma": "Imperativo", "Popularidad": "Alta", "Usabilidad": "Intermedio"},
    {"Nombre": "Java2", "Paradigma": "Imperativo", "Popularidad": "Alta", "Usabilidad": "Avanzado"},
    
    {"Nombre": "Python3", "Paradigma": "Imperativo", "Popularidad": "Moderada", "Usabilidad": "Amigable para principiantes"},
    {"Nombre": "JavaScript3", "Paradigma": "Imperativo", "Popularidad": "Moderada", "Usabilidad": "Intermedio"},
    {"Nombre": "Java3", "Paradigma": "Imperativo", "Popularidad": "Moderada", "Usabilidad": "Avanzado"},
    
    {"Nombre": "Python4", "Paradigma": "Imperativo", "Popularidad": "Baja", "Usabilidad": "Amigable para principiantes"},
    {"Nombre": "JavaScript4", "Paradigma": "Imperativo", "Popularidad": "Baja", "Usabilidad": "Intermedio"},
    {"Nombre": "Java4", "Paradigma": "Imperativo", "Popularidad": "Baja", "Usabilidad": "Avanzado"},
    
    {"Nombre": "Python5", "Paradigma": "Orientado a Objetos", "Popularidad": "Alta", "Usabilidad": "Amigable para principiantes"},
    {"Nombre": "JavaScript5", "Paradigma": "Orientado a Objetos", "Popularidad": "Alta", "Usabilidad": "Intermedio"},
    {"Nombre": "Java5", "Paradigma": "Orientado a Objetos", "Popularidad": "Alta", "Usabilidad": "Avanzado"},
    
    {"Nombre": "Python6", "Paradigma": "Orientado a Objetos", "Popularidad": "Moderada", "Usabilidad": "Amigable para principiantes"},
    {"Nombre": "JavaScript6", "Paradigma": "Orientado a Objetos", "Popularidad": "Moderada", "Usabilidad": "Intermedio"},
    {"Nombre": "Java6", "Paradigma": "Orientado a Objetos", "Popularidad": "Moderada", "Usabilidad": "Avanzado"},
    
    {"Nombre": "Python7", "Paradigma": "Orientado a Objetos", "Popularidad": "Baja", "Usabilidad": "Amigable para principiantes"},
    {"Nombre": "JavaScript7", "Paradigma": "Orientado a Objetos", "Popularidad": "Baja", "Usabilidad": "Intermedio"},
    {"Nombre": "Java7", "Paradigma": "Orientado a Objetos", "Popularidad": "Baja", "Usabilidad": "Avanzado"},
    
    {"Nombre": "Python8", "Paradigma": "Multiparadigma", "Popularidad": "Alta", "Usabilidad": "Amigable para principiantes"},
    {"Nombre": "JavaScript8", "Paradigma": "Multiparadigma", "Popularidad": "Alta", "Usabilidad": "Intermedio"},
    {"Nombre": "Java8", "Paradigma": "Multiparadigma", "Popularidad": "Alta", "Usabilidad": "Avanzado"},
    
    {"Nombre": "Python9", "Paradigma": "Multiparadigma", "Popularidad": "Moderada", "Usabilidad": "Amigable para principiantes"},
    {"Nombre": "JavaScript9", "Paradigma": "Multiparadigma", "Popularidad": "Moderada", "Usabilidad": "Intermedio"},
    {"Nombre": "Java9", "Paradigma": "Multiparadigma", "Popularidad": "Moderada", "Usabilidad": "Avanzado"},
    
    {"Nombre": "Python10", "Paradigma": "Multiparadigma", "Popularidad": "Baja", "Usabilidad": "Amigable para principiantes"},
    {"Nombre": "JavaScript10", "Paradigma": "Multiparadigma", "Popularidad": "Baja", "Usabilidad": "Intermedio"},
    {"Nombre": "Java10", "Paradigma": "Multiparadigma", "Popularidad": "Baja", "Usabilidad": "Avanzado"}
]

# Agregar reglas al sistema experto basado en la base de datos
for lenguaje in base_de_datos:
    sistema_experto_lenguajes.agregar_regla(
        {"Paradigma": lenguaje["Paradigma"], "Popularidad": lenguaje["Popularidad"], "Usabilidad": lenguaje["Usabilidad"]},
        lenguaje["Nombre"]
    )

class InterfazExploradorLenguajes:
    def __init__(self, root):
        self.root = root
        self.root.title("Explorador de Lenguajes de Programación")

        self.sistema_experto_lenguajes = sistema_experto_lenguajes  # Usar el sistema experto

        # Combobox para Marcas
        self.label_paradigma = ttk.Label(root, text="Paradigma:")
        self.label_paradigma.grid(column=0, row=1, padx=10, pady=5, sticky=tk.W)
        self.paradigmas = ttk.Combobox(root, values=["Imperativo", "Orientado a Objetos", "Multiparadigma"])
        self.paradigmas.grid(column=1, row=1, padx=10, pady=5)

        # Combobox para Características
        self.label_popularidad = ttk.Label(root, text="Popularidad:")
        self.label_popularidad.grid(column=0, row=2, padx=10, pady=5, sticky=tk.W)
        self.popularidades = ttk.Combobox(root, values=["Alta", "Moderada", "Baja"])
        self.popularidades.grid(column=1, row=2, padx=10, pady=5)

        # Combobox para Preferencias de Diseño
        self.label_usabilidad = ttk.Label(root, text="Nivel de Usabilidad:")
        self.label_usabilidad.grid(column=0, row=3, padx=10, pady=5, sticky=tk.W)
        self.usabilidades = ttk.Combobox(root, values=["Amigable para principiantes", "Intermedio", "Avanzado"])
        self.usabilidades.grid(column=1, row=3, padx=10, pady=5)

        # Botón para Enviar
        self.boton_enviar = ttk.Button(root, text="Enviar", command=self.mostrar_sugerencia)
        self.boton_enviar.grid(column=0, row=4, columnspan=2, pady=10)

    def mostrar_sugerencia(self):
        preferencias = {
            "Paradigma": self.paradigmas.get(),
            "Popularidad": self.popularidades.get(),
            "Usabilidad": self.usabilidades.get()
        }

        # Sugerir un lenguaje de programación utilizando el sistema experto
        lenguaje_sugerido = self.sistema_experto_lenguajes.obtener_sugerencia(preferencias)

        # Mostrar la sugerencia en una nueva ventana
        ventana_sugerencia = tk.Toplevel(self.root)
        app_sugerencia = InterfazSugerenciaLenguaje(ventana_sugerencia, lenguaje_sugerido)
        ventana_sugerencia.mainloop()

class InterfazSugerenciaLenguaje:
    def __init__(self, root, lenguaje_sugerido):
        self.root = root
        self.root.title("Sugerencia de Lenguaje de Programación")

        frame_principal = ttk.Frame(root)
        frame_principal.grid(column=0, row=0, pady=10, padx=10)

        self.label_nombre = ttk.Label(frame_principal, text="Lenguaje Sugerido: " + lenguaje_sugerido)
        self.label_nombre.grid(column=0, row=0, pady=10, padx=10, sticky=tk.W)

        self.label_populares = ttk.Label(frame_principal, text="Lenguajes más Populares:")
        self.label_populares.grid(column=1, row=0, pady=10, padx=10, sticky=tk.W)

        self.tabla_populares = ttk.Treeview(frame_principal, columns=("Nombre", "Popularidad"))
        self.tabla_populares.heading("#0", text="Nombre")
        self.tabla_populares.heading("#1", text="Popularidad")
        self.tabla_populares.grid(column=1, row=1, pady=10, padx=10, rowspan=2, sticky=(tk.W, tk.N))

        datos_ejemplo = [("Python", "Alta"), ("JavaScript", "Muy Alta"), ("Java", "Alta")]
        for dato in datos_ejemplo:
            self.tabla_populares.insert("", "end", values=(dato[0], dato[1]))

if __name__ == "__main__":
    root = tk.Tk()
    app = InterfazExploradorLenguajes(root)
    root.mainloop()
