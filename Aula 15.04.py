from datetime import datetime

busca = input('Qual nome vc busca: ')

with open('dados.csv', 'r') as arquivo:
    next(arquivo)
    lista_linhas = arquivo.readlines()
    for linha in lista_linhas:
        nome, matricula, data_nascimento = linha.strip('\n').split(',')
        if (nome == busca):
            data_nascimento = datetime.strip(data_nascimento, '%d/%m/%Y')
            print(nome, '>', data_nascimento)




