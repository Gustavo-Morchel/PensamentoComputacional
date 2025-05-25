class Produto:

    def __init__(self, nome: str, preco: float, moeda = "BRL"):
        """
        Método construtor da classe Produto
        Entradas: nome(string), preco(float)
        """
        self.__nome = nome
        self.__preco = preco
        self.__moeda = moeda

    def __str__(self) -> str:
        """Método que retorna uma string com as informações do produto"""
        infos = f"Nome: {self.__nome}\n"
        infos += f"Preço: {self.__preco}\n"
        infos += f"Moeda: {self.__moeda}\n"
        return infos
    
    def get_nome(self) -> str:
        """Método que retorna o nome do produto"""
        return self.__nome
    
    def set_nome(self, nome: str):
        """Método que define o nome do produto"""
        self.__nome = nome
    
    def get_preco(self) -> float:
        """Método que retorna o preço do produto"""
        return self.__preco
    
    def set_preco(self, preco: float):
        """Método que define o preço do produto"""
        if preco < 0:
            raise ValueError("O preço não pode ser negativo.")
        self.__preco = preco
    
    def get_moeda(self) -> str:
        """Método que retorna a moeda do produto"""
        return self.__moeda

    def set_moeda(self, moeda: str):
        """Define a moeda do produto."""
        self.__moeda = moeda.upper()
  
    
    

