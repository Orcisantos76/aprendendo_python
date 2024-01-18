dados_vendas = {}

while True:
    nome = input("Digite seu nome: \n ou sair: ").lower()
    if nome == 'sair':
        print('Até breve.')
        break
    while True:
        vendas = input('Digite as vendas: ')
        if vendas.isdigit():
            venda = int(vendas)
            print(f'{venda} vendas registrada para {nome}')
            break
        else:
            print('Entrada invalida, Digite um numero.')
    if nome not in dados_vendas:
        dados_vendas[nome] = [venda]
    else:
        dados_vendas[nome].append(venda)

for nome, vendas in dados_vendas.items():
    total_vendas = sum(vendas)
    numero_vendas = len(vendas)
    media_vendas = total_vendas/len(vendas)
    print(f'{nome}: Total de vendas = R$ {total_vendas:.2f}\n'
          f'Média de vendas = R$ {media_vendas:.2f}'
          f'Número de vendas: {numero_vendas}')
