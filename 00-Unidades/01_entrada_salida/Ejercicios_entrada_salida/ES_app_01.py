import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:
apellido:
---
Ejercicio: entrada_salida_01
---
Enunciado:
Al presionar el  botón, se debe mostrar un mensaje como el siguiente "Esto no anda, funciona".
'''

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        self.title("UTN FRA")

        self.btn_mostrar = customtkinter.CTkButton(
            master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")

    def btn_mostrar_on_click(self):
        edad = 22 # Operador de asignacion
        # pep8 -> 4 espacios
        # pep8 -> 79 caracteres por linea
        edadpromediodejugadoresdebasquet = 23.2 # Tipo de dato: float

        # notacion snake case
        edad_promedio_de_jugadores_de_basquet = 23.2
        # notacion camel case
        edadPromedioDeJugadoresDeBasquet = 23.2
        # notacion pascal case
        EdadPromedioDeJugadoresDeBasquet = 23.2
        # notacion hungara
        iEdadPromedioDeJugadoresDeBasquet = 23.2

        nombre = "Jorge" # Tipo de dato string
        verificado = True # Tipo de dato boolean
        vacio = None # Tipo de dato None (variable sin valor)

        print(edad)
        print(edad_promedio_de_jugadores_de_basquet)

        # alert("Hola PY!", "Esto es un mensaje de prueba")
        # respuesta_question = question("Hola PY!", "Esto es un mensaje de prueba")
        
        # print(respuesta_question)

        respuesta_prompt = prompt("Hola PY!", "Esto es un mensaje de prueba")

        print(respuesta_prompt)
        

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
