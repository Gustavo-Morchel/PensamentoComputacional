class MinhaExcecao(Exception):
    pass

    def dividir(a,b):
        if b == 0:
            #raise se comunica com except e retorna o erro
            raise MinhaExcecao("Divisão por zero não é permitida") 
        return a / b

