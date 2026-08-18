CREATE TABLE fornecedor_perfis (
id_fornecedor int not null,
id_perfis int not null,
primary key (id_fornecedor, id_perfis),

CONSTRAINT fk_fornecedor_fornecedor_perfis
foreign key (id_fornecedor)
references fornecedore(id),

CONSTRAINT fk_perfis_fornecedor_perfis
foreign key (id_perfis)
references perfis(id)
);