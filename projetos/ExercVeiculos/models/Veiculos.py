class Veiculos:
    """
    Classe com as principais funcionalidade do sistema de veículos
    """
    def __init__(self, placa: str, modelo: str, marca: str, cor: str, valor_fipe: float, ano: int ) -> None:
        """
        Método construtor da classe Veiculos
        Entradas: placa(string), modelo(string), marca(string), cor(string) e valor_fipe(float), ano(int)
        """
        self.__placa = placa
        self.__modelo = modelo
        self.__marca = marca
        self.__cor = cor
        self.__valor_fipe = valor_fipe
        self.__ano = ano
    
    def __str__(self) -> str:
        """Método que retorna uma string com as informações do veículo"""
        infos = f"Placa: {self.__placa}\n"
        infos += f"Modelo: {self.__modelo}\n"
        infos += f"Marca: {self.__marca}\n"
        infos += f"Ano: {self.__ano}\n"
        infos += f"Cor: {self.__cor}\n"
        infos += f"Valor Fipe: {self.__valor_fipe}\n"
        return infos

    def get_placa(self) -> str:
        """Método que retorna a placa do veículo"""
        return self.__placa