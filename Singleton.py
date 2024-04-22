from Perfil import Perfil
from Registro import Registro

class SingletonMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

class Database(metaclass=SingletonMeta):
    # esta es como una base de datos temporal

    # usuario guardado
    def UsuarioNuevo(self, usuario):
        nuevoUsuario = Perfil()
        nuevoUsuario.nombre=usuario
        self.usuarios.append(usuario)
        if(nuevoUsuario.nombre==usuario):
            print("El usuario ya se encuentra creado.")
            return True
        else:
            self.usuarios.append(usuario)
            print("Se agrego el nuevo usuario: ", usuario)
            return False
    
    # se busca guardar los usuario
    def CrearUsuario(self, usuario):
        nuevoPerfil = Perfil()
        nuevoPerfil.nombre = usuario
        if (self.existeUsuario(usuario=nuevoPerfil)):
            print("Bienvenido al sistema")
            return True
        else:
            print("No se encuentra registrado")
            return False

    def existeUsuario(self, usuario):
        for x in self.usuarios:
            if (x.nombre == usuario.nombre):
                return True
        return False

    def CrearTxtGuardar(self, codigo, nombreProducto, talla, cantidad, precioUnidad):
        producto= Registro()
        producto.codigo=codigo
        producto.nombreProducto=nombreProducto
        producto.talla= talla
        producto.cantidad=cantidad
        producto.precioUnidad=precioUnidad
        
        #se abre el fichero o archivo txt para guardar
        fichero = open("Inventario.txt",'a')
        
        try:
            #se abre el archivo y se escribe con write
            fichero.write("\nCodigo: ")
            fichero.write(producto.codigo)
            fichero.write("\nNombre del Producto:")
            fichero.write(producto.nombreProducto)
            fichero.write("\nTalla: ")
            fichero.write(producto.talla)
            fichero.write("\nCantidad: ")
            fichero.write(producto.cantidad)
            fichero.write("\nPrecio por unidad: ")
            fichero.write(producto.precioUnidad)
            
            print("REVISAR EL ARCHIVO DE TEXTO")
        finally:
            #se cierra el archivo con close
            fichero.close()
            
            
#---------Metodo para mostrar los datos guardados en el txt---------
    def MuestraTxtGuardado(self,):
        with open("Inventario.txt") as file_object:
            linea=file_object.read()
            print(linea)

    def __init__(self):
        self.usuarios = []  # arreglo
        nuevoUsuario = Perfil()
        nuevoUsuario.nombre = "Mailyn"
        
        self.usuarios.append(nuevoUsuario)
        
        self.producto=[] #matriz
        nuevoProducto= Registro()
        nuevoProducto.codigo= "1238910"
        nuevoProducto.nombreProducto= "Camisa"
        nuevoProducto.talla= "s"
        nuevoProducto.cantidad= 1
        nuevoProducto.precioUnidad= 4500
        nuevoProducto.precioTotal= 4500
        nuevoProducto.descuento= nuevoProducto.cantidad*0.05
        nuevoProducto.precioTotalconDesc= nuevoProducto.precioTotal+nuevoProducto.descuento
        
        self.producto.append(nuevoProducto)
