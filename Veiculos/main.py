from models.veiculos import veiculos

corsaGSI = veiculos("Corsa GSI", "Volkswagen", "IND-1010", 1995, "Vermelho", 0 , 0, 0)

corsaGSI.acelerar()
corsaGSI.exibir_infos()

corsaGSI.frenagem()
corsaGSI.exibir_infos()

corsaGSI.frenagem()
corsaGSI.exibir_infos()

# corsaGSI.alterarPlaca("IND1A10")
# corsaGSI.exibir_infos()

# corsaGSI.placa = "NovaPlaca"

# print(corsaGSI.obterPlaca())

# placa = corsaGSI.obterPlaca()
# print(placa)



