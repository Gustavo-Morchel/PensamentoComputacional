from models.Veiculos import Veiculos
from models.Moto import Moto
from models.Carro import Carro
from models.Caminhao import Caminhao
from models.Frota import Frota
from models.VeiculoEletrico import VeiculoEletrico

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
frota1.adicionar_veiculo(caminhao_1)
frota1.adicionar_veiculo(moto_1)
frota1.adicionar_veiculo(carro_1)

distancia_percorrida = float(input("Digite a distância percorrida (em km): "))

print(F"O Caminhão consome {caminhao_1.calcular_consumo(distancia_percorrida)} litros de combustível.")
print(f"A Moto consome {moto_1.calcular_consumo(distancia_percorrida)} litros de combustível.")
print(f"O Carro consome {carro_1.calcular_consumo(distancia_percorrida)} litros de combustível.")
print(f"O Veículo Elétrico consome {carroEletrico.calcular_consumo(distancia_percorrida)} kHw de energia.")
print(F"A frota tem {frota1.__str__()} veículos {frota1.calcular_total_consumo(distancia_percorrida)} litros de combustível.")

print(voyage == voyage)

