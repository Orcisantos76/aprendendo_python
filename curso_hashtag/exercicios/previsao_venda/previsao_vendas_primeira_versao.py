previsao_vendas = {}


while True:
    continuar = input('Deseja continuar: Sim/Não: ')
    continuar = continuar.lower()
    print(continuar, 'sair')
    if continuar == 'não' or continuar == 'nao':
        print('Até breve')
        break
    try:
        produto = str(input('Digite o produto: '))
    except ValueError:
        print('Produto invalido')
    try:
        venda = float(input('Vendas do mes atual: '))
        taxa_de_crescimento = float(input('Digite a taxa de crecimento: '))
    except ValueError:
        print('Por favor, digite um número inteiro válido.')
        continue

    aumento = (taxa_de_crescimento*venda)/100
    previsao_vendas = venda + aumento
    previsao_vendas = int(previsao_vendas)
    print(produto, 'nome\n', venda, 'vendas\n',
          'previsao de vendas, conforme taxa de crescimento prevista:  ', previsao_vendas)

print(type(previsao_vendas))
