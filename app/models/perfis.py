class Perfis:
    def __init__(self, id, nome, descricao):
        self._id = id
        self._nome = nome 
        self._descricao = descricao 

    @property 
    def id(self):
        return self._id 
    @id.setter 
    def id(self, novo_id):
        self._id = novo_id

    @property 
    def nome(self):
        return self._nome
    @nome.setter 
    def nome(self, novo_nome):
        self._nome = novo_nome

    @property 
    def descricao(self):
        return self._descricao
    @descricao.setter 
    def descricao(self, nova_descricao):
        self._descricao = nova_descricao

    def atualizar_dados(self, novo_nome, nova_descricao):
        self._nome = novo_nome
        self._descricao = nova_descricao
            