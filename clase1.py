# importa
from Registro import Registro
from Singleton import Database


class InventarioTienda:

    def __init__(self):
        self.usuario = []

    def revisarUsuario(self, usuarioA):  # valida si el usuario ya esta en la base o si no
        return Database().CrearUsuario(usuarioA)  # es mi arreglo se encuentra vacio

    def almacenarUsuario(self, usuarioV):
        return Database().UsuarioViejo(usuarioV)

    def txtGuardar(self, codigo, nombreProducto, talla, cantidad, precioUnidad):
        return Database().CrearTxtGuardar(codigo, nombreProducto,talla,cantidad,precioUnidad)
    
    def muestraTxt(self):
        return Database().MuestraTxtGuardado()
        