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
    
def limpiarFormulario(self):
   self.cajaTxtCodigo.delete(0,END)
   

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

obtieneTxt = cajaTxt.get() # obtiene el txt de la caja 
def CreaUsuario():
    usuario= InventarioTienda().nuevoUsuario(usuarioN=obtieneTxt)
    if usuario==True:
        messagebox.showinfo(message="Aceptar", title="Se creo exitosamente")
    else:
        messagebox.showinfo(message="Aceptar", title="No se creo")
  
        
        
#son de los botones de la ventana 1
btnCrearUsuario = Button(text="Crear usuario", command=CreaUsuario)
btnCrearUsuario.grid(row=0, column=3, padx=5, pady=5)

# se crear la funcion vtn2 para crear otra ventana
def abrirvtn2():
    ventana2 = Toplevel()
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
    ventana3 = Toplevel()
    ventana3.geometry("450x450")
    ventana3.title("Inventario")
    
    #se agregan todo los datos para guardar
    txtTitulo= Label(ventana3,text="Inventario entrada de la tienda")
    txtTitulo.grid(row=0, column=0, padx=10, pady=10)
    
    #txt de codigo
    txtCodigo= Label(ventana3,text="Código: ")
    txtCodigo.grid(row=1, column=0, padx=10, pady=10)
    #se agrega la caja que almacena el dato de codigo
    cajaTxtCodigo = Entry(ventana3, font="Arial 12")
    cajaTxtCodigo.grid(row=1, column=1, padx=2, pady=5) 
    
    #txt de Nombre Producto
    txtNombreProducto= Label(ventana3,text="Nombre del Producto: ")
    txtNombreProducto.grid(row=2, column=0, padx=10, pady=10)
    #se agrega la caja que almacena el dato de nombre producto
    cajaTxtNombreProducto = Entry(ventana3, font="Arial 12")
    cajaTxtNombreProducto.grid(row=2, column=1, padx=2, pady=5) 
    
    #txt de Talla
    txtTalla= Label(ventana3,text="Talla: ")
    txtTalla.grid(row=3, column=0, padx=10, pady=10)
    #se agrega la caja que almacena el dato de talla
    cajaTxtTalla = Entry(ventana3, font="Arial 12")
    cajaTxtTalla.grid(row=3, column=1, padx=2, pady=5) 
    
    #txt de Cantidad
    txtCantidad= Label(ventana3,text="Cantidad: ")
    txtCantidad.grid(row=4, column=0, padx=10, pady=10)
    #se agrega la caja que almacena el dato de talla
    cajaTxtCantidad = Entry(ventana3, font="Arial 12")
    cajaTxtCantidad.grid(row=4, column=1, padx=2, pady=5) 
        
    #txt de Precio c/u
    txtPrecioCu= Label(ventana3,text="Precio C/U: ")
    txtPrecioCu.grid(row=5, column=0, padx=10, pady=10)
    #se agrega la caja que almacena el dato de talla
    cajaTxtPrecioCu = Entry(ventana3, font="Arial 12")
    cajaTxtPrecioCu.grid(row=5, column=1, padx=2, pady=5) 
     
    #txt de PrecioTotal
    txtPrecioTotal= Label(ventana3,text="Precio Total: ")
    txtPrecioTotal.grid(row=6, column=0, padx=10, pady=10)
    #se agrega la caja que almacena el dato de talla
    cajaTxtPrecioTotal = Entry(ventana3, font="Arial 12")
    cajaTxtPrecioTotal.grid(row=6, column=1, padx=2, pady=5) 
     
    #txt de Descuento
    txtDescuento= Label(ventana3,text="Descuento: ")
    txtDescuento.grid(row=7, column=0, padx=10, pady=10)
    #se agrega la caja que almacena el dato de descuento
    cajaTxtDescuento = Entry(ventana3, font="Arial 12")
    cajaTxtDescuento.grid(row=7, column=1, padx=2, pady=5) 
     
    #txt de TotalConDescuento
    txtTotalConDescuento= Label(ventana3,text="Total Con Descuento: ")
    txtTotalConDescuento.grid(row=8, column=0, padx=10, pady=10)
    #se agrega la caja que almacena el dato de talla
    cajaTxtTotalConDesc = Entry(ventana3, font="Arial 12")
    cajaTxtTotalConDesc.grid(row=8, column=1, padx=2, pady=5) 
    
    
    def obtieneCajaTxt():
        obtieneCodigo= cajaTxtCodigo.get()
        obtieneNombreProducto= cajaTxtNombreProducto.get()
        obtieneTalla= cajaTxtTalla.get()
        obtieneCantidad= cajaTxtCantidad.get()
        obtienePrecioUnidad= cajaTxtPrecioCu.get()
            
        producto= InventarioTienda().txtGuardar(codigo=obtieneCodigo,nombreProducto=obtieneNombreProducto,
                                              talla=obtieneTalla,cantidad=obtieneCantidad, 
                                             precioUnidad=obtienePrecioUnidad)
        print("Se guarda")
        
        muestra= InventarioTienda().muestraTxt()
        print(muestra)

    btnCofirmar = Button(ventana3, text="Aceptar", command= obtieneCajaTxt )
    btnCofirmar.grid(row=9, column=2, padx=10, pady=10)

    btnLimpiar = Button(ventana3, text="Limpiar", command= limpiarFormulario )
    btnLimpiar.grid(row=9, column=1, padx=10, pady=10)

def abrirvtn4():
    ventana4 = Toplevel()
    ventana4.geometry("500x500")
    ventana4.title("Inventario para modificar")
    
    #se agregan todo los datos para guardar
    txtTitulo= Label(ventana4,text="Modificar Inventario")
    txtTitulo.grid(row=0, column=0, padx=10, pady=10)



#funcion de guardar los datos del inventario
def Guardar():
    messagebox.showinfo(message="Esta ventana que se abre a continuacion es para guardar datos en el inventario", title="Guardar")
    abrirvtn3()
#funcion de modificar los datos del inventario
def Modificar():
    messagebox.showinfo(message="Esta ventana que se abre a continuacion es para realizar modificaciones al inventario", title="Modificar")
    abrirvtn4()
#funcion de eliminar los datos del inventario
def Eliminar():
    messagebox.showinfo(message="La ventana a continuacion es con el fin de eliminar datos del inventario.", title="Eliminar")
    abrirvtn3()

 
vtn.mainloop()
