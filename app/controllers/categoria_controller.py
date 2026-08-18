from app.models.categoria import Categoria
from app.core.idiomas import Idioma

class Categoria_Controller:
    def __init__(self, dao, view):
        self.dao = dao
        self.view = view
        self.categoria_selecionada = None

    def new(self):
        self.view.limpar_campos()

    def save(self):
        try:
            nome = self.view.ler_dados_categoria()
            categoria = Categoria(
                None,
                nome
            )
            self.dao.save(categoria)
            self.get_all()
            self.view.exibir_mensagem(Idioma.t("categoria.cadastro_sucesso"))
        except ValueError as e:
            self.view.exibir_mensagem(f"{Idioma.t('comum.erro_prefixo')}{Idioma.t(str(e))}", False)

    def get_all(self):
        categorias = self.dao.get_all()
        self.view.exibir_categorias(categorias)

    def selecionar_categoria(self, event):
        try:
            id_categoria = self.view.get_id_selecionado()
            self.categoria_selecionada = self.dao.get_by_id(
                id_categoria
            )
            self.view.preencher_campos(
                self.categoria_selecionada
            )

        except IndexError:
            pass

    def update(self):
        try:
            if self.categoria_selecionada is None:
                self.view.exibir_mensagem(Idioma.t("categoria.selecionar_categoria"), False)
                return
            nome = self.view.ler_dados_categoria()
            self.categoria_selecionada.atualizar_dados(nome)
            self.dao.update(self.categoria_selecionada)
            self.get_all()
            self.view.exibir_mensagem(Idioma.t("categoria.atualizacao_sucesso"))
        except ValueError as e:
            self.view.exibir_mensagem(f"{Idioma.t('comum.erro_prefixo')}{Idioma.t(str(e))}", False)

    def delete(self):
        if self.categoria_selecionada is None:
            self.view.exibir_mensagem(Idioma.t("categoria.selecionar_categoria"), False)
            return
        if not self.view.confirmar_exclusao():
            return
        try:
            sucesso = self.dao.delete(self.categoria_selecionada.id)
            if sucesso:
                self.categoria_selecionada = None
                self.view.limpar_campos()
                self.get_all()
                self.view.exibir_mensagem(Idioma.t("categoria.exclusao_sucesso"))
            else:
                self.view.exibir_mensagem(Idioma.t("categoria.nao_encontrada"), False)
        except Exception as e:
            self.view.exibir_mensagem(Idioma.t("categoria.problemas_exclusao"), False)
