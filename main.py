from tkinter import * 
import tkinter as tk
from tkinter import messagebox

from clase1 import InventarioTienda

#se instancia la ventana
vtn = tk.Tk()
vtn.geometry("500x150")
vtn.title("Inventario Tienda")

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
    guardaUsuario=InventarioTienda().revisarUsuario(usuarioA=obtieneTxt)
    if guardaUsuario==True:  
        messagebox.showinfo(message="Ingresar", title="Bienvenido")
        abrirvtn2()
    else:
        messagebox.showinfo(message="El usuario es incorrecto, intentelo nuevamente.", title="Bienvenido")

#se agregan los botones a utilizar
btnIngresar = Button(text="Ingresar", command=Ingresar)
btnIngresar.grid(row=0, column=2, padx=5, pady=5)


def CreaUsuario():
    obtieneTxt = cajaTxt.get() # obtiene el txt de la caja 
    usuario= InventarioTienda.almacenarUsuario(usuarioV=obtieneTxt)

#son de los botones de la ventana 1
btnCrearUsuario = Button(text="Crear usuario", command=CreaUsuario)
btnCrearUsuario.grid(row=0, column=3, padx=5, pady=5)

# se crear la funcion vtn2 para crear otra ventana
def abrirvtn2():
    ventana2 = Toplevel(vtn)
    ventana2.geometry("450x150")
    ventana2.title("Menú Tienda")
    
    
    #Se agrega el titulo del menu
    txtInventarioTienda= Label(ventana2,text="Menú del inventario")
    txtInventarioTienda.grid(row=1, column=0, padx=10, pady=10)
    #Se agregan las opciones del menu (guardar, modificar, eliminar)
    #Se agregar el boton de guardar
    btnGuardar= Button(ventana2,text="Guardar",command=Guardar)
    btnGuardar.grid(row=2, column=0, padx=5, pady=5)
    #Se agregar el boton de modificar
    btnModificar= Button(ventana2,text="Modificar",command=Modificar)
    btnModificar.grid(row=2, column=1, padx=10, pady=10)
    #Se agregar el boton de eliminar
    btnEliminar= Button(ventana2,text="Eliminar",command=Eliminar)
    btnEliminar.grid(row=2, column=3, padx=10, pady=10)
    
    
def abrirvtn3():
    ventana3 = Toplevel(abrirvtn2)
    ventana3.geometry("450x450")
    ventana3.title("Inventario")
    
#funcion de guardar los datos del inventario
def Guardar():
    messagebox.showinfo(message="Se guardo exitosamente", title="Guardar")
   
    #se agregan todo los datos para guardar
    txtTitulo= Label(abrirvtn3,text="Inventario entrada de la tienda")
    txtTitulo.grid(row=0, column=0, padx=10, pady=10)
    
    #txt de codigo
    txtCodigo= Label(abrirvtn3,text="Código: ")
    txtCodigo.grid(row=0, column=1, padx=10, pady=10)
    #txt de codigo
    txtNombreProducto= Label(abrirvtn3,text="Nombre del Producto: ")
    txtNombreProducto.grid(row=0, column=2, padx=10, pady=10)
    #txt de Talla
    txtTalla= Label(abrirvtn3,text="Talla: ")
    txtTalla.grid(row=0, column=3, padx=10, pady=10)
    #txt de Cantidad
    txtCantidad= Label(abrirvtn3,text="Cantidad: ")
    txtCantidad.grid(row=0, column=4, padx=10, pady=10)
    #txt de Precio c/u
    txtPrecioCu= Label(abrirvtn3,text="Precio C/U: ")
    txtPrecioCu.grid(row=0, column=5, padx=10, pady=10)
    #txt de PrecioTotal
    txtPrecioTotal= Label(abrirvtn3,text="Precio Total: ")
    txtPrecioTotal.grid(row=0, column=6, padx=10, pady=10)
    

#funcion de modificar los datos del inventario
def Modificar():
    messagebox.showinfo(message="Se modifico exitosamente", title="Modificar")

#funcion de eliminar los datos del inventario
def Eliminar():
    messagebox.showinfo(message="Se elimino exitosamente", title="Eliminar")


    
 

vtn.mainloop()
