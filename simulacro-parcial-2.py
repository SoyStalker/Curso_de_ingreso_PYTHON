import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
Enunciado:
Se desea desarrollar un programa que permita al usuario ingresar el nombre, año emitido (inferior al 2000, Superior a 2000 e inferior a 2015 y superior al 2015), si es online u offline y costo (500 a 10000) de 10 videojuegos.
Realizar las siguientes operaciones:

A - Encontrar el videojuego más caro y el más barato ingresado.
B - Calcular el promedio de los costos de los videojuegos, pero solo para aquellos que son online.
C - Encontrar los videojuegos con el costo máximo y mínimo de aquellos emitidos antes de 2015.
D - Calcular el porcentaje de videojuegos offline en relación al total de videojuegos ingresados.
E - Informar a que rango de año emitido pertenecen la mayor parte de los videojuegos vendidos.

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
    
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")

    def btn_comenzar_ingreso_on_click(self):
        costo_maximo = 0
        costo_minimo = 500

        promedio_costos = 0

        videojuegos_online = 0

        offline = 0
        total_videojuegos = 2

        contador_antes_2000 = 0
        contador_2000_2015 = 0
        contador_despues_2015 = 0

        costo_maximo_c = 0
        costo_minimo_c = 10000

        for i in range(2):
            nombre = prompt(f'Videojuego {i + 1}', 'Ingresa el nombre del videojuego')

            while nombre == '':
                nombre = prompt(f'Videojuego {i + 1}', 'No puedes ingresar un nombre vacio')

            año_emision = prompt(f'Videojuego {i + 1}', 'Ingresa el año de emisión del videojuego: ')

            while True:
                if año_emision != '-2000' and año_emision != '+2000' and año_emision != '-2015' and año_emision != '+2015':
                    año_emision = prompt(f'Videojuego {i + 1}', 'Ingresa un año válido (debe ser -2000, +2000, -2015 o +2015): ')
                else:
                    break



            estado_videojuego = prompt(f'Videojuego {i + 1}', 'Ingresa el estado del videojuego')

            while estado_videojuego != 'online' and estado_videojuego != 'offline':
                estado_videojuego = prompt(f'Videojuego {i + 1}', 'Ingresa el estado del videojuego (online o offline)')

            costo = prompt(f'Videojuego {i+1}', 'Ingresa el costo ')

            while True:
                if not costo.isdigit():
                    costo = prompt(f'Videojuego {i+1}', 'Ingresa un valor numérico para el costo (500 a 10000): ')
                elif not (500 <= int(costo) <= 10000):
                    costo = prompt(f'Videojuego {i+1}', 'Ingresa un costo dentro del rango (500 a 10000): ')
                else:
                    costo = int(costo)
                    if costo > costo_maximo:
                        costo_maximo = costo
                    else:
                        costo_minimo = costo
                    break

            #B
            if estado_videojuego == 'online':
                promedio_costos += costo
                videojuegos_online += 1
            
            #C 
            if año_emision == '-2015' or año_emision == '+2000':
                if costo > costo_maximo_c:
                    costo_maximo_c = costo
                else:
                    costo_minimo_c = costo
                    break

            #D
            if estado_videojuego == 'offline':
                offline += 1

            #E
            if año_emision == '-2000':
                contador_antes_2000 += 1
            elif año_emision == '+2000' and año_emision == '-2015':
                contador_2000_2015 += 1
            else:
                contador_despues_2015 += 1

            print(
                    f"\n Videojuego {i+1}:",
                    "\n Nombre =", nombre,
                    "\n Año de Emision =", año_emision,
                    "\n Estado =", estado_videojuego,
                    "\n Costo = $",costo,
                )
            
        # B
        if promedio_costos != 0:
            promedio_precios = promedio_costos / videojuegos_online
        else:
            promedio_precios = 0

        # C
            
        promedio_precios = promedio_costos / total_videojuegos if total_videojuegos != 0 else 0

        #D
        porcentaje_offline = (offline / total_videojuegos) * 100

        #E
        mayor_contador = max(contador_antes_2000, contador_2000_2015, contador_despues_2015)
        if mayor_contador == contador_antes_2000:
            rango_mas_comun = "antes de 2000"
        elif mayor_contador == contador_2000_2015:
            rango_mas_comun = "entre 2000 y 2015"
        else:
            rango_mas_comun = "después de 2015"
        
        alert('A', f'El videojuego mas caro cuesta {costo_maximo}\nEl videojuego mas barato cuesta {costo_minimo}')
        alert('B', f'El promedio de los costos de los videojuegos online es {promedio_precios}')
        alert('C', f'El videojuego con costo máx -2015 es {costo_maximo_c}\nEl videojuego con costo mín -2015 es {costo_minimo_c}')
        alert('D', f'El porcentaje de los offline es de {porcentaje_offline}')
        alert('E', f"La mayor parte de los videojuegos vendidos pertenecen al rango de año: {rango_mas_comun}")


        

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
