class Filme:
    def __init__(self, titulo, genero, duracao, avaliacao):
        self.titulo = titulo
        self.genero = genero
        self.duracao = duracao
        self. avaliacao = avaliacao
    
    def avaliar(self, valor):
        if valor >= 0 and valor <=10:
            self.avaliacao = valor
        else:
            print("Não pode tem que ser entre 0 ou 10")
    def exibir_filme(self):
        print(f"Titulo: {self.titulo}, Gênero: {self.genero}, Duração: {self.duracao}, Avalicação: {self.avaliacao}")