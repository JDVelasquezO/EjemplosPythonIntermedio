class Car:
    def __init__(self, paramId: int, 
                paramColor: list = ["Blanco", "Negro"],
                paramBrand: str = "Toyota"):
        self.id = paramId
        self.color = paramColor
        self.brand = paramBrand

    def arrancar(self):
        print(f"El carro {self.id} ha arrancado")

    def frenar(self):
        print(f"El carro {self.id} ha frenado")

    def __str__(self):
        return f"""
        El carro tiene color {self.color},
        tiene marca {self.brand}
        """
