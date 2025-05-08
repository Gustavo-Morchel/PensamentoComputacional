import time

class ContaCorrente:
    '''
    OBS: Operações no histórico> 0 - Sacar, 1 - Depositar e 2 - Transferir
    '''

    def __init__(self,titular, limite = 500, historico = [], saldo = 0):
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        self.historico = historico
    
    def depositar(self, valor, remetente = None):
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
            self.saldo += valor
            self.historico.append({"operacao": op,
                                   "remetente": remetente,
                                   "destinatario": self.titular,
                                   "valor": valor,
                                   "saldo": self.saldo,
                                   "data e tempo": int(time.time())})
            return True
        else:
            print(f"O valor {valor} é inválido!")
            return False

    def sacar(self, valor, destinatario = None):
        '''
        Método que realiza o saque na conta bancária
        Entradas: valor(float) e destinatario(string)
        Return:True, se a operação foi realizada com sucesso. False, se a operação não foi realizada
        '''
        op = 0
        if destinatario != None:
            op = 2
        if valor <= self.saldo:
            self.saldo -= valor
            self.historico.append({"operacao": op,
                                   "remetente": self.titular,
                                   "destinatario": destinatario,
                                   "valor": valor,
                                   "saldo": self.saldo,
                                   "data e tempo": int(time.time())})
            print(f"Saque realizado!")
            return True
        else: #Sem grana na conta
            a = input(f"Deseja utilizar o limite? ({self.limite}) (S/N) ")
            if a == 's':
                if (self.saldo + self.limite) >= valor:
                    self.saldo -= valor
                    print(f"Saque realizado!")
                    return True
                else:
                    print("Saldo e limite insuficiente")
            else:
                print("Operação com limite cancelada!")
        return False



    def transferir(self,destinatario, valor ):
        """
        Método para transferir um valor entre duas contas
        Entradas: valor(float) e objeto ContaBancaria do destinatário
        Saida: Se ok -> True, se não -> False.
        """

        #se o saque ocorrer com sucesso 
        if self.sacar(valor,destinatario.titular):
            #deposita na conta do destinatario
            destinatario.depositar(valor,self.titular)


    def exibirHistorico(self):
        print("Histórico de Transações:")
        for transacao in self.historico:
            dataTempo = time.localtime(transacao["data e tempo"])
            print(f"OP: {transacao['operacao']} \nRemetente: {transacao['remetente']} \nDestinatário: {transacao['destinatario']} \nSaldo: {transacao['saldo']} \nValor: {transacao['valor']} \nData: {dataTempo.tm_mday}/{dataTempo.tm_mon}/{dataTempo.tm_year} \nHora: {dataTempo.tm_hour}:{dataTempo.tm_min}:{dataTempo.tm_sec}")

    