from ..ExercVeiculos.models.Veiculos import Veiculos

class CarroCombustao(Veiculos):
    """
    Classe que representa os veículos do tipo Carros a combustão
    """
    def __init__(self, placa: str, modelo: str, marca: str, cor: str, valor_fipe: float, ano: int, combustivel: str, nPortas: int, nAssentos: int, nCilindradas: int, nCambio: str, nivel_combustivel: int) -> None:
        """Método construtor da classe CarrosCombustao"""
        Veiculos.__init__(self,placa,modelo,marca,cor,valor_fipe,ano)
        self.__combustivel = combustivel
        self.__nPortas = nPortas
        self.__nAssentos = nAssentos
        self.__nCilindradas = nCilindradas
        self.__nCambio = nCambio
        self.__nivel_combustivel = nivel_combustivel

    def __str__(self) -> str:
        """Método que retorna uma string com as informações do veículo"""
        # Chama o método __str__ da classe pai (Veiculos)
        infos = super().__str__()
        # Adiciona as informações específicas da classe CarrosCombustao
        infos += f"Combustível: {self.__combustivel}\n"
        infos += f"Número de Portas: {self.__nPortas}\n"
        infos += f"Número de Assentos: {self.__nAssentos}\n"
        infos += f"Número de Cilindradas: {self.__nCilindradas}\n"
        infos += f"Câmbio: {self.__nCambio}\n"
        infos += f"Nível de combustível: {self.__nivel_combustivel}\n"
        return infos 
    
    def abastercer(self, percentual_adicionado: int) -> None: #Indica o retorno do metodo
        """Método que abastece o veículo"""
        novoPercentual = self.__nivel_combustivel + percentual_adicionado
        if novoPercentual <= 100:
            self.__nivel_combustivel = novoPercentual
            return True
        return False