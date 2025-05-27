import tkinter as tk


def clique():
    if rotulo.cget("text") == "Olá, Mundo!":
        rotulo.config(text="Você clicou no botão!")
    else:
        rotulo.config(text="Olá, Mundo!")

janela = tk.Tk()
janela.title("Minha Janela")

rotulo = tk.Label(janela, text="Olá, Mundo!", font=("Arial", 16))
rotulo.pack(pady=20)

botao = tk.Button(janela, text="Clique aqui", command=clique)
botao.pack(pady=10)

janela.geometry("400x300")
janela.mainloop()