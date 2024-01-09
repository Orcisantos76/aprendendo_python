# Relatório de vendas¶
# Primeira versão do relatório de vendas
# Escreva um programa que calcula o total e a média de vendas para cada vendedor em uma empresa. O usuário deve digitar o nome do vendedor e suas vendas, e o programa deve manter o controle do total e da média de vendas para cada vendedor.

# Estruture seu programa da seguinte forma:

# Crie um dicionário vazio para armazenar os dados de vendas.
# Crie um loop infinito que solicite ao usuário o nome do vendedor e suas vendas.
# Dentro do loop, use uma declaração if para verificar se o usuário digitou 'sair'.
# Se o usuário digitar 'sair', encerre o loop usando break.
# Se o usuário digitar qualquer outra coisa, use as entradas para calcular o total e a média de vendas para o vendedor e adicione-os ao dicionário.
# Depois que o loop for encerrado, use um loop for para iterar sobre o dicionário e mostrar o total e a média de vendas para cada vendedor.

dados_vendas = {}


def validar_nome():
    '''Recebe nome do usuario se digitar sair encerra'''
    while True:
        nome = input('Digite seu nome, ou "sair" para sair: ').lower()
        if nome.isalpha() and nome != 'sair':
            return nome
        elif nome == 'sair':
            return 'Encerrado pelo usuário'
        else:
            print('O nome deve ser um nome')


nome = validar_nome()
print(nome)
