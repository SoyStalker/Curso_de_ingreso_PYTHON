import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:
apellido:
---
TP: For_UTN_Factory
---
Enunciado:
UTN Software Factory está en la búsqueda de programadores para incorporar a su equipo de 
trabajo. En las próximas semanas se realizará un exhaustivo proceso de selección. Para ello se 
ingresarán los siguientes datos de los 10 postulantes para luego establecer distintas métricas 
necesarias para tomar decisiones a la hora de la selección:

Nombre
Edad (mayor de edad)
Género (F-M-NB)
Tecnología (PYTHON - JS - ASP.NET)
Puesto (Jr - Ssr - Sr)

Informar por pantalla:
a. Cantidad de postulantes de genero no binario (NB) que programan en ASP.NET o JS 
cuya edad este entre 25 y 40, que se hayan postulado para un puesto Ssr.
b. Nombre del postulante Jr con menor edad.
c. Promedio de edades por género.
d. Tecnologia con mas postulantes (solo hay una).
e. Porcentaje de postulantes de cada genero.

Todos los datos se ingresan por prompt y los resultados se muestran por consola (print)

'''

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        self.title("UTN Fra")

        self.btn_validar = customtkinter.CTkButton(
            master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")

    def btn_validar_on_click(self):

        cantidad_no_binarios = 0

        nombre_minimo = ''
        minimo = 100

        suma_edades_f = 0
        suma_edades_m = 0
        suma_edades_nb = 0
        cantidad_candidatos_f = 0
        cantidad_candidatos_m = 0
        cantidad_candidatos_nb = 0

        cantidad_python = 0
        cantidad_js = 0
        cantidad_asp_net = 0

        for i in range(10):
            nombre = prompt(f'Persona {i + 1}', 'Ingresa tu nombre:')
            edad = prompt(f'Persona {i + 1}', 'Ingresa tu edad:')
            
            while edad:
                if not edad.isdigit() or int(edad) < 18:
                    alert('Error!', 'Ingresa una edad mayor a 18.')
                    edad = prompt('Edad', 'Ingresa tu edad!') 
                else:
                    edad = int(edad)
                    break

            sexo = prompt(f'Persona {i + 1}', 'Ingrese tu sexo')
            validar_sexo = ['f', 'm', 'nb']

            while sexo not in validar_sexo:
                sexo = prompt(f'Error (persona {i+1})', 'Ingresa un género válido (f, m, nb):')
    
                if sexo in validar_sexo:
                    break

            tecnologia = prompt(f'Persona {i + 1}', 'Ingrese tu tecnologia')
            validar_t = ['python', 'js', 'asp.net']

            while tecnologia not in validar_t:
                tecnologia = prompt(f'Error (persona {i+1})', 'Ingresa una tecnologia válida (python, js o asp.net):')
    
                if tecnologia in validar_t:
                    break

            puesto = prompt(f'Persona {i + 1}', 'Ingrese tu puesto')
            validar_puesto = ['jr', 'ssr', 'sr']

            while puesto not in validar_puesto:
                puesto = prompt(f'Error (persona {i+1})', 'Ingresa un puesto válido (jr, ssr o sr):')
    
                if puesto in validar_puesto:
                    break

            # A
                
            if sexo == 'nb' and tecnologia == 'asp.net' or 'js':
                if( 25 >= edad <= 40):
                    if(puesto == 'ssr'):
                        cantidad_no_binarios += 1

            # B
                        
            if puesto == 'jr' and edad < minimo:
                minimo = edad
                nombre_minimo = nombre

            # C

            if sexo == 'f':
                suma_edades_f += edad
                cantidad_candidatos_f += 1
            if sexo == 'm':
                suma_edades_m += edad
                cantidad_candidatos_m += 1
            if sexo == 'nb':
                suma_edades_nb += edad
                cantidad_candidatos_nb += 1

            # D
                
            if tecnologia == 'python':
                cantidad_python += 1
            if tecnologia == 'js':
                cantidad_js += 1
            if tecnologia == 'asp.net':
                cantidad_asp_net += 1

            print(
                    f"\n Persona {i + 1}:",
                    "\n Nombre =", nombre,
                    "\n Edad =", edad,
                    "\n sexo =", sexo,
                    "\n tecnologia =", tecnologia,
                    "\n puesto: =", puesto
                )
            
        tecnologia_con_mas_postulantes = max(cantidad_python, cantidad_js, cantidad_asp_net)

        if tecnologia_con_mas_postulantes == cantidad_python:
            tecnologia_mas_postulantes = 'python'
        elif tecnologia_con_mas_postulantes == cantidad_js:
            tecnologia_mas_postulantes = 'js'
        else:
            tecnologia_mas_postulantes = 'asp.net'

        promedio_nb = suma_edades_nb / cantidad_candidatos_nb 
        promedio_f = suma_edades_f / cantidad_candidatos_f
        promedio_m = suma_edades_m / cantidad_candidatos_m



        total_postulantes = cantidad_candidatos_f + cantidad_candidatos_m + cantidad_candidatos_nb
        porcentaje_f = (cantidad_candidatos_f / total_postulantes) * 100
        porcentaje_m = (cantidad_candidatos_m / total_postulantes) * 100
        porcentaje_nb = (cantidad_candidatos_nb / total_postulantes) * 100
            
        alert('A', f'Cantidad de postulantes de NB es de: {cantidad_no_binarios}')
        alert('B', f'Nombre del postulante Jr con menor edad: {nombre_minimo}')
        alert('C', f'Promedio de edades por género:\n Hombres: {cantidad_candidatos_m} Promedio: {promedio_m}\n Mujeres: {cantidad_candidatos_f} Promedio: {promedio_f}\n No Binario: {cantidad_candidatos_nb} Promedio: {promedio_nb}')
        alert('D', f'Tecnologia con mas postulantes: {tecnologia_mas_postulantes} ({tecnologia_con_mas_postulantes})')
        alert('E', f'Porcentaje de postulantes de cada género:\nFemenino: {porcentaje_f}%\nMasculino: {porcentaje_m}% \nNo binario: {porcentaje_nb}%')



if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
