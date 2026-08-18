from app.models.perfis import Perfis
from app.core.idiomas import Idioma

class Perfis_Controller:
    def __init__(self, dao, view):
        self.dao = dao 
        self.view = view
        self.perfis_selecionados = None 

    def new (self):
        self.view.limpar_campos()

    def save(self):
        try:
            nome, descricao = self.view.ler_dados_perfis()
            perfis = Perfis(None, nome, descricao)
            self.dao.save(perfis)
            self.get_all()
            self.view.exibir_mensagem(Idioma.t("perfis.perfis_cadastrados"))
        except ValueError as e:
            self.view.exibir_mensagem(f"{Idioma.t('comum.erro_prefixo')}{Idioma.t(str(e))}", False)


    def get_all(self):
        perfis = self.dao.get_all()
        self.view.exibir_perfis(perfis)

    def selecionar_perfis(self, event):
        try:
            id_perfis = self.view.get_id_selecionado()
            self.perfis_selecionados = self.dao.get_by_id(
                id_perfis
            )
            self.view.preencher_campos(
                self.perfis_selecionados
            )
        except IndexError:
            try:
                if self.perfis_selecionadosis is None:
                    self.view.exibir_mensagem(Idioma.t("perfis.selecione_perfil"), False)
                    return 
                nome,descricao = self.view.ler_dados_perfis()
                self.perfis_selecionados.atualizar_dados(nome, descricao)
                self.dao.update(self.perfis_selecionados)
                self.get_all()
                self.view.exibir_mensagem(Idioma.t("perfis.perfil_atualizado"))
            except ValueError as e:
                self.view.exibir_mensagem(f"{Idioma.t('comum.erro_prefixo')}{Idioma.t(str(e))}", False)


    def delete(self):
        if self.perfis_selecionados is None:
            self.view.exibir_mensagem(Idioma.t("perfis.selecione_perfil"), False )
            return 
        if not self.view.confirmar_exclusao():
            return 
        try:
            sucesso = self.dao.delete(self.perfis_selecionados.id)
            if sucesso:
                self.perfis_selecionados = None
                self.view.limpar_campos()
                self.get_all()
                self.view.exibir_mensagem(Idioma.t("perfis.perfil_excluido"))
            else:
                self.view.exibir_mensagem(Idioma.t("perfis.nao_encontrado"), False)
        except Exception as e:
            self.view.exibir_mensagem(Idioma.t("perfis.problema_exclusao"), False)