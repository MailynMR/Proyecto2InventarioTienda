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
obtieneUsuario = str()
obtieneCodigo = int()
obtieneNombreProducto = str()
obtieneTalla = str()
obtieneCantidad = int()
obtienePrecioUnidad = float()


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
    
# se crear la funcion vtn3 para crear otra ventana donde esta para rellenar
def abrirvtn3():
    ventana3 = Toplevel(vtn)
    ventana3.geometry("450x450")
    ventana3.title("Inventario")
    
    #se agregan todo los datos para guardar
    txtTitulo= Label(ventana3,text="Inventario entrada de la tienda")
    txtTitulo.grid(row=0, column=0, padx=10, pady=10)
    
    #txt de codigo
    txtCodigo= Label(ventana3,text="Código: ")
    txtCodigo.grid(row=1, column=0, padx=10, pady=10)
    #se agrega la caja que almacena el dato de codigo
    obtieneCodigo = cajaTxtCodigo = Entry(ventana3, font="Arial 12")
    cajaTxtCodigo.grid(row=1, column=1, padx=2, pady=5) 
    
    #txt de Nombre Producto
    txtNombreProducto= Label(ventana3,text="Nombre del Producto: ")
    txtNombreProducto.grid(row=2, column=0, padx=10, pady=10)
    #se agrega la caja que almacena el dato de nombre producto
    obtieneNombreProducto= cajaTxtNombreProducto = Entry(ventana3, font="Arial 12")
    cajaTxtNombreProducto.grid(row=2, column=1, padx=2, pady=5) 
    
    #txt de Talla
    txtTalla= Label(ventana3,text="Talla: ")
    txtTalla.grid(row=3, column=0, padx=10, pady=10)
    #se agrega la caja que almacena el dato de talla
    obtieneTalla = cajaTxtTalla = Entry(ventana3, font="Arial 12")
    cajaTxtTalla.grid(row=3, column=1, padx=2, pady=5) 
    
    #txt de Cantidad
    txtCantidad= Label(ventana3,text="Cantidad: ")
    txtCantidad.grid(row=4, column=0, padx=10, pady=10)
    #se agrega la caja que almacena el dato de talla
    obtieneCantidad = cajaTxtCantidad = Entry(ventana3, font="Arial 12")
    cajaTxtCantidad.grid(row=4, column=1, padx=2, pady=5) 
        
    #txt de Precio c/u
    txtPrecioCu= Label(ventana3,text="Precio C/U: ")
    txtPrecioCu.grid(row=5, column=0, padx=10, pady=10)
    #se agrega la caja que almacena el dato de talla
    obtienePrecioUnidad = cajaTxtPrecioCu = Entry(ventana3, font="Arial 12")
    cajaTxtPrecioCu.grid(row=5, column=1, padx=2, pady=5) 
     
    #txt de PrecioTotal
    txtPrecioTotal= Label(ventana3,text="Precio Total: ")
    txtPrecioTotal.grid(row=6, column=0, padx=10, pady=10)
    #se agrega la caja que almacena el dato de talla
    obtienePrecioTotal = cajaTxtPrecioTotal = Entry(ventana3, font="Arial 12")
    cajaTxtPrecioTotal.grid(row=6, column=1, padx=2, pady=5) 
     
    #txt de Descuento
    txtDescuento= Label(ventana3,text="Descuento: ")
    txtDescuento.grid(row=7, column=0, padx=10, pady=10)
    #se agrega la caja que almacena el dato de descuento
    obtieneDescuento = cajaTxtDescuento = Entry(ventana3, font="Arial 12")
    cajaTxtDescuento.grid(row=7, column=1, padx=2, pady=5) 
     
    #txt de TotalConDescuento
    txtTotalConDescuento= Label(ventana3,text="Total Con Descuento: ")
    txtTotalConDescuento.grid(row=8, column=0, padx=10, pady=10)
    #se agrega la caja que almacena el dato de talla
    obtieneprecioTotalconDesc = cajaTxtTotalConDesc = Entry(ventana3, font="Arial 12")
    cajaTxtTotalConDesc.grid(row=8, column=1, padx=2, pady=5) 
    
    btnCofirmar = Button(ventana3, text="Aceptar", command= obtieneCajaTxt )
    btnCofirmar.grid(row=9, column=2, padx=10, pady=10)

    
def obtieneCajaTxt(self):
    obtieneCodigo= self.cajaTxtCodigo.get()
    obtieneNombreProducto= self.cajaTxtNombreProducto.get()
    obtieneTalla=self.cajaTxtTalla.get()
    obtieneCantidad=self.cajaTxtCantidad.get()
    obtienePrecioUnidad=self.cajaTxtPrecioCu.get()
         
    self.producto= InventarioTienda.txtGuardar(codigo=obtieneCodigo,nombreProducto=obtieneNombreProducto,
                                               talla=obtieneTalla,cantidad=obtieneCantidad, 
                                               precioUnidad=obtienePrecioUnidad)
    
    
#funcion que se usa en abrirvtn4 
# aceptar es para que guarde mi archivo en el txt

def Aceptar():
    messagebox.showinfo(message="Se realizo exitosamente", title="Aceptar")
    producto=InventarioTienda.txtGuardar()
    
#funcion de guardar los datos del inventario
def Guardar():
    abrirvtn3()
#funcion de modificar los datos del inventario
def Modificar():
    messagebox.showinfo(message="Se modifico exitosamente", title="Modificar")
    abrirvtn3()
#funcion de eliminar los datos del inventario
def Eliminar():
    messagebox.showinfo(message="Se elimino exitosamente", title="Eliminar")
    abrirvtn3()
    
    
vtn.mainloop()
