import os
from app.models.cidade import Cidade


class Cidade_Controller:

    def __init__(self, dao, estado_dao, view):
        self.dao = dao
        self.estado_dao = estado_dao
        self.view = view

    def save(self):
        try:

            estados = self.estado_dao.get_all()
            if not estados:
                self.view.exibir_mensagem(
                    "Cadastre um estado antes de cadastrar cidades.",
                    False
                )
                return
            self.view.exibir_estados(estados)
            id_estado = int(self.view.ler_estado())
            estado = self.estado_dao.get_by_id(id_estado)
            if estado is None:

                self.view.exibir_mensagem(
                    "Estado não encontrado.",
                    False
                )
                return

            nome = self.view.ler_dados_cidade()
            cidade = Cidade(
                None,
                nome,
                estado
            )
            self.dao.save(cidade)
            self.view.exibir_mensagem(
                "Cidade cadastrada com sucesso!"
            )
        except ValueError:
            self.view.exibir_mensagem(
                "Entrada inválida.",
                False
            )
        except KeyboardInterrupt:
            self.view.exibir_mensagem(
                "Operação cancelada.",
                False
            )

    def get_all(self):
        cidades = self.dao.get_all()
        self.view.exibir_cidades(cidades)
        self.view.aguardar_entrada()
    def update(self):
        try:
            cidades = self.dao.get_all()
            self.view.exibir_cidades(cidades)
            id_cidade = int(self.view.ler_id())
            cidade = self.dao.get_by_id(id_cidade)
            if cidade is None:
                self.view.exibir_mensagem(
                    "Cidade não encontrada.",
                    False
                )
                return
            estados = self.estado_dao.get_all()
            self.view.exibir_estados(estados)
            id_estado = self.view.ler_estado(
                cidade.estado.id
            )
            estado = self.estado_dao.get_by_id(
                int(id_estado)
            )

            if estado is None:
                self.view.exibir_mensagem(
                    "Estado não encontrado.",
                    False
                )
                return

            nome = self.view.ler_dados_cidade(
                cidade
            )
            cidade.atualizar_dados(
                nome,
                estado
            )
            self.dao.update(cidade)
            self.view.exibir_mensagem(
                "Cidade atualizada com sucesso!"
            )
        except ValueError as e:
            self.view.exibir_mensagem(
                f"Erro: {str(e)}",
                False
            )
    def delete(self):
        try:
            cidades = self.dao.get_all()
            self.view.exibir_cidades(cidades)
            id_cidade = int(self.view.ler_id())
            sucesso = self.dao.delete(id_cidade)
            if sucesso:
                self.view.exibir_mensagem(
                    "Cidade excluída com sucesso!"
                )
            else:
                self.view.exibir_mensagem(
                    "Cidade não encontrada.",
                    False
                )
        except ValueError:

            self.view.exibir_mensagem(
                "ID inválido.",
                False
            )
    def inicializar_sistema(self):

        while True:
            os.system("cls" if os.name == "nt" else "clear")
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

                self.view.exibir_mensagem(
                    "Opção inválida.",
                    False
                )