# Clases o Plantillas:
class User:
    def __init__(self, paramNombre, paramEdad,
                 paramActivo, paramCursos): # Inicializador o Constructor
        
        self.nombre = paramNombre
        self.edad = paramEdad
        self.activo = paramActivo
        self.cursos = paramCursos

# Objetos e Instancia: Creación de objeto
user = User("Daniel", 25, False, {})
user2 = User("Jose", 20, True, {})

print(user.nombre)
print(user2.nombre)
