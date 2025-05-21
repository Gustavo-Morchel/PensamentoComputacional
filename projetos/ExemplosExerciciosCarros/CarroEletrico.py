from ..ExercVeiculos.models.Veiculos import Veiculos

class CarroEletrico(Veiculos):
    """
    Classe que representa os veículos do tipo Carros elétricos
    """
    def __init__(self, placa: str, modelo: str, marca: str, cor: str, valor_fipe: float, ano: int, nAssentos: int, nPortas: int, nivel_bateria: int, tipo_bateria: str, autonomia: int) -> None:
        """Método construtor da classe CarroEletrico"""
        Veiculos.__init__(self, placa,modelo,marca,cor,valor_fipe,ano)
        self.__nAssentos = nAssentos
        self.__nPortas = nPortas
        self.__nivel_bateria = nivel_bateria
        self.__tipo_bateria = tipo_bateria
        self.__autonomia = autonomia

    def __str__(self) -> str:
        """Método que retorna uma string com as informações do veículo"""
        # Chama o método __str__ da classe pai (Veiculos)
        infos = super().__str__()
        # Adiciona as informações específicas da classe CarroEletrico
        infos += f"Número de Assentos: {self.__nAssentos}\n"
        infos += f"Número de Portas: {self.__nPortas}\n"
        infos += f"Nível de Bateria: {self.__nivel_bateria}\n"
        infos += f"Tipo de Bateria: {self.__tipo_bateria}\n"
        infos += f"Autonomia: {self.__autonomia}\n"
        return infos
    
    def get_nivel_bateria(self) -> int:
        """Método que retorna o nível de bateria do veículo"""
        return self.__nivel_bateria
    def get_tipo_bateria(self) -> str:
        """Método que retorna o tipo de bateria do veículo"""
        return self.__tipo_bateria
    def get_autonomia(self) -> int:
        """Método que retorna a autonomia do veículo"""
        return self.__autonomia