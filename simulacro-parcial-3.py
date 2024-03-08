import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Enunciado:
De 5 mascotas que ingresan a una veterinaria  se deben tomar y validar los siguientes datos.

Nombre
Tipo (gato ,perro o exotico)
Peso ( entre 10 y 80)
Sexo( F o M  )
Edad(mayor a 0)

Pedir datos por prompt y mostrar por print, se debe informar:
Informe A- Cuál fue el sexo menos ingresado (F o M)
Informe B- El porcentaje de mascotas hay  por tipo  (gato ,perro o exotico)
Informe C- El nombre y tipo de la mascota menos pesada
Informe D- El nombre del perro más joven
Informe E- El promedio de peso de todas las mascotas
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
    
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")

    def btn_comenzar_ingreso_on_click(self):
        contador_genero_f = 0
        contador_genero_m = 0
        sexo_menos_ingresado = ''

        contador_gato = 0
        contador_perro = 0
        contador_exotico = 0

        peso_mascota_menos_pesada = 81
        nombre_mascota_menos_pesada = ""
        tipo_mascota_menos_pesada = ""

        nombre_perro_mas_joven = ""
        edad_perro_mas_joven = 101

        peso_total = 0

        for i in range(5):
            nombre = prompt(f'Mascota {i + 1}', 'Ingresa un nombre')

            while nombre == '':
                nombre = prompt(f'Mascota {i + 1}', 'Ingresa un nombre')

            tipo = prompt(f'Mascota {i + 1}', 'Ingresa el tipo de mascota')

            while True:
                if tipo != 'gato' and tipo != 'perro' and tipo != 'exotico':
                    tipo = prompt(f'Mascota {i + 1}', 'Ingresa el tipo de mascota (gato, perro o exotico)')
                else:
                    break

            peso = prompt(f'Mascota {i + 1}', 'Ingresa el peso de la mascota')

            while True:
                if not peso.isdigit() or 10 > int(peso) < 80:
                    peso = prompt(f'Mascota {i + 1}', 'Ingresa el peso de la mascota (entre 10 y 80)')
                else:
                    peso = int(peso)
                    break

            sexo = prompt(f'Mascota {i + 1}', 'Ingresa el sexo')

            while sexo != 'f' and sexo != 'm':
                sexo = prompt(f'Mascota {i + 1}', 'Ingresa el sexo (f o m)')

            edad = prompt(f'Mascota {i + 1}', 'Ingresa la edad')

            while True:
                if not edad.isdigit() or not 0 < int(edad) < 100:
                    edad = prompt(f'Mascota {i + 1}', 'Ingresa la edad (Mayor a 0 y menor a 100)')
                else:
                    edad = int(edad)
                    break

            print(
                    f"\n Mascota {i + 1}:",
                    "\n Nombre = ", nombre,
                    "\n Tipo = ", tipo,
                    "\n Peso = ", peso,
                    "\n Sexo = ",sexo,
                    "\n Edad = ",edad,
                )
            
            # Informe A - Cuál fue el sexo menos ingresado (F o M)
            if sexo == 'm':
                contador_genero_m += 1
            else:
                contador_genero_f += 1
            
            # Informe B- El porcentaje de mascotas que hay por tipo (gato ,perro o exotico)
                
            if tipo == 'gato':
                contador_gato += 1
            elif tipo == 'perro':
                contador_perro += 1
            else:
                contador_exotico +=1

            # Informe C- El nombre y tipo de la mascota menos pesada
            if peso < peso_mascota_menos_pesada:
                nombre_mascota_menos_pesada = nombre
                tipo_mascota_menos_pesada = tipo
                peso_mascota_menos_pesada = peso

            # Informe D- El nombre del perro más joven
            if tipo == 'perro' and edad < edad_perro_mas_joven:
                nombre_perro_mas_joven = nombre
                edad_perro_mas_joven = edad

            # Informe E- El promedio de peso de todas las mascotas
            peso_total += peso

        # A
        if contador_genero_m <= contador_genero_f:
            genero_menos_ingresado = 'Hombres'
        elif contador_genero_f <= contador_genero_m:
            genero_menos_ingresado = 'Mujeres'

        # B
        total_mascotas = contador_gato + contador_perro + contador_exotico
        porcentaje_gatos = (contador_gato / total_mascotas) * 100 if total_mascotas > 0 else 0
        porcentaje_perros = (contador_perro / total_mascotas) * 100 if total_mascotas > 0 else 0
        porcentaje_exoticos = (contador_exotico / total_mascotas) * 100 if total_mascotas > 0 else 0

        # Informe E- El promedio de peso de todas las mascotas
        promedio_peso = peso_total / 5
        
        print(
            f"\n A) El genero menos ingresado es {genero_menos_ingresado}",
            f"\n B) Porcentaje de gatos: {porcentaje_gatos}%\n Porcentaje de perros: {porcentaje_perros}%\n Porcentaje de mascotas exóticas: {porcentaje_exoticos}%",
            f"\n C) La mascota menos pesada es un {tipo_mascota_menos_pesada} llamado {nombre_mascota_menos_pesada}",
            f"\n D) El perro más joven se llama {nombre_perro_mas_joven}",
            f"\n E) El promedio de peso de todas las mascotas es: {promedio_peso} kg ",
        )



if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
