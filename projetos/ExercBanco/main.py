from models.ContaCorrente import ContaCorrente
from utils.ferramentas import Ferramentas

contaTeste = ContaCorrente("ContaTeste", 500, [], 1000, [])

contasBanco = []
contasBanco.append(contaTeste)
ferramentas = Ferramentas()
i = 0
listaPix = list()

titular = input("Digite o seu nome: ")
while i < 3:
    chave = input(f"Digite sua {i+1}º chave PIX:  ")
    if chave.len() > 5:
        listaPix.append(chave)
        i += 1
        continue
    else:
        print("Chave muito curta ")
    
contasBanco.append(ContaCorrente(titular,listaPix))

while True:
    condicao = int(input("Digite: \n1- Depositar \n2- Sacar \n3- Transferir \n4- Fazer Pix \n5- Excluir conta \n6- Sair\n"))
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
        pass

    elif condicao == 5:
        deletar = input("Digite o nome do seu titular para confirmar a exclusão da conta") 
        for conta in contasBanco:
            if deletar == conta.titular:
                if conta.saldo > 0:
                    transfere = input(f"Você tem R$:{conta.saldo} precisa transferir este dinheiro para alguma conta, Digite o nome do titular: ")
                    for conta2 in contasBanco:
                        if conta2.titular == transfere:
                            conta.transferir(conta2,conta.saldo)
                            conta.exibirHistorico()
                            break
                contasBanco.remove(conta)
                break
    elif condicao == 6:
        print("Saindo do sistema...")
        break

