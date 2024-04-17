from Perfil import Perfil


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
    def UsuarioViejo(self, usuario):
        if usuario in self.registro.usuario:
            print("Usuario encontrado")
        else:
            print("Usuario no encontrado, intentelo nuevamente.")

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

    def CrearTzt

    def __init__(self):
        self.usuarios = []  # arreglo
        nuevoUsuario = Perfil()
        nuevoUsuario.nombre = "Mailyn"
        self.usuarios.append(nuevoUsuario)
    # self.registro.crearProducto = [] # matriz
