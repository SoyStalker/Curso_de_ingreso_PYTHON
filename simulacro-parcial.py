import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Enunciado 1 : De 5  personas que ingresan al hospital se deben tomar y validar los siguientes datos.

nombre , 
temperatura, entre 35 y 42 
sexo( f, m , nb ) 
 edad(mayor a 0)
pedir datos por prompt y mostrar por print
Punto A-informar cual fue el sexo mas ingresado
Punto B-el porcentaje de personas con fiebre y el porcentaje sin fiebre

Punto C - por el número de DNI del alumno

DNI terminados en  6 o 7

1)informar la cantidad de personas mayores de edad (desde los 18 años)
2)la edad promedio en total de todas las personas mayores de edad (18 años)
3) el nombre de la persona de sexo masculino con la temperatura mas baja(si la hay)

Todos los alumnos: 
B-informar cual fue el sexo mas ingresado
C-el porcentaje de personas con fiebre y el porcentaje sin fiebre

'''

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        self.title("UTN FRA")

        self.btn_mostrar = customtkinter.CTkButton(
            master=self, text="Mostrar", command=self.btn_mostrar_on_click)
        self.btn_mostrar.grid(row=2, pady=20, columnspan=2, sticky="nsew")

    def btn_mostrar_on_click(self):
        contador_genero_m = 0
        contador_genero_f = 0
        contador_genero_nb = 0
        contador_sexo_mas_ingresado = max(contador_genero_m, contador_genero_f, contador_genero_nb)

        contador_con_fiebre = 0
        contador_sin_fiebre = 0

        edad_total_mayores_18 = 0
        contador_mayores_18 = 0

        temp_mas_baja = 43
        nombre_min = None


        for i in range(5):
            nombre = prompt(f'Nombre (persona {i+1})', 'Ingresa tu nombre:')
            temp = prompt(f'Termometro (persona {i+1})', 'Ingrese tu temperatura!')
    
            while temp:
                if not temp.isdigit() or not (35 <= int(temp) <= 42):
                    alert('Error!', 'Ingresa una temperatura válida entre 35 y 42.')
                    temp = prompt(f'Termometro (persona {i+1})', 'Ingrese tu temperatura!') 
                else:
                    temp = int(temp)
                    break
                
            generos_validos = ['f', 'm', 'nb']
    
            sexo = prompt(f'Sexo (persona {i+1})', 'Ingresa tu genero!')
    
            while sexo not in generos_validos:
                sexo = prompt('Error', 'Ingresa un género válido (f, m, nb):')
    
            edad = prompt(f'Edad (persona {i+1})', 'Ingresa tu edad!')
    
            while edad:
                if not edad.isdigit() or int(edad) <= 0:
                    alert('Error!', 'Ingresa una edad válida mayor que cero.')
                    edad = prompt('Edad', 'Ingresa tu edad!') 
                else:
                    edad = int(edad)
                    break

            # A
                
            if contador_genero_m >= contador_genero_f and contador_genero_m >= contador_genero_nb:
                genero_mas_ingresado = 'Hombres'
            elif contador_genero_f >= contador_genero_m and contador_genero_f >= contador_genero_nb:
                genero_mas_ingresado = 'Mujeres'
            else:
                genero_mas_ingresado = 'No Binario'

            if sexo == 'm':
                contador_genero_m += 1
                if temp < temp_mas_baja:
                    nombre_min = nombre
                    temp_mas_baja = temp

            elif sexo == 'f':
                contador_genero_f += 1
            else:
                contador_genero_nb += 1

            # B
                
            if temp >= 37:
                contador_con_fiebre += 1
            else:
                contador_sin_fiebre += 1

            # C

            if edad >= 18:
                edad_total_mayores_18 += edad
                contador_mayores_18 += 1

            # Imprimir los datos de la persona
            print(
                f"\n Persona {i+1}:",
                "\n Nombre =", nombre,
                "\n temperatura =", temp,
                "\n sexo =", sexo,
                "\n edad =", edad
            )

        # Calcular la edad promedio
        if contador_mayores_18 > 0:
            edad_promedio_mayores_18 = edad_total_mayores_18 / contador_mayores_18
        else:
            edad_promedio_mayores_18 = 0

        porcentaje_con_fiebre = (contador_con_fiebre / i) * 100
        porcentaje_sin_fiebre = (contador_sin_fiebre / i) * 100
        
        # Imprime A
        alert('Fin de los datos:', f'A) Genero mas ingresado = {genero_mas_ingresado}: {max(contador_genero_m, contador_genero_f, contador_genero_nb)}')

        #Imprime B
        alert('Fin de los datos:', f'B)\n Cantidad con fiebre: {contador_con_fiebre} ({porcentaje_con_fiebre}%) \n Cantidad sin fiebre {contador_sin_fiebre} ({porcentaje_sin_fiebre}%)')

        #Imprime C
        alert('Fin de los datos:', f'C) Mayores de edad: {contador_mayores_18}\n Promedio de personas mayores de 18 años: {edad_promedio_mayores_18}')

        #Imprime D
        alert('Fin de los datos:', f'D)\n Nombre de la persona M con la temperatura mas baja: {nombre_min} ({temp_mas_baja}°C)')
        

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
