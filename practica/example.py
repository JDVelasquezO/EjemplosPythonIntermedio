# ------------------------------------------- Rol.py ---------------------------------------
from enum import Enum

class Rol(Enum):
    APRENDIZ = 1
    PROFESIONAL = 2

# -------------------------------------------  Lugar.py
class Lugar:
    def __init__(self, nombre, direccion, telefono):
        self.nombre = nombre
        self.direccion = direccion
        self.telefono = telefono

    def __str__(self):
        return f"{self.nombre} - {self.direccion}"

# -------------------------------------------  Persona.py
class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
        self.rol = Rol.APRENDIZ
        self.lugares = []

    def setRol(self, rol):
        self.rol = rol

    def addLugar(self, lugar):
        self.lugares.append(lugar)

    def __str__(self):
        return f"La persona {self.nombre} tiene rol: {self.rol} y lugares: [{', '.join(map(str, self.lugares))}]"

# -------------------------------------------  Main.py
persona1 = Persona('Daniel', 'Velasquez')
persona1.setRol(Rol.PROFESIONAL)

lugar1 = Lugar("Usac", "Zona 12", "78945612")
lugar2 = Lugar("Zoologico", "Zona 13", "78945614")

persona1.addLugar(lugar1)
persona1.addLugar(lugar2)

print(persona1)
