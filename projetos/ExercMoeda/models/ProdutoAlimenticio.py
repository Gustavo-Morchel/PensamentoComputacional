from models.Produto import Produto

class ProdutoAlimenticio(Produto):

    def __str__(self) -> str:
        """Método que retorna uma string com as informações do produto eletrônico"""
        infos = super().__str__()
        return infos