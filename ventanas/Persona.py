class Persona:
    def __init__(self, nombre, apellido, identificador, correo, contraseña):
        self.nombre = nombre
        self.apellido = apellido
        self.identificador = identificador
        self.correo = correo
        self.contraseña = contraseña

    @staticmethod
    def iniciar_sesion(correo, contraseña, usuarios):
        # print(correo)
        # print(contraseña)
        for usuario in usuarios:
            if usuario.correo == correo and usuario.contraseña == contraseña:
                return "Inicio de sesión exitoso", usuario
        return "Credenciales incorrectas", None # None es no existe
