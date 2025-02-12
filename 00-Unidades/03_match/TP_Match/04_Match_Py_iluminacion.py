import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre:
apellido:
---
TP: Iluminación
---
Enunciado:
Todas las lámparas están  al mismo precio de $800 pesos final.
		A.	Si compra 6 o más  lamparitas bajo consumo tiene un descuento del 50%. 
		B.	Si compra 5  lamparitas bajo consumo marca "ArgentinaLuz" se hace un descuento del 40 % y si es de otra marca el descuento es del 30%.
		C.	Si compra 4  lamparitas bajo consumo marca "ArgentinaLuz" o “FelipeLamparas” se hace un descuento del 25 % y si es de otra marca el descuento es del 20%.
		D.	Si compra 3  lamparitas bajo consumo marca "ArgentinaLuz"  el descuento es del 15%, si es  “FelipeLamparas” se hace un descuento del 10 % y si es de otra marca un 5%.
		E.	Si el importe final con descuento suma más de $4000 se obtiene un descuento adicional de 5%.
'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__() 

        self.title("UTN Fra")

        self.label1 = customtkinter.CTkLabel(master=self, text="Marca")
        self.label1.grid(row=0, column=0, padx=10, pady=10)
        
        self.combobox_marca = customtkinter.CTkComboBox(master=self, values=["ArgentinaLuz", "FelipeLamparas","JeLuz","HazIluminacion","Osram"])
        self.combobox_marca.grid(row=0, column=1, padx=10, pady=10)

        self.label2 = customtkinter.CTkLabel(master=self, text="Cantidad")
        self.label2.grid(row=1, column=0, padx=10, pady=10)

        self.combobox_cantidad = customtkinter.CTkComboBox(master=self, values= ["1", "2","3","4","5","6","7","8","9","10","11","12"])
        self.combobox_cantidad.grid(row=1, column=1, padx=10, pady=10)
                
        self.btn_calcular = customtkinter.CTkButton(master=self, text="Calcular", command=self.btn_calcular_on_click)
        self.btn_calcular.grid(row=2, pady=20, columnspan=2, sticky="nsew")

    def btn_calcular_on_click(self):
        lampara = 800

        lamparitas = int(self.combobox_cantidad.get())
        marca = self.combobox_marca.get()

        precio_total = lamparitas * lampara

        descuento = 1
        descuento_adicional = 0

        match lamparitas:
            case 6:
                descuento *= 0.50
                alert('alert', 'Caso A: 50%')

            case 5:
                if(marca == 'ArgentinaLuz'):
                    descuento *= 0.4
                    alert('alert', 'Caso B: 40%')
                else:
                    descuento *= 0.3
                    alert('alert', 'Caso B: 30%')

            case 4:
                if(marca == 'ArgentinaLuz' or marca == 'FelipeLamparas'):
                    descuento *= 0.25
                    alert('alert', 'Caso C: 25%')
                else:
                    descuento *= 0.2
                    alert('alert', 'Caso C: 20%')

            case 3:
                if(marca == 'ArgentinaLuz'):
                    descuento *= 0.15
                    alert('alert', 'Caso D: 15%')
                elif(marca == 'FelipeLamparas'):
                    descuento *= 0.1
                    alert('alert', 'Caso D: 10%')

                else:
                    descuento *= 0.05
                    alert('alert', 'Caso D: 5%')

        precio_con_descuento = precio_total * (1 - descuento)

        # Calcular descuento adicional
        if precio_con_descuento >= 4000:
            descuento_adicional = 0.05  # 5%
            descuento_adicional_aplicado = precio_con_descuento * descuento_adicional
            precio_con_descuento -= descuento_adicional_aplicado
            descuento = 0.05

        precio_final = precio_con_descuento * (1 - descuento_adicional)
        alert('Alert', 'El precio final con el ' + str(descuento * 100) + '% de descuento es: $' + str(precio_con_descuento))
        
        

        
    
if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()