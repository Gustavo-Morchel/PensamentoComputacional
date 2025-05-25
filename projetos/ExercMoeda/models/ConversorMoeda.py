from models.Produto import Produto
from utils.Erros import MoedaInvalidaError
class ConversorMoeda(Produto):

    def __init__(self):
        self.__usd_brl = 5.05
        self.__eur_brl = 6.14
        self.__eur_usd = 1.22
    
    def converte_preco_para_usd(self, produto: Produto) -> bool:
        moeda_atual = produto.get_moeda()
        preco = produto.get_preco()

        if moeda_atual == "USD":
            return False  # já está em USD
        elif moeda_atual == "BRL":
            novo_preco = preco / self.__usd_brl
            produto.set_preco(novo_preco)
            produto.set_moeda("USD")
            return True
        elif moeda_atual == "EUR":
            # EUR para USD
            novo_preco = preco * self.__eur_usd
            produto.set_preco(novo_preco)
            produto.set_moeda("USD")
            return True
        else:
            raise MoedaInvalidaError(f"Moeda inválida: {moeda_atual}")

    def converte_preco_para_eur(self, produto: Produto) -> bool:
        moeda_atual = produto.get_moeda()
        preco = produto.get_preco()

        if moeda_atual == "EUR":
            return False  # já está em EUR
        elif moeda_atual == "BRL":
            novo_preco = preco / self.__eur_brl
            produto.set_preco(novo_preco)
            produto.set_moeda("EUR")
            return True
        elif moeda_atual == "USD":
            # USD para EUR
            novo_preco = preco / self.__eur_usd
            produto.set_preco(novo_preco)
            produto.set_moeda("EUR")
            return True
        else:
            raise MoedaInvalidaError(f"Moeda inválida: {moeda_atual}")

    def converte_preco_para_brl(self, produto: Produto) -> bool:
        moeda_atual = produto.get_moeda()
        preco = produto.get_preco()

        if moeda_atual == "BRL":
            return False  # já está em BRL
        elif moeda_atual == "USD":
            novo_preco = preco * self.__usd_brl
            produto.set_preco(novo_preco)
            produto.set_moeda("BRL")
            return True
        elif moeda_atual == "EUR":
            novo_preco = preco * self.__eur_brl
            produto.set_preco(novo_preco)
            produto.set_moeda("BRL")
            return True
        else:
            raise MoedaInvalidaError(f"Moeda inválida: {moeda_atual}")