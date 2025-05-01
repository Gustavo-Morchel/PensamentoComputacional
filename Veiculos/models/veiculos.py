class veiculos:
    def __init__(self, modelo, marca, placa, ano, cor, velocidade, latitude, longetude,):
        self.modelo = modelo
        self.marca = marca
        self.placa = placa
        self.ano = ano
        self.cor = cor
        self.velocidade = velocidade
        self.latitude = latitude
        self.longetude = longetude
    
    def acelerar(self):
        self.velocidade += 10
        novaLatitude = self.latitude + 1
        self.alterarLatitude(novaLatitude)
        print(f"O carro de placa {self.placa} foi acelarado até {self.velocidade} km/h")
    
    def frenagem(self):
        if self.velocidade > 0:
         self.velocidade -= 10
         print("Seu carro freiou")
        else:
           print("Ta dando ré garaio")

    def exibir_infos(self):
        print(f"O veículo {self.modelo}, de placa {self.placa} está a {self.velocidade} km/h e está na Latidude: {self.latitude}")
           
    def alterarModelo(self, modelo):
        self.modelo = modelo
   
    def alterarMarca(self, marca):
        self.marca = marca

    def alterarPlaca(self, placa):
        self.placa = placa

    def alterarAno(self, ano):
        self.ano = ano

    def alterarCor(self, cor):
        self.cor = cor

    def alterarLongetude(self, longetude):
        self.longetude = longetude

    def alterarLatitude(self, latitude):
        self.latitude = latitude

    def obterPlaca(self):
        return self.placa
    
