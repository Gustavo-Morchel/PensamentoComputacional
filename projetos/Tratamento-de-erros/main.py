from models.testeRaise import MinhaExcecao

while True:
    try:
        n1 = input("Digite o primeiro número ou 'Sair' para sair: ")
        if n1.upper() == "sair":
            break
        n1 = float(n1)
        n2 = float(input("Digite o segundo número: "))
    except ValueError:
        print("Valor inválido. Por favor, insira um número.")
        continue

    resultado = MinhaExcecao.dividir(n1, n2)
    print(f"O resultado da divisão é: {resultado}")

    