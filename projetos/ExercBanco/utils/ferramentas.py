class Ferramentas:
    def buscar_conta(self,titular):
            for conta in contasBanco:
                if conta.titular == titular:
                    return conta