from tkinter import * 
import tkinter as tk
from tkinter import messagebox

from clase1 import InventarioTienda

#se instancia la ventana
vtn = tk.Tk()
vtn.geometry("450x150")
vtn.title("Tienda")

#variable donde guarda la txt
obtieneTxt= str()

#se hace la etiqueta de texto
txtUsuario= Label(text="Ingrese su usuario: ")
txtUsuario.grid(row=0, column=0, padx=5, pady=5)

#se hace la caja de texto 
obtieneTxt = cajaTxt = Entry(vtn, font="Arial 12")
cajaTxt.grid(row=0, column=1, padx=2, pady=5) 

#se hace la funcion de ingresar
def Ingresar():
    obtieneTxt= cajaTxt.get()
    #el get de la caja va aqui
    InventarioTienda.revisarUsuario(usuarioV=obtieneTxt)
    if InventarioTienda==True:  
        messagebox.showinfo(message="Ingresar", title="Bienvenido")
        #vtn2()
    else:
        messagebox.showinfo(messagebox="El usuario es incorrecto, intentelo nuevamente.", titles="Bienvenido")

 
      
#se agregan los botones a utilizar
btnIngresar = Button(text="Tienda", command=Ingresar)
btnIngresar.grid(row=0, column=2, padx=5, pady=5)

def prueba():
    messagebox.showinfo(messagebox="Prueba 1", titles="Prueba")

# se crear la funcion vtn2 para crear otra ventana
def abrirvtn2():
    ventana2 = Toplevel(vtn)
    ventana2.geometry("450x150")
    ventana2.title("Inventario Ropa")

# se crean los label y las cajas de la ventana 2 (vtn2)	
#se hace la etiqueta de 

txtInventarioTienda= Label(text="INVENTARIO ENTRADA DE LA TIENDA")
txtInventarioTienda.grid(row=1, column=0, padx=5, pady=5)
btnPrueba= Button(text="Prueba", command=prueba)
    
btnVnt2= Button(text="Vtn2", command=abrirvtn2)
btnVnt2.grid(row=0, column=3, padx=5, pady=5)

vtn.mainloop()
