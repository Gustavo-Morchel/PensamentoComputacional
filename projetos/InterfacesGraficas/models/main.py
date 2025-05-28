import tkinter as tk



def mostrar_opcao(botao):
    texto = f"Escolha {opcao1.get()}"
    texto += f" {opcao2.get()}"
    texto += f" {opcao3.get()}"
    rotulo.config(text=texto)

    if opcao1.get() and opcao2.get() and opcao3.get():
        if botao == "Saude":
            opcao1.set(False)
        if botao == "Tempo":
            opcao3.set(False)
        if botao == "Dinheiro":
            opcao2.set(False)    

janela = tk.Tk()
janela.title("Exemplo de Interface Gráfica")
janela.geometry("300x200")
opcao1 = tk.BooleanVar()
opcao2 = tk.BooleanVar()
opcao3 = tk.BooleanVar()

tk.Radiobutton(janela, text="Dinheiro", variable=opcao1, value=True, command=lambda : mostrar_opcao("Dinheiro")).pack()
tk.Radiobutton(janela, text="Tempo", variable=opcao2, value=True, command=lambda : mostrar_opcao("Tempo")).pack()
tk.Radiobutton(janela, text="Saude", variable=opcao3, value=True, command=lambda : mostrar_opcao("Saude")).pack()

rotulo = tk.Label(janela, text="Escolheu")
rotulo.pack(pady=10)

janela.mainloop()