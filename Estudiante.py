# Curso.py
class Curso:
    def __init__(self, idCurso, nombreCurso):
        self.idCurso = idCurso
        self.nombreCurso = nombreCurso

    def __str__(self):
        return f"{self.nombreCurso}"

# Carnet.py
class Carnet:
    def __init__(self, noCarnet, fechaCarnet):
        self.noCarnet = noCarnet
        self.fechaCarnet = fechaCarnet

    def __str__(self):
        return self.noCarnet

# Estudiante.py
class Estudiante:
    def __init__(self, carnet, nombre):
        self.carnet = carnet # Asociación es para variables
        self.nombre = nombre
        self.cursos = [] # Agregación es para listas

    def addCursos(self, curso):
        self.cursos.append(curso)

    def __str__(self):
        return f"El estudiante {self.carnet} tiene los cursos: " + ', '.join(map(str, self.cursos))

# Main.py
mate1 = Curso(1, "Mate Basica 1")
fisica = Curso(2, "Fisica Basica")
progra = Curso(3, "Programación Básica")

carnet = Carnet("201800722", '01/01/2018')

estudiante = Estudiante(carnet, "Daniel Velasquez")

# Asignación de cursos al estudiante = Agregación
estudiante.addCursos(mate1)
estudiante.addCursos(fisica)
estudiante.addCursos(progra)

print(estudiante)


