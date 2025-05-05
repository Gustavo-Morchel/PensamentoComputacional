class Livro:
    def __init__(self,titulo,autor,ano_publicacao,numero_paginas,pagina_atual):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.numero_paginas = numero_paginas
        self.pagina_atual = pagina_atual
    
    def avancar_pagina(self):
        if self.pagina_atual >= 0 and self.pagina_atual < self.numero_paginas:
           self.pagina_atual +=1
        else:
           print("Não tem como")
    def voltar_pagina(self):
        if self.pagina_atual >= 1 and self.pagina_atual <= self.numero_paginas:
            self.pagina_atual -=1
        else:
            print("Não tem como descer mais que 0")
    def exibir_informacoes(self):
        print(f"Titulo: {self.titulo},  Autor: {self.autor}, Ano de Publicação: {self.ano_publicacao}, Número de Páginas: {self.numero_paginas}, Página Atual: {self.pagina_atual}  ")