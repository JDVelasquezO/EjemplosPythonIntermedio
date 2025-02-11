from enum import Enum

class Rol(Enum):
    # NAME = VALUE
    GERENTE = 1
    EMPLEADO = 2
    CONSERJE = 3
    ADMINISTRADOR = 4

print(Rol.CONSERJE.name)
print(list(Rol))

for rol in (Rol):
    print(f"{rol.value}: {rol.name}")
