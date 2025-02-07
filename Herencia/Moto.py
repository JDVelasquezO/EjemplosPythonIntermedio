from Vehicle import Vehicle

class Moto(Vehicle):
    def __init__(self, paramType, paramId, paramColor, paramBrand, paramLlantas):
        super().__init__(paramType, paramId, paramColor, paramBrand, paramLlantas)

    def hacerTruco(self):
        print("Haciendo caballito")