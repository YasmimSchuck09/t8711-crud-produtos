import tkinter as tk
from tkinter import messagebox

janela = tk.Tk()

janela.title("Meu primeiro sisteminha")
janela.geometry("800x600")
janela.resizable(False, False)

lbl_titulo = tk.Label(
    janela,
    text = "EXEMPLO DE CADASTRO",
    font= ("Arial",12,"bold")
)

# ----------------------------- LABEL TITULO
lbl_titulo.grid(
    row = 0,
    column = 0,
    padx = 10,
    pady = 5,
    columnspan = 3
)

# ---------------------------- LABEL NOME
lbl_nome = tk.Label(
    janela,
    text = "Nome:"
)
lbl_nome.grid(
    row = 1,
    column = 0,
    padx = 10,
    pady = 5
)
# --- ENTRY (campo de entrada do nome)
txt_nome = tk.Entry(
    janela,
    width = 40
)
txt_nome.grid(
    row = 1,
    column = 1
)

# ------------------------- LABEL IDADE 
lbl_idade = tk.Label(
    janela,
    text = "Idade"
)
lbl_idade.grid(
    row = 2,
    column = 0,
    padx = 10,
    pady = 5    
)
# --- ENTRY (caixa de entrada da idade)
txt_idade = tk.Entry(
    janela,
    width= 40
)
txt_idade.grid(
    row = 2,
    column = 1
)

def printar():
    print(txt_nome.get())

# btn = botão
btn_escrever_nome = tk.Button(
    janela,
    text = "Printar o nome",
    command = printar
)

btn_escrever_nome.grid(
    row = 3,
    column = 0,
    padx = 10,
    pady = 5
)

def avaliar_idade():
    if txt_idade.get() == "":
        messagebox.showerror( #ícone vermelho de erro
            "Sisteminha",
            "Tu só pode estar de sacanagem!"
        )
        return    
    idade = int(txt_idade.get())
    if idade >= 18:
        messagebox.showinfo( #ícone quando da certo
            "Sisteminha",
            "Com " + str(idade) + " você é bem vindo"
        )
        return
    messagebox.showwarning( #ícone de atenção 
        "Sisteminha",
        "Fedelho!!!!"
    )
    return
    

btn_avaliar_idade = tk.Button(
    janela,
    text = "Avaliar idade",
    command = avaliar_idade
)
btn_avaliar_idade.grid(
    row = 3,
    column = 1
)

janela.mainloop()