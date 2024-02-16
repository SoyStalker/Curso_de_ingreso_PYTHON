import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:
apellido:
---
Ejercicio: while_10
---
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario 
quiera hasta que presione el botón Cancelar (en el prompt). 
Luego calcular:
    A. La suma acumulada de los negativos
    B. La suma acumulada de los positivos
    C. Cantidad de números positivos ingresados
    D. Cantidad de números negativos ingresados
    E. Cantidad de ceros
    F. Diferencia entre la cantidad de los números positivos ingresados y los negativos

Informar los resultados mediante alert()

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
    
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
        contador = 0
        numero_negativo = 0
        numero_postivo = 0
        mensaje_negativos = 'No se introdujeron numeros negativos'
        mensaje_ceros = 'No se introdujeron ceros'
        mensaje_positivos = 'No se introdujeron numeros positivos'

        contador_negativo = 0
        contador_positivo = 0
        contador_ceros = 0
        
        while True:
            numero = prompt('title', f'Ingrese el número {contador + 1}:')

            contador += 1

            if numero is None:
                break
            
            numero = int(numero)

            if numero < 0:
                numero_negativo += numero
                contador_negativo += 1
                mensaje_negativos = f'Se introdujeron {contador_negativo} negativos \n La suma de los negativos es: {numero_negativo}'

            elif numero > 0:
                numero_postivo += numero
                contador_positivo += 1
                mensaje_positivos = f'Se introdujeron {contador_positivo} positivos \n La suma de los positivos es: {numero_postivo}'
            
            elif numero == 0:
                contador_ceros += 1
                mensaje_ceros = f'Se introdujeron {contador} ceros'

        alert('Alert', f' {mensaje_negativos} \n\n {mensaje_positivos} \n\n {mensaje_ceros}')

    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()