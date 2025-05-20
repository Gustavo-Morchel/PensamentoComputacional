from .Veiculos import Veiculos
class Caminhao(Veiculos):
    
    def __init__(self, placa: str, modelo: str, marca: str, cor: str, valor_fipe: float, ano: int) -> None:
        """Método construtor da classe Caminhão"""
        Veiculos.__init__(self, placa,modelo,marca,cor,valor_fipe,ano)

    def __str__(self) -> str:
        """Método que retorna uma string com as informações do veículo"""
        infos = super().__str__()
        return infos
    
    def calcular_consumo(self, distancia: float) -> float:
        """
        Método que calcula o consumo do veículo
        Entradas: distancia(float)
        Saídas: consumo(float)
        """
        consumo_total =  distancia / 5 # 5 km/l
        return consumo_total