from app.core.idiomas import Idioma
from app.models.fornecedor import Fornecedor

class Fornecedor_Controller:
    def __init__(self,dao,categoria_dao,fornecedor_categoria_dao,perfil_dao,fornecedor_perfis_dao,view):
        self.dao = dao
        self.categoria_dao = categoria_dao
        self.fornecedor_categoria_dao = fornecedor_categoria_dao
        self.view = view
        self.perfil_dao = perfil_dao
        self.fornecedor_perfis_dao = fornecedor_perfis_dao
        self.fornecedor_selecionado = None


    def new(self):
        self.view.limpar_campos()

    def save(self):
        try:
            razao_social, nome_fantasia, cnpj, sla_atendimento = self.view.ler_dados_fornecedor()
            fornecedor = Fornecedor(
                    None,
                    razao_social, 
                    nome_fantasia, 
                    cnpj, 
                    sla_atendimento
                )
            self.dao.save(fornecedor)
            self.get_all()
            self.view.exibir_mensagem(Idioma.t( "fornecedor.cadastro_sucesso"))
        except ValueError:
            self.view.exibir_mensagem(Idioma.t("fornecedor.erro_entrada"), False)
        
    def get_all(self):
        fornecedores = self.dao.get_all()
        self.view.exibir_fornecedores(fornecedores)

    def selecionar_fornecedor(self, event):
        try:
            id_fornecedor = self.view.get_id_selecionado()
            self.fornecedor_selecionado = self.dao.get_by_id(
                id_fornecedor
            )
            self.view.preencher_campos(
                self.fornecedor_selecionado
            )

        except IndexError:
            pass

    def update(self):
        try:
            if self.fornecedor_selecionado is None:
                self.view.exibir_mensagem(Idioma.t("fornecedor.selecione_na lista"), False)
                return

            razao_social, nome_fantasia, cnpj, sla_atendimento = self.view.ler_dados_fornecedor()

            self.fornecedor_selecionado.atualizar_dados(
                razao_social,
                nome_fantasia,
                cnpj,
                sla_atendimento
            )

            self.dao.update(self.fornecedor_selecionado)
            self.get_all()
            self.view.exibir_mensagem(Idioma.t("fornecedor.atualizacao_sucesso"))

        except ValueError as e:
            self.view.exibir_mensagem(f"{Idioma.t('comum.erro_prefixo')}{Idioma.t(str(e))}", False)

    def delete(self):
        if self.fornecedor_selecionado is None:
            self.view.exibir_mensagem(Idioma.t("fornecedor.selecione_na lista"), False)
            return

        if not self.view.confirmar_exclusao():
            return

        try:
            sucesso = self.dao.delete(self.fornecedor_selecionado.id)

            if sucesso:
                self.fornecedor_selecionado = None
                self.view.limpar_campos()
                self.get_all()
                self.view.exibir_mensagem(Idioma.t("fornecedor.exclusao_sucesso"))
            else:
                self.view.exibir_mensagem(Idioma.t("fornecedor.nao_encontrado"), False)

        except Exception as e:
            self.view.exibir_mensagem(Idioma.t("fornecedor.problema_exclusao"), False)

    def abrir_categorias(self):
        if self.fornecedor_selecionado is None:
            self.view.exibir_mensagem(Idioma.t("fornecedor.selecione_na lista"), False)
            return

        categorias_disponiveis = self.categoria_dao.get_all()

        if not categorias_disponiveis:
            self.view.exibir_mensagem(
                (Idioma.t("fornecedor.cadastre_categorias")),
                False
            )
            return

        self.fornecedor_selecionado.categorias = self.fornecedor_categoria_dao.get_categorias_por_fornecedor(
            self.fornecedor_selecionado
        )

        self.view.abrir_categorias(
            self.fornecedor_selecionado,
            categorias_disponiveis
        )

    def abrir_perfis(self):
        if self.fornecedor_selecionado is None:
            self.view.exibir_mensagem(Idioma.t("fornecedor.selecione_na lista"), False)
            return

        perfis_disponiveis = self.perfil_dao.get_all()

        if not perfis_disponiveis:
            self.view.exibir_mensagem(
                (Idioma.t("fornecedor.cadastre_perfis_antes")),
                False
            )
            return
        self.fornecedor_selecionado.perfis = self.fornecedor_perfis_dao.get_perfis_por_fornecedor(
            self.fornecedor_selecionado
        )

        self.view.abrir_perfis(
            self.fornecedor_selecionado,
            perfis_disponiveis
        )

    def salvar_categorias(self, view_categorias, fornecedor, categorias_selecionadas):
        try:
            self.fornecedor_categoria_dao.substituir_categorias_do_fornecedor(
                fornecedor,
                categorias_selecionadas
            )
            fornecedor.categorias = self.fornecedor_categoria_dao.get_categorias_por_fornecedor(
                fornecedor
            )
            view_categorias.exibir_mensagem(
                (Idioma.t("fornecedor.atualizacao_categoria"))
            )
            view_categorias.fechar()
        except Exception as e:
            view_categorias.exibir_mensagem(
                (Idioma.t("fornecedor.erro_salvar_cat")),
                False
            )
    def salvar_perfis(self, view_perfis, fornecedor, perfis_selecionadas):
        try:
            self.fornecedor_perfis_dao.substituir_perfis_do_fornecedor(
                fornecedor,
                perfis_selecionadas
            )
            fornecedor.perfis = self.fornecedor_perfis_dao.get_perfis_por_fornecedor(
                fornecedor
            )
            view_perfis.exibir_mensagem(
                (Idioma.t("fornecedor.perfil_forne_atualizado"))
            )
            view_perfis.fechar()
        except Exception as e:
            view_perfis.exibir_mensagem(
                (Idioma.t("fornecedor.erro_salvar_cat")),
                False
            )