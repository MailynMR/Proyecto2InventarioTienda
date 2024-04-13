# importa
from Registro import Registro
from Singleton import Database


class InventarioTienda:

    def __init__(self):
        self.usuario = []

    def revisarUsuario(self, usuarioA):  # valida si el usuario ya esta en la base o si no
        return Database().CrearUsuario(usuarioA)  # es mi arreglo se encuentra vacio

    def almacenarUsuario(self, usuarioV):
        self.usuario = Database().UsuarioViejo(usuarioV)

    # def escribirFichero(self, mensaje): # Escribe un mensaje en un fichero
    #     with open ('Inventario.txt', 'w') as fichero:
    #         fichero.write(mensaje)

    # def leefichero()# Leer el mensaje del fichero
    #     mensaje=""
    #     with open ('Inventario.txt', 'r') as fichero
    #     # Borra el contenido del fichero para dejarlo vacío
    #     f = open ('Inventario.txt', 'w') as fichero
    #     f.close()
    #     return mensaje

    # #va en el main
    # #escribirFichero("Esto es un mensaje")
    # #print(lee_fichero())
