from tkinter import tk
from   tkinter import messagebox, ttk
from clase1 import InventarioTienda

#variable donde guarda la txt
obtieneTxt= str()

#se hace la etiqueta de texto
txtUsuario= tk.Label(text="Ingrese su usuario: ")
txtUsuario.grid(row=0, column=0, padx=5, pady=5)

def Ingresar():
    obtieneTxt= txtUsuario.get()
    #el get de la caja va aqui
    InventarioTienda.almacenarUsuario(usuarioV=obtieneTxt)

if InventarioTienda==True:
    messagebox.showinfo(message="¡Hola, mundo!", title="Saludo")
else:
    messagebox.showinfo(messagebox="El usuario es incorrecto, intentelo nuevamente.")
        

vtn = tk.Tk()
vtn.config(width=300, height=200)
vtn.title("Tienda")
	
btnIngresar = ttk.Button(text="Tienda", command=Ingresar)
btnIngresar.grid(row=2, column=2, padx=5, pady=5)

	
vtn.mainloop()
