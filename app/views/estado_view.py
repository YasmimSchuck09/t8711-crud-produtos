import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[2]))

from app.models.estado import Estado

import tkinter as tk
from tkinter import messagebox 
from tkinter import ttk 

class Estado_View:
    def __init__(self, root, controller): #construtor
        self.root = root
        self.controller = controller
        self.configurar_janela()
        self.criar_componentes()
        self.configurar_treeview()
        self.configurar_eventos()

    def configurar_janela(self): #criação da janela
        self.root.title("CRUD de Estados") #titulo da janela
        self.root.geometry("800X600")
        self.root.resizable(False, False)

    def criar_componentes(self):
        self.lbl_titulo = tk.Label( #titulo principal
        self.root,
        text = "Cadastro de Estados",
        font = ("Arial", 16, "bold"),
        )
        self.lbl_titulo.grid(
            row = 0,
            column = 0,
            columnspan = 4,
            padx = 5,
            pady = 5
        )
        self.frm_dados = tk.LabelFrame(
            self.root,
            text = "Dados de Estado"
        )
        self.frm_dados.grid(
            row = 1,
            column = 0,
            columnspan= 4,
            padx = 10,
            pady = 5,
            sticky="ew" # local de onde ira ficar (norte, sul, leste, oeste)
        )
        
        self.lbl_id = tk.Label( #LABEL ID
            self.frm_dados,
            text = "ID:"
        )
        self.lbl_id.grid(
            row= 0,
            column = 0,
            padx = 5, 
            pady = 5,
            sticky = "w"
        )
        self.txt_id = tk.Entry(
            self.frm_dados,
            width = 10,
            state = "readonly"
        )
        self.txt_id.grid(
            row = 0,
            column = 1,
            pasx = 5,
            pady = 5,
            sticky = "w"
        )

        self.lbl_nome = tk.Label( #LABEL NOME
            self.frm_dados,
            text = "Nome:"
        )
        self.lbl_nome.grid(
            row = 1,
            column = 0,
            padx= 5,
            pady = 5,
            sticky = "w"
        )
        self.txt_nome = tk.Entry(
            self.frm_dados,
            width = 40 # espaçamento da resposta 
        )
        self.txt_nome.grid(
            row = 1,
            column = 1,
            padx = 5,
            pady = 5,
            sticky = "w"
        )
        
        self.lbl_sigla = tk.Label( # LABEL SIGLA
            self.frm_dados,
            text = "Sigla:"
        )
        self.lbl_sigla.grid(
            row = 2,
            column = 0,
            padx = 5,
            pady = 5,
            sticky = "w"
        )
        self.txt_sigla = tk.Entry(
            self.frm_dados,
            width = 5
        )
        self.txt_sigla.grid(
            row = 2,
            column = 2,
            padx = 5,
            pady = 5,
            sticky = "w"
        )

        self.tbl_estado = ttk.Treeview(
            self.root,
            height = 10
        )
        self.tbl_estado.grid(
            row = 3,
            column = 0,
            columnspan= 4,
            padx = 10,
            pady = 10,
            sticky = "nsew"
        )

    def configurar_treeview(self):
        self.tbl_estado["columns"] = ( # determinando as colunas da tabela
            "id",
            "nome",
            "sigla"
        )
        self.tbl_estado.column( # posicionando as colunas
            "#0",
            width = 0,
            stretch = False
        )
        self.tbl_estado.column(
            "id",
            width = 50
        )
        self.tbl_estado.column(
            "nome",
            width = 50
        )
        self.tbl_estado.column(
            "sigla",
            width = 20
        )

        self.tbl_estado.heading( #titulo das tabelas
            "id",
            text = "ID"
        )
        self.tbl_estado.heading(
            "nome",
            text = "Nome"
        )
        self.tbl_estado.heading(
            "sigla",
            text = "Sigla"
        )


    def configurar_eventos(self): # botoes que terão no nosso sistema
        self.btn_novo.config(
            command = self.controller.new #botão novo
        )
        self.btn_salvar.config(
            command = self.controller.save # botão salvar
        )
        self.btn_alterar.config(
            command = self.controller.update #botão alterar
        )
        self.btn_excluir.config(
            command = self.controller.delete #botão excluir 
        )
        self.tbl_estado.bind(
            "<<TreeviewSelect>>",
            self.controller.selecionar_estado
        )

    def preencher_campos(self, estado):

        self.limpar_campos()
        self.txt_id.config(state = "normal")
        self.txt_id.insert(
            0,
            str(estado.id)
        )
        self.txt_id.config(state = "readonly")
        self.txt_nome.insert(
            0, 
            estado.nome
        )
        self.txt_sigla.insert(
            0,
            estado.sigla
        )

    def limpar_campos(self): #aqui é o campo em que deletamos todos os campos quando clicarmos neste botão 
        self.txt_id.config(state = "normal")
        self.txt_id.delete(0 ,tk.END)
        self.txt_id.config(state = "readonly")
        self.txt_nome.delete(0, tk.END)
        self.txt_sigla.delete(0, tk.END)

    def limpar_treeview(self):
        for item in self.tbl_estado.get_children():
            self.tbl_estado.delete(item)

    def get_id_selecionado(self):
        item = self.tbl_estado.selection()[0]
        return self.tbl_estado.item(item)["values"][0]
    
    def confirmar_exclusao(slef): # mensagem quando o botão DELETAR for clicado
        return messagebox.askyesno(
            "Confirmação",
            "Deseja realmente excluir este estado?"
        )
    

    def ler_dados_estado(self): # quando precisar ocorrer a leitura dos dados vai puxar os campos nome e sigla
        nome = self.txt_nome.get()
        sigla = self.txt_sigla.get()
        return nome, sigla
    
    def exibir_mensagem(self, mensagem, sucesso=True): #mensagem se sucesso ou erro
        if sucesso:
            messagebox.showinfo(
                "Mini ERP",
                mensagem
            )
        else:
            messagebox.showerror(
                "Mini ERP",
                mensagem
            )

    def exibir_estados(self, estados): #quando precisar ser exposto os dados vai puxar os campos id, nome e sigla 
        self.limpar_treeview()
        for estado in estados:
            self.tbl_estados.insert(
                "",
                tk.END,
                values = (
                    estado.id,
                    estado.nome,
                    estado.sigla
                )
            )

    def iniciar(self):  #importante para rodar o codigo 
        self.root.mainloop()