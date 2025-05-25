from models.Produto import Produto
from models.ProdutoEletronico import ProdutoEletronico
from models.ProdutoAlimenticio import ProdutoAlimenticio
from models.ConversorMoeda import ConversorMoeda
from utils.Erros import MoedaInvalidaError

# Solicita os dados ao usuário
nome = input("Digite o nome do produto: ")
preco = float(input("Digite o preço do produto: "))
moeda = input("Digite a moeda do produto (BRL, USD ou EUR): ").upper()
tipo = input("Digite o tipo do produto (alimenticio ou eletronico): ").lower()

# Cria o objeto correto usando polimorfismo
if tipo == "alimenticio":
    produto = ProdutoAlimenticio(nome, preco, moeda)
elif tipo == "eletronico":
    produto = ProdutoEletronico(nome, preco, moeda)
else:
    print("Tipo de produto inválido.")
    exit()

conversor = ConversorMoeda()

# Pergunta para qual moeda deseja converter
moeda_destino = input("Para qual moeda deseja converter o preço? (USD, EUR ou BRL): ").upper()

# Tenta converter para a moeda escolhida e trata possíveis erros
try:
    if moeda_destino == "USD":
        convertido = conversor.converte_preco_para_usd(produto)
        if convertido:
            print("Conversão realizada para dólar com sucesso!")
        else:
            print("O produto já está em dólar.")
    elif moeda_destino == "EUR":
        convertido = conversor.converte_preco_para_eur(produto)
        if convertido:
            print("Conversão realizada para euro com sucesso!")
        else:
            print("O produto já está em euro.")
    elif moeda_destino == "BRL":
        convertido = conversor.converte_preco_para_brl(produto)
        if convertido:
            print("Conversão realizada para real com sucesso!")
        else:
            print("O produto já está em real.")
    else:
        print("Moeda de destino inválida.")
        exit()
    print(produto)
except MoedaInvalidaError as e:
    print(f"Erro ao converter moeda: {e}")








