from .CarrosCombustao  import CarroCombustao
from .CarroEletrico import CarroEletrico

class CarroConvEletrico(CarroCombustao, CarroEletrico):
    """Classe que implementea metódos especificos de um carro convertido em eletrico"""
    def __init__(self, placa: str, modelo: str, marca: str, cor: str, valor_fipe: float, ano: int,
                  combustivel: str, nPortas: int, nAssentos: int, nCilindradas: int, nCambio: str, 
                  nivel_combustivel: int, nivel_bateria: int, tipo_bateria: str, autonomia: int) -> None:
        """Método construtor da classe CarroEletrico"""
        CarroCombustao.__init__(self,placa,modelo,marca,cor,valor_fipe,ano, combustivel, nPortas, nAssentos, nCilindradas, nCambio, nivel_combustivel)
        CarroEletrico.__init__(self, placa, modelo, marca, cor, valor_fipe, ano, nAssentos, nPortas, nivel_bateria, tipo_bateria, autonomia)
       
    def __str__(self) -> str:
        """Método que retorna uma string com as informações do veículo
        Colocar só a diferença entre os dois tipos de carro
        """
        infos = CarroCombustao.__str__(self)
        infos += f"Nível de Bateria: {CarroEletrico.get_nivel_bateria(self)}\n"
        infos += f"Tipo de Bateria: {CarroEletrico.get_nivel_bateria(self)}\n"
        infos += f"Autonomia: {CarroEletrico.get_autonomia(self)}\n"
        return infos

    def abastercer(self, percentual_adicionado: float) -> bool: #Indica o retorno do metodo
        print("Carro convertido em eletrico, não é possivel abastecer")
        return False