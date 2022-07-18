#produto.py


#classe Produto
class Produto:
    #contrutor da classe
    def __init__(self, nome, descricao, valor,quantidade):
        self.nome = nome
        self.descricao = descricao
        self.valor = valor
        self.quantidade = quantidade

    #função builtin (sobrescrita de função)
    def __str__ (self):
        return f'Nome: {self.nome:10} \tDesc:{self.descricao:10} \tR$ {self.valor:10} \tQuantidade:{self.quantidade:10}'
    


