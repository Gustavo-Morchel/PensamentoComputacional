from models.ContaCorrente import ContaCorrente
from utils.ferramentas import Ferramentas

contaTeste = ContaCorrente("ContaTeste", 500, [], 1000)

contasBanco = []
contasBanco.append(contaTeste)

ferramentas = Ferramentas()

titular = input("Digite o seu nome: ")
contasBanco.append(ContaCorrente(titular))

while True:
    condicao = int(input("Digite: \n1- Depositar \n2- Sacar \n3- Transferir \n4- Sair\n"))
    if condicao == 1:
        nome = input("Digite o nome do titular: ")
        conta = ferramentas.buscar_conta(nome, contasBanco)
        if conta:
            valor = float(input("Digite o valor a ser depositado: "))
            conta.depositar(valor)
            conta.exibirHistorico()
        else:
            print("Conta não encontrada!")
    elif condicao == 2: 
        nome = input("Digite o nome do titular: ")
        conta = ferramentas.buscar_conta(nome, contasBanco)
        if conta:
            valor = float(input("Digite o valor a ser sacado: "))
            conta.sacar(valor)
            conta.exibirHistorico()
        else:
            print("Conta não encontrada!")
    elif condicao == 3:
        nome = input("Digite o nome do titular: ")
        conta = ferramentas.buscar_conta(nome, contasBanco)
        if conta:
            valor = float(input("Digite o valor a ser transferido: "))
            nome_destinatario = input("Digite o nome do destinatário: ")
            destinatario = ferramentas.buscar_conta(nome_destinatario, contasBanco)

            if destinatario:
                conta.transferir(destinatario, valor)
                conta.exibirHistorico()
                destinatario.exibirHistorico()
            else:
                print("Destinatário não encontrado!")
        else:
            print("Conta não encontrada!")
    elif condicao == 4:
        print("Saindo do sistema...")
        break
