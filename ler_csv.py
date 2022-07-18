#ler_csv.py



ARQUIVO = 'F:\\curso python Leandro\\aula1\\planilha.csv'
import csv

tabela = csv.reader(open(ARQUIVO))


with open(ARQUIVO, encoding='utf-8') as arq:
    tabela = csv.reader(arq)
    for linha in tabela:
        print(linha)

