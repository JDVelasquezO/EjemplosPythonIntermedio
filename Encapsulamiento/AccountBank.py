class AccountBank:
    def __init__(self, idAccount: str, amount: float):
        self.__idAccount = idAccount
        self.__amount = amount
        self.__total = amount

    def getIdAccount(self):
        return self.__idAccount
    
    def getTotal(self):
        return self.__total
    
    def getAmount(self):
        return self.__amount

    def __updateTotal(self, amount):
        self.__total += amount

    def transfer(self, amountTransfer, otherAccount):
        otherAccount.__updateTotal(amountTransfer)
        print("Se ha transferido dinero")

accountBank1 = AccountBank('145789', 20)
accountBank2 = AccountBank('257863', 10)

print(accountBank1.getIdAccount())

print("Dinero actual: ", accountBank2.getTotal()) # Cantidad de dinero antes
accountBank1.transfer(5, accountBank2)
print("Dinero actual: ", accountBank2.getTotal()) # Cantidad de dinero después
