'''

Estruture seu programa da seguinte forma:

Crie um dicionário vazio para armazenar os dados de vendas.
Crie um loop infinito que solicite ao usuário o nome do vendedor e suas vendas.
Dentro do loop, use uma declaração if para verificar se o usuário digitou 'sair'.
Se o usuário digitar 'sair', encerre o loop usando break.
Se o usuário digitar qualquer outra coisa, use as entradas para calcular o total e a média de vendas para o vendedor e adicione-os ao dicionário.
Depois que o loop for encerrado, use um loop for para iterar sobre o dicionário e mostrar o total e a média de vendas para cada vendedor.
'''

dados_vendas = {}
# todo dicionário recebe uma chave e um valor {'orci': 47} chave orci, valor 47
while True:
    nome = input('Digite o nome do vendedor: \n ou "sair" para sair: ').lower()
    if nome == 'sair':
        print('Até mais')
        break
    vendas = float(input('Digite as vendas: '))
    if nome not in dados_vendas:
        dados_vendas[nome] = [vendas]
        print(dados_vendas[nome])
        print(dados_vendas)
    else:
        dados_vendas[nome].append(vendas)
        print(f'Vendas sera inserida ao usuario {dados_vendas}, \n'
              # dicionario[chave = elemento][indice em value]
              f'{dados_vendas[nome][-1]}, ultimas vendas inseridas')
for nome, vendas in dados_vendas.items():
    total_vendas = sum(vendas)
    media_vendas = total_vendas/len(vendas)
    print(f'{nome}: Total de vendas = R$ {total_vendas:.2f}.'
          f'Média vendas = R$ {media_vendas:.2f}')
