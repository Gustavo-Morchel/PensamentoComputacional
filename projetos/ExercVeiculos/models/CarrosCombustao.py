from .Veiculos import Veiculos

class CarrosCombustao(Veiculos):
    """
    Classe que representa os veículos do tipo Carros a combustão
    """
    def __init__(self, placa: str, modelo: str, marca: str, cor: str, valor_fipe: float, ano: int, combustivel: str, nPortas: int, nAssentos: int, nCilindradas: int, nCambio: str) -> None:
        """Método construtor da classe CarrosCombustao"""
        super().__init__(placa,modelo,marca,cor,valor_fipe,ano)
        self.__combustivel = combustivel
        self.__nPortas = nPortas
        self.__nAssentos = nAssentos
        self.__nCilindradas = nCilindradas
        self.__nCambio = nCambio

    def __str__(self) -> str:
        infos = super().__str__()
        infos += f"Combustível: {self.__combustivel}\n"
        infos += f"Número de Portas: {self.__nPortas}\n"
        infos += f"Número de Assentos: {self.__nAssentos}\n"
        infos += f"Número de Cilindradas: {self.__nCilindradas}\n"
        infos += f"Câmbio: {self.__nCambio}\n"
        return infos 