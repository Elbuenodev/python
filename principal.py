from models import Produto
from config import db

db.drop_all()

# cria todas as tabelas do banco de dados
db.create_all()

# cria uma entidade

tv = Produto(descricao='Tv Samsung', preco=1999, quantidade=10)

# sem id ainda
print(tv)

# salva no banco
db.session.add(tv)  # insert into Produto values...
db.session.commit()

# agora com id
print(tv)

# alterando a descrição
tv.descricao = 'TV Lg 50'
db.session.add(tv)
db.session.commit()

# cria outra entidade
fogao = Produto(descricao='Fogâo 6 bocas', preco=2500, quantidade=5)
db.session.add(fogao)
db.session.commit()

# consulta todos os produtos cadstrados (SELECT*FROM produto)
produtos = Produto.query.all()
for p in produtos:
    print(p)

    # BUSCANDO UM UNICO ITEM
porId = Produto.query.filter_by(id=1).first()
print('busca por id', porId)

# busca por descrição
porDescricao = Produto.query.filter_by(descricao='TV Lg 50').all()
print('busca por Descrição: ', porDescricao)

# apagar
produto = Produto.query.filter_by(id=2).first()
if produto:
    db.session.delete(produto)
    db.session.commit()
    print('apagou')
else:
    print('não apagou')
