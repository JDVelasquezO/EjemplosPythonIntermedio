class Vehicle:
    def __init__(self, paramType, paramId: int, paramColor: str, 
                paramBrand: str, paramNumLlantas: int):
        self.paramType = paramType
        self.id = paramId
        self.color = paramColor
        self.brand = paramBrand
        self.numLlantas = paramNumLlantas

    def arrancar(self):
        print(f"El vehiculo {self.id} ha arrancado")

    def frenar(self):
        print(f"El vehiculo {self.id} ha frenado")

    def __str__(self):
        return f"""
        El vehiculo de tipo {self.paramType} tiene color {self.color},
        tiene marca {self.brand} y tiene {self.numLlantas} llantas
        """