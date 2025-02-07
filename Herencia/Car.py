from Vehicle import Vehicle

class Car(Vehicle):
    def __init__(self, paramType: str, paramId: int, paramColor: str, 
                paramBrand: str, paramLlantas: str):
        super().__init__(paramType, paramId, paramColor, paramBrand, paramLlantas)

    def abrirPuerta(self):
        print("Abriendo puerta")