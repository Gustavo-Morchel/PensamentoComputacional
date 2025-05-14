from models.Veiculos import Veiculos
from models.CarrosCombustao import CarrosCombustao

voyage = Veiculos("BCE9D36", "Voyage", "Volkswagen", "Preto", 50000, 2020)
print(voyage)

jetta_gli = CarrosCombustao("JDM9D36", "Jetta GLI", "Volkswagen", "Branco", 250000, 2025, "Gasolina", 4, 5, 2000, "Automático")
print(jetta_gli)