class Ferramentas:
    def buscar_conta(self, titular, contas): 
        for conta in contas:
            if conta.titular == titular:
                return conta
        return False
