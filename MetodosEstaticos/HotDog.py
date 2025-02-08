class HotDog:
    def __init__(self, ingredents: list):
        self.ingredents = ingredents

    @staticmethod
    def verifyIngredents(ingr):
        if ingr == "Lechuga":
            print(f"{ingr} No es un ingrediente del hotdog")
            return False
        else:
            return True

    def getIngredents(self):
        return self.ingredents

ingrs = ["Pan", "Salchicha", "Mayonesa", "Mostaza", "Lechuga"]
ingrs2 = ["Pan", "Salchicha", "Mayonesa", "Mostaza"]
if all(HotDog.verifyIngredents(i) for i in ingrs):
    hotdog = HotDog(ingrs)
    print("HotDog creado correctamente")
    print(hotdog.getIngredents())

if all(HotDog.verifyIngredents(i) for i in ingrs2):
    hotdog = HotDog(ingrs)
    print("HotDog creado correctamente")

'''
hotdog = HotDog(["Pan", "Salchicha", "Mayonesa", "Mostaza"])
if all(hotdog.verifyIngredents(i) for i in hotdog.ingredents):
    print("Hotdog creado")
'''
