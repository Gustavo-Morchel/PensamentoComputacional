import time

class ContaCorrente:
    '''
    OBS: Operações no histórico> 0 - Sacar, 1 - Depositar e 2 - Transferir
    '''
    def __init__(self,titular: str, chavePix: list = [], limite: float = 500, historico:list = [], saldo: float = 0) -> None : 
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite
        self.__chavePix = chavePix
        self.__historico = historico
    
    def depositar(self, valor: float, remetente: str = None) -> bool:
        '''
        Método que realiza o depósito na conta bancária
        Entradas: valor(float) e remetente(string)
        Return:True, se a operação foi realizada com sucesso. False, se a operação não foi realizada
        '''
        op = 1
        #detecta se é uma transferência
        if remetente != None:
            op =2
        if valor > 0:
            self.__saldo += valor
            self.__historico.append({"operacao": op,
                                   "remetente": remetente,
                                   "destinatario": self.__titular,
                                   "valor": valor,
                                   "saldo": self.__saldo,
                                   "data e tempo": int(time.time())})
            return True
        else:
            print(f"O valor {valor} é inválido!")
            return False

    def sacar(self, valor: float, destinatario: str = None)-> bool:
        '''
        Método que realiza o saque na conta bancária
        Entradas: valor(float) e destinatario(string)
        Return:True, se a operação foi realizada com sucesso. False, se a operação não foi realizada
        '''
        op = 0
        if destinatario != None:
            op = 2
        if valor <= self.__saldo:
            self.__saldo -= valor
            self.__historico.append({"operacao": op,
                                   "remetente": self.__titular,
                                   "destinatario": destinatario,
                                   "valor": valor,
                                   "saldo": self.__saldo,
                                   "data e tempo": int(time.time())})
            print(f"Saque realizado!")
            return True
        else: #Sem grana na conta
            a = input(f"Deseja utilizar o limite? ({self.__limite}) (S/N) ")
            if a == 's':
                if (self.__saldo + self.__limite) >= valor:
                    self.__saldo -= valor
                    print(f"Saque realizado!")
                    return True
                else:
                    print("Saldo e limite insuficiente")
            else:
                print("Operação com limite cancelada!")
        return False



    def transferir(self,destinatario: str, valor: float )-> bool:
        """
        Método para transferir um valor entre duas contas
        Entradas: valor(float) e objeto ContaBancaria do destinatário
        Saida: Se ok -> True, se não -> False.
        """

        #se o saque ocorrer com sucesso 
        if self.sacar(valor,destinatario.titular):
            #deposita na conta do destinatario
            destinatario.depositar(valor,self.__titular)


    def exibirHistorico(self):
        print("Histórico de Transações:")
        for transacao in self.__historico:
            dataTempo = time.localtime(transacao["data e tempo"])
            print(f"OP: {transacao['operacao']} \nRemetente: {transacao['remetente']} \nDestinatário: {transacao['destinatario']} \nSaldo: {transacao['saldo']} \nValor: {transacao['valor']} \nData: {dataTempo.tm_mday}/{dataTempo.tm_mon}/{dataTempo.tm_year} \nHora: {dataTempo.tm_hour}:{dataTempo.tm_min}:{dataTempo.tm_sec}")


    ##Getters (Get)
    @property
    def titular(self):
        return self.__titular
    
    @property
    def saldo(self):
        return self.__saldo
    
    @property
    def limite(self):
        return self.__limite
    
    @property
    def historico(self):
        return self.__historico
    
    @property
    def chavePix(self):
        return self.__chavePix

