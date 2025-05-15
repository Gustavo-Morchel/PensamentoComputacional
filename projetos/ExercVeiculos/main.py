from models.Veiculos import Veiculos
from models.CarrosCombustao import CarroCombustao
from models.CarroEletrico import CarroEletrico
from models.CarroConvEletrico import CarroConvEletrico 

voyage = Veiculos("BCE9D36", "Voyage", "Volkswagen", "Preto", 50000, 2020)
# print(voyage)

jetta_gli = CarroCombustao("JDN0A00", "Jetta GLI", "Volkswagen", "Preto", 95000, 2020, "Gasolina", 4, 5, 2000, "Automático", 50)
# print(jetta_gli)

tesla_model_s = CarroEletrico("JDN0A00", "Model S", "Tesla", "Branco", 950000, 2025, 5, 4, 100, "Lítio", 600)
# print(tesla_model_s)

fusca_eletrico = CarroConvEletrico("JDN0A01", "Fusca", "Volkswagen", "Amarelo", 50000, 2020, "Gasolina", 2, 2, 1300, "Manual", 50, 100, "Lítio", 300)
print(fusca_eletrico)


# print(jetta_gli)

# if jetta_gli.abastercer(50):
#     print("Abastecimento realizado com sucesso")
# else:
#     print("Abastecimento não realizado")

# print(jetta_gli)

fusca_eletrico.abastercer(50)
print(fusca_eletrico)