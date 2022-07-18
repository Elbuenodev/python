#ler_csv.py
from produto import Produto
import csv

ARQUIVO = 'F:\\curso python Leandro\\aula1\\planilha.csv'
primeira = True
lista_produtos = []

with open(ARQUIVO, encoding='utf-8') as arq:
    tabela = csv.reader(arq)
    for linha in tabela:
        if primeira:
            primeira = False #inverte a váriavel para não imprimir o cabeçalho e continua executando o código.
            continue
        lista = linha [0].split(';')
        nome = lista[0]
        desc = lista[1]
        valor = lista[2]
        quant = lista[3]
        p = Produto(nome, desc, valor, quant)
        lista_produtos.append(p)
        
for item in lista_produtos:
    print(p)

