dados_vendas = {}

while True:
    nome = input('Digite seu nome: \n Sair para sair: ').lower()
    if nome == 'sair':
        print('Até breve')
        break
    while True:
        venda = input('Digite as vendas: ')
        venda = int(venda)
        break

    if nome not in dados_vendas:
        dados_vendas[nome] = {'total_vendas': venda, 'quantidade_vendas': 1}
    else:
        dados_vendas[nome]['total_vendas'] += venda
        dados_vendas[nome]['quantidade_vendas'] += 1

for nome, dados in dados_vendas.items():
    total_vendas = dados['total_vendas']
    media_vendas = total_vendas/dados['quantidade_vendas']
    print(f'{nome}: Total de vendas = R${total_vendas:.2f}\n'
          f'Média vendas =R$ {media_vendas:.2f}')
