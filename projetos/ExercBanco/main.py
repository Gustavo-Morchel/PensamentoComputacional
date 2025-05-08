from models.ContaCorrente import ContaCorrente
from utils.ferramentas import Ferramentas

gustavo = ContaCorrente("Gustavo", 1000, 500, [])
# gustavo.depositar(50)
# teste = ContaCorrente("Teste", 2000, 500, [])

# # gustavo.depositar(150)
# # gustavo.sacar(100)
# # gustavo.exibirHistorico()

# gustavo.transferir(teste, 50)

# gustavo.exibirHistorico()
# teste.exibirHistorico()

contasBanco = []

titular = input("Digite o seu nome: ")
contasBanco.append(ContaCorrente(titular))

while True:
    condicao = int(input("Digite: \n1- Depositar \n2- Sacar \n3- Transferir \n4- Sair\n"))
    if condicao == 1:
        conta = Ferramentas.buscar_conta(input("Digite o nome do titular: "))
    elif condicao == 2:
        pass
    elif condicao == 3:
        pass
    elif condicao == 4:
        pass
        

    

