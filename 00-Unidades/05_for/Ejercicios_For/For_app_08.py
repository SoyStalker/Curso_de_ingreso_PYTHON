import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:
apellido:
---
Ejercicio: for_08
---
Enunciado:
Al presionar el botón 'Mostrar' pedir un número. Mostrar cada número primo entre 1 y el número ingresado, e informar la cantidad de números primos encontrados.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN Fra")
        
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")


    def btn_mostrar_on_click(self):
        numero = int(prompt('Alert', 'Ingrese un numero:'))
        cantidad_primos = 0
        
        for num in range(2, numero + 1):
            primo = True
            for i in range(2, num):
                if num % i == 0:
                    primo = False
                    break
            if primo:
                cantidad_primos += 1
        
        alert('Alert', f'Cantidad de números primos hasta {numero} son: {cantidad_primos}')
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()