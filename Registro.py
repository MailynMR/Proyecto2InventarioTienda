# SE AGREGA TODO LO QUE SE LLENA EN EL INVENTARIO

class Registro:

    # se inicializan las variables con cada una de sus tipos de entrada
    def __init__(self):
        self.codigo = int()
        self.nombreProducto = str()
        self.talla = str()
        self.cantidad = int()
        self.precioUnidad = float()

    def crearProducto(self, codigo, nombreProducto, talla, cantidad, precioUnidad):
        
        self.codigo = codigo
        self.nombreProducto = nombreProducto
        self.talla = talla
        self.cantidad = cantidad
        self.precioUnidad = precioUnidad