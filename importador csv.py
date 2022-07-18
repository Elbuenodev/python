ARQUIVO = 'F:\\curso python Leandro\\aula1\\planilha.csv'
#importa csv

print()
print('------------------------------------------------------------------')
print ('NOME            |   DESCRICAO    |     VALOR   |     QUANTIDADE')
print('------------------------------------------------------------------')

       
arquivo = open (ARQUIVO, 'r')
imprimir = False

for linha in arquivo:
    lista = linha.split(';')
    if imprimir:
        nome = lista[0]
        desc =lista[1]
        valor = float (lista[2])
        quant = int (lista[3])
        print(f'{nome:15} | {desc:15} | R$ {valor:8.2f} | {quant:2}')

    imprimir = True
print('----------------+-----------------+-------------+-----------------')

arquivo.close()
#Só imprime a partir da segunda linha (pula nomes das colunas)


