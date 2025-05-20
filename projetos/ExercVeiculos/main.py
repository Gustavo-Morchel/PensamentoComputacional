from models.Veiculos import Veiculos
from models.CarrosCombustao import CarroCombustao
from models.CarroEletrico import CarroEletrico
from models.CarroConvEletrico import CarroConvEletrico 
from models.Moto import Moto
from models.Carro import Carro
from models.Caminhao import Caminhao
from models.Frota import Frota

voyage = Veiculos("BCE9D36", "Voyage", "Volkswagen", "Preto", 50000, 2020)
# print(voyage)

jetta_gli = CarroCombustao("JDN0A00", "Jetta GLI", "Volkswagen", "Preto", 95000, 2020, "Gasolina", 4, 5, 2000, "Automático", 50)
# print(jetta_gli)

tesla_model_s = CarroEletrico("JDN0A00", "Model S", "Tesla", "Branco", 950000, 2025, 5, 4, 100, "Lítio", 600)
# print(tesla_model_s)

fusca_eletrico = CarroConvEletrico("JDN0A01", "Fusca", "Volkswagen", "Amarelo", 50000, 2020, "Gasolina", 2, 2, 1300, "Manual", 50, 100, "Lítio", 300)
# print(fusca_eletrico)

caminhao_1 = Caminhao("JDN0AAB", "Caminhão", "Volkswagen", "Branco", 200000, 2020)
# print(caminhao_1)

moto_1 = Moto("JDN0AAK", "Moto", "Honda", "Preto", 20000, 2020)
# print(moto_1)

carro_1 = Carro("JDN0ALK", "Carro", "Volkswage1n", "Preto", 50000, 2020)  
# print(carro_1)
frota1 = Frota()
# if jetta_gli.abastercer(50):
#     print("Abastecimento realizado com sucesso")
# else:
#     print("Abastecimento não realizado")

# print(jetta_gli)

# fusca_eletrico.abastercer(50)
# print(fusca_eletrico)

distancia_percorrida = float(input("Digite a distância percorrida (em km): "))
print(F"O Caminhão consome {caminhao_1.calcular_consumo(distancia_percorrida)} litros de combustível.")
print(f"A Moto consome {moto_1.calcular_consumo(distancia_percorrida)} litros de combustível.")
print(f"O Carro consome {carro_1.calcular_consumo(distancia_percorrida)} litros de combustível.")

frota1.adicionar_veiculo(caminhao_1)
frota1.adicionar_veiculo(moto_1)
frota1.adicionar_veiculo(carro_1)

print(F"A frota tem {frota1.__str__()} veículos {frota1.calcular_total_consumo(distancia_percorrida)} litros de combustível.")



