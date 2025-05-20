class Frota:

    def __init__(self) -> None:
        """Método construtor da classe Frota"""
        self.__veiculos_adicionar = []
        
        
    def __str__(self) -> str:
        
        return f"Frota com {len(self.__veiculos_adicionar)} veículos."
    
    def adicionar_veiculo(self, veiculo):
        """
        Método que adiciona um veículo à frota
        Entradas: veiculo(Veiculos)
        Saídas: None
        """
        self.__veiculos_adicionar.append(veiculo)

    def calcular_total_consumo(self, distancia: float) -> float:
        media = 0
        for veiculo in self.__veiculos_adicionar:
            media += veiculo.calcular_consumo(distancia)
        return media