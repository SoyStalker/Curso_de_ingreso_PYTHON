import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:
apellido:
---
Ejercicio: listas_04
---
Enunciado:
Al presionar el botón 'INGRESAR' se le solicitará al usuario que ingrese:
    Edad.
    Genero.
Luego del ingreso, al presionar el boton 'INFORMAR' mostrar por Dialog Alert:
    A. Promedio de edad de los hombres.
    B. Porcentaje de mujeres mayores de 18 respecto al total de personas. 
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")

        self.label = customtkinter.CTkLabel(master=self, text="Edad")
        self.label.grid(row=0, column=0, padx=20, pady=10)
        self.txt_edad = customtkinter.CTkEntry(master=self)
        self.txt_edad.grid(row=0, column=1)

        self.label2 = customtkinter.CTkLabel(master=self, text="Genero")
        self.label2.grid(row=1, column=0, padx=20, pady=10)
        self.txt_genero = customtkinter.CTkEntry(master=self)
        self.txt_genero.grid(row=1, column=1)

        self.btn_ingresar = customtkinter.CTkButton(master=self, text="INGRESAR", command=self.btn_ingresar_on_click)
        self.btn_ingresar.grid(row=2, pady=10, padx=30,columnspan=2, sticky="nsew")

        self.btn_informar = customtkinter.CTkButton(master=self, text="INFORMAR", command=self.btn_informar_on_click)
        self.btn_informar.grid(row=3, pady=10, padx=30,columnspan=2, sticky="nsew")

        self.lista_edades = []
        self.lista_generos = []

    def btn_ingresar_on_click(self):
        edad = self.txt_edad.get()
        lista_edad = self.lista_edades

        if not edad.isdigit() or int(edad) < 0:
            alert('Error', 'Debes ingresar un número mayor o igual a 0 para la edad')
        else:
            edad = int(edad)
            sexo = self.txt_genero.get().lower()
            lista_genero = self.lista_generos

            if sexo == '':
                pass
            elif sexo not in ['m', 'f']:
                alert('Error', 'Debes ingresar "m" o "f" para el género')
            else:
                lista_genero.append(sexo)
                lista_edad.append(edad)

            print('edades: ', lista_edad)
            print('generos: ', lista_genero)


    def btn_informar_on_click(self):
        lista_edad = self.lista_edades
        lista_genero = self.lista_generos

        juntar_listas = list(zip(lista_genero, lista_edad))

        # A. Promedio de edad de los hombres.
        suma_edad_hombres = 0
        cantidad_hombres = 0

        for genero, edad in juntar_listas:
            if genero == 'm':
                suma_edad_hombres += edad
                cantidad_hombres += 1

        promedio_edad_hombres = round(suma_edad_hombres / cantidad_hombres)

        # B. Porcentaje de mujeres mayores de 18 respecto al total de personas.
        edad_mujeres_mayores = 0
        porcentaje_mujeres_mayores = 0

        for genero, edad in juntar_listas:
            if genero == 'f' and edad >= 18:
                edad_mujeres_mayores += edad

        total_de_personas = len(juntar_listas)

        if total_de_personas > 0:
            procentaje_mujeres_mayores = (edad_mujeres_mayores / total_de_personas) * 100
        else:
            procentaje_mujeres_mayores = 0

        alert('Información', f"Promedio de edad de los hombres: {promedio_edad_hombres}\nPorcentaje de mujeres mayores de edad es: {porcentaje_mujeres_mayores}%")

    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()