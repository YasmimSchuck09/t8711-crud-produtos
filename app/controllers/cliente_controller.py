import os
from app.models.produto import Produto

class Cliente_Controller:
    def __init__(self, dao, cidade_dao, view):
        self.dao = dao
        self.cidade_dao = cidade_dao
        self.view = view
        self.cliente_selecionado = None

    def new(self):
        self.view.limpar_campos()

    def carregar_cidades(self):
        cidades = self.cidade_dao.get_all()
        self.view.carregar_cidades(cidades)

    def save(self):
        try:
            nome, data_nascimento, limite_credito, cidade = self.view.ler_dados_clientes()
            cliente = Produto(None, nome, data_nascimento, limite_credito, cidade)
            self.dao.save(cliente)
            self.get_all()
            self.view.exibir_mensagem("Cliente cadastrado com sucesso!")
        except ValueError as e:
            self.view.exibir_mensagem(f"Erro: {str(e)}", False)

    def get_all(self):
        cliente = self.dao.get_all()
        self.view.exibir_cliente(cliente)

    def selecionar_cliente(self, event):
        try:
            id_cliente= self.view.get_id_selecionado()
            self.cliente_selecionado = self.dao.get_by_id(
                id_cliente
            )
            self.view.preencher_campos(
                self.cliente_selecionado
            )
        except IndexError:
            pass

    def update(self):
        try:
            if self.cliente_selecionado is None:
                self.view.exibir_mensagem("Selecione um cliente na lista.", False)
                return
            nome, data_nascimento, limite_credito, cidade = self.view.ler_dados_clientes()
            self.produto_selecionado.atualizar_dados(nome, data_nascimento, limite_credito, cidade)
            self.dao.update(self.cliente_selecionado)
            self.get_all()
            self.view.exibir_mensagem("Cliente atualizado com sucesso!")
        except ValueError as e:
            self.view.exibir_mensagem(f"Erro: {str(e)}", False)

    def delete(self):
        if self.cliente_selecionado is None:
            self.view.exibir_mensagem("Selecione um cliente na lista.", False)
            return
        if not self.view.confirmar_exclusao():
            return
        try:
            sucesso = self.dao.delete(self.cliente_selecionado.id)
            if sucesso:
                self.cliente_selecionado = None
                self.view.limpar_campos()
                self.get_all()
                self.view.exibir_mensagem("Cliente excluído com sucesso!")
            else:
                self.view.exibir_mensagem("Cliente não encontrado.", False)
        except Exception as e:
            self.view.exibir_mensagem("Problemas ao excluir cliente", False)

    def inicializar_sistema(self):
        while True:
            os.system('cls' if os.name == 'nt' else 'clear')
            opcao = self.view.renderizar_menu()
            if opcao == 0:
                break
            elif opcao == 1:
                self.save()

            elif opcao == 2:
                self.get_all()

            elif opcao == 3:
                self.update()

            elif opcao == 4:
                self.delete()

            else:
                self.view.exibir_mensagem("Opção inválida. Tente novamente.", False)
