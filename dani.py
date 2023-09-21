import csv

# Abra o arquivo CSV em modo de leitura
with open('dados.csv', mode='r') as file:
    # Crie um leitor CSV
    reader = csv.reader(file)
    
    # Itere pelas linhas do arquivo
    for row in reader:
        # 'row' é uma lista com os valores das colunas em cada linha
        print(row)

        