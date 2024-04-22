# importa
from Registro import Registro
from Singleton import Database

class InventarioTienda:

    def __init__(self):
        self.usuario = {}#TUPLA

#        ---------Metodo para guardar los datos en el txt---------
    def revisarUsuario(self, usuarioA):  # valida si el usuario ya esta en la base o si no
        return Database().CrearUsuario(usuarioA)  # es mi arreglo se encuentra vacio

#        ---------Metodo para guardar los datos en el txt---------
    def almacenarUsuario(self, usuarioV):
        return Database().UsuarioViejo(usuarioV)

#        ---------Metodo para guardar los datos en el txt---------
    def nuevoUsuario(self, usuarioN):
        return Database().UsuarioNuevo(usuarioN)

#        ---------Metodo para guardar los datos en el txt---------
    def txtGuardar(self, codigo, nombreProducto, talla, cantidad, precioUnidad):
        return Database().CrearTxtGuardar(codigo, nombreProducto,talla,cantidad,precioUnidad)

#        ---------Metodo para guardar los datos en el txt---------        
    def muestraTxt(self):
        return Database().MuestraTxtGuardado()
    