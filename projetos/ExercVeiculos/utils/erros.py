class MinhaExcecao(Exception):
    """Classe base para exceções personalizadas."""
    pass

    def DistanciaNegativa(distancia: float) -> None:
        """
        Método que verifica se a distância é negativa
        Entradas: distancia(float)
        Saídas: 
        """
        
        if distancia < 0:
            raise MinhaExcecao("Distância não pode ser negativa")
        else:
            return True  
        