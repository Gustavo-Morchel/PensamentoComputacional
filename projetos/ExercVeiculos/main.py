from models.Veiculos import Veiculos
from models.Moto import Moto
from models.Carro import Carro
from models.Caminhao import Caminhao
from models.Frota import Frota
from models.VeiculoEletrico import VeiculoEletrico
from utils.erros import MinhaExcecao

voyage = Veiculos("BCE9D36", "Voyage", "Volkswagen", "Preto", 50000, 2020)
# print(voyage)

caminhao_1 = Caminhao("JDN0AAB", "Caminhão", "Volkswagen", "Branco", 200000, 2020)
# print(caminhao_1)

moto_1 = Moto("JDN0ALK", "Moto", "Honda", "Preto", 20000, 2020)
# print(moto_1)

carro_1 = Carro("JDN0ALK", "Carro", "Volkswage1n", "Preto", 50000, 2020)  
# print(carro_1)
frota1 = Frota()

carroEletrico = VeiculoEletrico("JDN0A00", "Model S", "Tesla", "Branco", 950000, 2025)
# print(carroEletrico)

#Alterando a placa do veículo usando a função set_placa da classe Veiculos
carro_1.set_placa("AAA1A11")  
print(carro_1)

#Adiciona veiculos a frota
# frota1.adicionar_veiculo(caminhao_1)
# frota1.adicionar_veiculo(moto_1)
# frota1.adicionar_veiculo(carro_1)

carroEletrico.recarregar()


# print(F"O Caminhão consome {caminhao_1.calcular_consumo(distancia_percorrida)} litros de combustível.")
# print(f"A Moto consome {moto_1.calcular_consumo(distancia_percorrida)} litros de combustível.")
# print(f"O Carro consome {carro_1.calcular_consumo(distancia_percorrida)} litros de combustível.")
# print(f"O Veículo Elétrico consome {carroEletrico.calcular_consumo(distancia_percorrida)} kHw de energia.")
# print(F"A frota tem {frota1.__str__()} veículos {frota1.calcular_total_consumo(distancia_percorrida)} litros de combustível.")

# print(voyage == voyage)
# print(caminhao_1 == moto_1)


while True:
    placa = ""
    modelo = ""
    marca = ""
    cor = ""
    valor = 0
    ano = 0

    while True:
        try:    
            escolha = int(input("Escolha o tipo de veículo a ser adicionado a frota: \n1 - Caminhão\n2 - Moto\n3 - Carro\n4 - Veículo Elétrico\n"))
            if escolha not in range(1, 5):
                continue
            distancia_percorrida = float(input("Digite a distância percorrida (em km): "))
            if MinhaExcecao.DistanciaNegativa(distancia_percorrida):
                break
        except ValueError:
            print("Opção inválida. Tente novamente.")
        except MinhaExcecao as erro:
            print(erro)
        if escolha == 1:
            while True:
                placa = input("Digite a placa do caminhão (formato: AAA1A11): ").upper()
                if (
                    len(placa) == 7 and
                    placa[0].isalpha() and
                    placa[1].isalpha() and
                    placa[2].isalpha() and
                    placa[3].isnumeric() and
                    placa[4].isalpha() and
                    placa[5].isnumeric() and
                    placa[6].isnumeric()
                ):
                    modelo = input("Digite o modelo do caminhão: ")
                    marca = input("Digite a marca do caminhão: ")
                    cor = input("Digite a cor do caminhão: ")
                    valor = float(input("Digite o valor do caminhão: "))
                    ano = int(input("Digite o ano do caminhão: "))
                    caminhao = Caminhao(placa, modelo, marca, cor, valor, ano)
                    frota1.adicionar_veiculo(caminhao)
                    print(caminhao)
                    break
                else:
                    print("Placa inválida. Tente novamente.")
        elif escolha == 2:
            while True:
                placa = input("Digite a placa da Moto (formato: AAA1A11): ").upper()
                if (
                    len(placa) == 7 and
                    placa[0].isalpha() and
                    placa[1].isalpha() and
                    placa[2].isalpha() and
                    placa[3].isnumeric() and
                    placa[4].isalpha() and
                    placa[5].isnumeric() and
                    placa[6].isnumeric()
                ):
                    modelo = input("Digite o modelo da moto: ")
                    marca = input("Digite a marca da moto: ")
                    cor = input("Digite a cor da moto: ")
                    valor = float(input("Digite o valor da moto: "))
                    ano = int(input("Digite o ano da moto: "))
                    moto = Moto(placa, modelo, marca, cor, valor, ano)
                    frota1.adicionar_veiculo(moto)
                    print(moto)
                    break
                else:
                    print("Placa inválida. Tente novamente.")
        elif escolha == 3:
            while True:
                placa = input("Digite a placa da Carro (formato: AAA1A11): ").upper()
                if (
                    len(placa) == 7 and
                    placa[0].isalpha() and
                    placa[1].isalpha() and
                    placa[2].isalpha() and
                    placa[3].isnumeric() and
                    placa[4].isalpha() and
                    placa[5].isnumeric() and
                    placa[6].isnumeric()
                ):
                    modelo = input("Digite o modelo do carro: ")
                    marca = input("Digite a marca do carro: ")
                    cor = input("Digite a cor do carro: ")
                    valor = float(input("Digite o valor do carro: "))
                    ano = int(input("Digite o ano do carro: "))
                    carro = Carro(placa, modelo, marca, cor, valor, ano)
                    frota1.adicionar_veiculo(carro)
                    print(carro)
                    break
                else:
                    print("Placa inválida. Tente novamente.")
        elif escolha == 4:
            while True:
                placa = input("Digite a placa do carro elétrico (formato: AAA1A11): ").upper()
                if (
                    len(placa) == 7 and
                    placa[0].isalpha() and
                    placa[1].isalpha() and
                    placa[2].isalpha() and
                    placa[3].isnumeric() and
                    placa[4].isalpha() and
                    placa[5].isnumeric() and
                    placa[6].isnumeric()
                ):
                    modelo = input("Digite o modelo do carro elétrico: ")
                    marca = input("Digite a marca do carro elétrico: ")
                    cor = input("Digite a cor do carro elétrico: ")
                    valor = float(input("Digite o valor do carro elétrico: "))
                    ano = int(input("Digite o ano do carro elétrico: "))
                    carroEletrico = VeiculoEletrico(placa, modelo, marca, cor, valor, ano)
                    frota1.adicionar_veiculo(moto)
                    print(moto)
                    break
                else:
                    print("Placa inválida. Tente novamente.")
        else:
            print("Opção inválida. Tente novamente entre 1 a 4.")
            break
