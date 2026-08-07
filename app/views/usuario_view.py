from app.models.produto import Produto

import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

class Usuario_View:
    def __init__(self, root, controller):
        self.root = root 
        self.controller = controller
        self._cidades = []
        self.configurar_janela()
        self.criar_componentes()
        self.configurar_treeview()
        self.configurar_eventos()

    def configurar_janela(self):
        self.root.title("CRUD de Usuarios")
        self.root.geometry("800x600")
        self.root.resizable(False, False)

    def criar_componentes(self):
        self.lbl_titulo = tk.Label(
            self.root,
            text = "Cadastro de Usuarios",
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
            text = "Dados do usuarios"
        )
        self.frm_dados.grid(
            row = 1,
            column = 0,
            columnspan=4,
            padx = 10,
            pady = 5,
            sticky = "ew"
        )
        self.lbl_id = tk.Label(
            self.frm_dados,
            text = "ID:"
        )
        self.lbl_id.grid(
            row = 0,
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
            column= 1,
            padx = 5,
            pady = 5,
            sticky = "w"
        )
        self.lbl_nome = tk.Label(
            self.frm_dados,
            text = "Nome:"
        )
        self.lbl_nome.grid(
            row = 1,
            column = 0,
            padx = 5,
            pady = 5,
            sticky = "w"
        )
        self.txt_nome = tk.Entry(
            self.frm_dados,
            width = 40
        )
        self.txt_nome.grid(
            row = 1,
            column = 1,
            padx = 5,
            pady = 5,
            sticky = "w"
        )
        self.lbl_cidades = tk.Label(
            self.frm_dados,
            text = "Cidades:"
        )
        self.lbl_cidades.grid(
            row = 1,
            column = 2,
            padx = 5,
            pady = 5,
            sticky = "w"
        )
        self.cmb_cidades = ttk.Combobox( #campos de opção de resposta 
            self.frm_dados,
            width = 37,
            state = "readonly" #não sera possivel o usuario digitar, somente selecionar a opção
        )
        self.cmb_cidades.grid(
            row = 1,
            column = 3,
            padx = 5,
            pady = 5,
            sticky = "w"
        )
        self.lbl_email = tk.Label(
            self.frm_dados,
            text = "Email:"
        )
        self.lbl_email.grid(
            row = 2,
            column = 0,
            padx = 5,
            pady = 5,
            sticky = "w"
        )
        self.txt_email = tk.Entry(
            self.frm_dados,
            width = 20
        )
        self.txt_email.grid(
            row = 2,
            column = 1,
            padx = 5,
            pady = 5,
            sticky = "w"
        )
        self.lbl_data_nascimento = tk.Label(
            self.frm_dados,
            text = "Data nascimento:"
        )
        self.lbl_data_nascimento.grid(
            row = 2,
            column = 2,
            padx = 5,
            pady = 5,
            sticky = "w"
        )
        self.txt_data_nascimento = tk.Entry(
            self.frm_dados,
            width = 20
        )
        self.txt_data_nascimento.grid(
            row = 2,
            column = 3,
            padx = 5,
            pady = 5,
            sticky = "w"
        )
        self.frm_botoes = tk.Frame(
            self.frm_dados,
            border = 2,
            relief = "groove"
        )
        self.frm_botoes.grid(
            row = 4,
            column = 0,
            padx = 10,
            pady = 5,
            columnspan = 4,
        )
        self.btn_novo = tk.Button(
            self.frm_botoes,
            text = "Novo",
            width = 15
        )
        self.btn_novo.grid(
            row = 0,
            column = 0,
            padx = 5,
            pady = 5
        )
        self.btn_salvar = tk.Button(
            self.frm_botoes,
            text = "Salvar",
            width = 15
        )
        self.btn_salvar.grid(
            row = 0,
            column = 1,
            padx = 5,
            pady = 5
        )
        self.btn_alterar = tk.Button(
            self.frm_botoes,
            text = "Alterar",
            width = 15
        )
        self.btn_alterar.grid(
            row = 0,
            column = 2,
            padx = 5,
            pady = 5
        )
        self.btn_excluir = tk.Button(
            self.frm_botoes,
            text = "Excluir",
            width = 15
        )
        self.btn_excluir.grid(
            row = 0,
            column = 3,
            padx = 5,
            pady = 5
        )
        self.btn_fechar = tk.Button(
            self.frm_botoes,
            text = "Fechar",
            width = 15
        )
        self.btn_fechar.grid(
            row = 0,
            column = 4,
            padx = 5,
            pady = 5
        )
        self.tbl_usuarios = ttk.Treeview(
            self.root,
            height = 10
        )
        self.tbl_usuarios.grid(
            row = 3,
            column = 0,
            columnspan = 4,
            padx = 10,
            pady = 10,
            sticky = "nsew"
        )

    def configurar_treeview(self):
        self.tbl_usuarios["columns"] = (
            "id",
            "nome",
            "email",
            "data_nascimento",
            "cidades"
        )
        self.tbl_usuarios.column(
            "#0",
            width = 0,
            stretch = False
        )
        self.tbl_usuarios.column(
            "id",
            width = 10,
            anchor = "center"
        )
        self.tbl_usuarios.column(
            "nome",
            width = 40
        )
        self.tbl_usuarios.column(
            "email",
            width = 20
        )
        self.tbl_usuarios.column(
            "data_nascimento",
            width = 20
        )
        self.tbl_usuarios.column(
            "cidades",
            width = 40
        )

        self.tbl_usuarios.heading(
            "id",
            text = "ID"
        )
        self.tbl_usuarios.heading(
            "nome",
            text = "Nome"
        )
        self.tbl_usuarios.heading(
            "email",
            text = "Email"
        )
        self.tbl_usuarios.heading(
            "data_nascimento",
            text = "Data de nascimento"
        )
        self.tbl_usuarios.heading(
            "cidades",
            text = "Cidade"
        )

    def configurar_eventos(self):
        self.btn_novo.config(
            command = self.controller.new
        )
        self.btn_salvar.config(
            command = self.controller.save
        )
        self.btn_alterar.config(
            command = self.controller.update
        )
        self.btn_excluir.config(
            command = self.controller.delete
        )
        self.btn_fechar.config(
            command = self.fechar
        )
        self.tbl_produtos.bind(
            "<<TreeviewSelect>>",
            self.controller.selecionar_usuario
        )

    def carregar_cidade(self, cidades):
        self._cidades =cidades
        valores = []
        for cidade in cidades:
            valores.append(
                f"{cidade.id} - {cidade.nome}"
            )
        self.cmb_cidades["values"] = valores
        self.cmb_cidades.set("")

    def preencher_campos(self, usuario):

        self.limpar_campos()
        self.txt_id.config(state = "normal")
        self.txt_id.insert(
            0,
            str(usuario.id)
        )
        self.txt_id.config(state = "readonly")

        self.txt_nome.insert(
            0,
            usuario.nome
        )

        self.txt_email.insert(
            0,
            str(usuario.email)
        )

        self.txt_data_nascimento.insert(
            0,
            str(usuario.data_nascimento)
        )

        for indice, cidade in enumerate(self._cidade):
            if cidade.id == usuario.cidade.id:
                self.cmb_cidades.current(indice)
                break

    def limpar_campos(self):
        self.txt_id.config(state = "normal")
        self.txt_id.delete(0, tk.END)
        self.txt_id.config(state = "readonly")
        self.txt_nome.delete(0, tk.END)
        self.txt_email.delete(0, tk.END)
        self.txt_data_nascimento.delete(0, tk.END)
        self.cmb_cidades.set("")
        self.txt_nome.focus()

    def limpar_treeview(self):
        for item in self.tbl_usuarios.get_children():
            self.tbl_usuarios.delete(item)


    def get_id_selecionado(self):

        item = self.tbl_usuarios.selection()[0]

        return self.tbl_usuarios.item(item)["values"][0]

    def confirmar_exclusao(self):

        return messagebox.askyesno(
            "Confirmação",
            "Deseja realmente excluir este usuario?"
        )

    def ler_dados_usuario(self):
        nome = self.txt_nome.get()
        email = int(self.txt_email.get())
        data_nascimento = float(self.txt_data_nascimento.get())
        indice = self.cmb_cidades.current()
        if indice < 0:
            raise ValueError("Selecione uma cidade.")
        fornecedor = self._cidades[indice]
        return nome, email, data_nascimento, fornecedor

    def exibir_mensagem(self, mensagem, sucesso=True):
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
    def exibir_usuarios(self, usuarios):

        self.limpar_treeview()

        for usuario in usuarios:

            self.tbl_usuarios.insert(
                "",
                tk.END,
                values=(
                    usuario.id,
                    usuario.nome,
                    usuario.email,
                    f"{usuario.data_nascimento:.2f}",
                    usuario.cidades.nome
                )
            )
    def fechar(self):
        self.root.destroy()

    def iniciar(self):
        self.controller.carregar_cidades()
        self.controller.get_all()
        self.root.mainloop()
