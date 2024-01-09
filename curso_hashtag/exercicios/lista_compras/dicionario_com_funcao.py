
'''
# Exercícios de fixação

A seguir, você encontrará alguns exercícios para fixar os conceitos aprendidos no curso até agora. Os exercícios estão divididos por exemplos práticos da vida real:

- lista de compras
- previsão de vendas
- relatório de vendas
- segmentação de clientes
- analisador de texto

Para cada assunto, você encontrará ao menos um exercício. Nos casos onde há mais de um exercício para o mesmo assunto, você será convidado a resolver o mesmo problema de formas diferentes. Isso é proposital, pois o objetivo é que você pratique o que aprendeu e, ao mesmo tempo, aprenda novas formas de resolver um mesmo problema. Por exemplo, usando diferentes estruturas de dados, ou diferentes formas de iterar sobre uma estrutura de dados, ou, ainda, utilizando funções.

Tente resolver os exercícios sozinho. Se tiver dificuldades, consulte o material do curso e, se ainda assim não conseguir resolver, consulte a solução.

Lista de compras

Terceira versão da lista de compras'''

# Mantenha o programa da lista de compras com dicionário, mas agora use funções para organizar o código. Crie funções para cada uma das opções do menu: `adicionar_item`, `remover_item` e `ver_lista`. Crie também uma função para mostrar o menu. O programa deve continuar funcionando da mesma forma, mas agora o código deve estar organizado em funções.
#

lista_compras_dicionario_funcao = {'maça': 5, 'banana': 6, 'caju': 9}


def opcao_menu():
    '''
    Solicita ao usuario que escolha uma opção do menu.
    retorna:
        str: Opção escolhida pelo usuário
    '''
    opcao = input('Escolha uma opção:\n'
                  '1 Adicionar item\n'
                  '2 Remover item\n'
                  '3 Ver lista\n'
                  '4 Sair ')
    return opcao


def item_na_lista(item):
    '''
    Verifica se um item está na lista de compras.

    Input:
        item (str): Nome do item a ser verificado.
    Retorna:
        bool: True se o item estiver na lista, False caso contrário.
    '''
    return item in lista_compras_dicionario_funcao


def add_item():
    """
    Adiciona um item à lista de compras.

    Input:
        Nome do item (str): Nome do item a ser adicionado à lista.
        Quantidade (int): Quantidade do item a ser adicionada à lista.
    """
    item = input('Nome do item: ')
    item = item.lower()
    quantidade = int(input(f'Quantidade de {item}: '))

    if not item_na_lista(item):
        lista_compras_dicionario_funcao[item] = quantidade
    else:
        print(f'{item} Já está na lista')


def remove_item():
    """
    Remove um item da lista de compras.

    Input:
        Nome do item (str): Nome do item a ser removido da lista.
    """
    item = input('Nome do item a ser removido: ')
    item = item.lower()
    if item_na_lista(item):
        del lista_compras_dicionario_funcao[item]
        print(f'{item} removido da lista.')
    else:
        print('Item nao encontrado na lista')


def visualizar():
    '''Exibe a lista de compras atual.'''
    print('Lista de compras: ')
    for item, quantidade in lista_compras_dicionario_funcao.items():
        print(f'{item}: {quantidade}')


while True:
    opcao = opcao_menu()

    if opcao == '1':
        add_item()
    elif opcao == '2':
        remove_item()
    elif opcao == '3':
        visualizar()
    elif opcao == '4':
        print('Até breve')
        break
    else:
        print('Opção invalida. Escolha uma opção valida.')


# solução


# ## Previsão de vendas

# ### Primeira versão da previsão de vendas

# Escreva um programa que preveja as vendas totais para cada produto em uma empresa.
# O usuário deve digitar o nome do produto, as vendas do mês atual e a taxa de crescimento,
# e o programa deve calcular as vendas previstas para o próximo mês.
#
# Estruture seu programa da seguinte forma:
#
# 1. Crie um dicionário vazio para armazenar as previsões de vendas.
# 2. Crie um loop infinito que solicite ao usuário o nome do produto, as vendas do mês atual e a taxa de crescimento.
# 3. Dentro do loop, use uma declaração if para verificar se o usuário digitou 'sair'.
# 4. Se o usuário digitar 'sair', encerre o loop usando break.
# 5. Se o usuário digitar qualquer outra coisa, use as entradas para calcular as vendas previstas e adicione-as ao dicionário.
# 6. Depois que o loop for encerrado, use um loop for para iterar sobre o dicionário e mostrar as previsões de vendas para cada produto.
#
# Exemplo de saída:
#
# ```
# Digite o nome do produto (ou 'sair' para sair): iphone
# Digite as vendas do mês atual: 10000
# Digite a taxa de crescimento (%): 10
# Digite o nome do produto (ou 'sair' para sair): capinha para iphone
# Digite as vendas do mês atual: 200
# Digite a taxa de crescimento (%): 20
# Digite o nome do produto (ou 'sair' para sair): sair
# iphone: Previsão de vendas do próximo mês = R$ 11000.00
# capinha para iphone: Previsão de vendas do próximo mês = R$ 240.00
# ```
#

# In[ ]:


# solução


# ### Segunda versão da previsão de vendas
#

# Mantenha a mesma funcionalidade do programa anterior, mas agora valide a entrada do usuário.
# Se o usuário digitar um valor inválido para vendas ou taxa de crescimento, mostre a mensagem
# "Entrada inválida. Por favor, digite um número para vendas e taxa de crescimento." e peça
# para o usuário digitar novamente. Tal validação deve ser feita usando try/except.
#

# In[ ]:


# solução


# ## Relatório de vendas

# ### Primeira versão do relatório de vendas

# Escreva um programa que calcula o total e a média de vendas para cada vendedor em uma empresa.
# O usuário deve digitar o nome do vendedor e suas vendas, e o programa deve manter o controle
# do total e da média de vendas para cada vendedor.
#
# Estruture seu programa da seguinte forma:
#
# 1. Crie um dicionário vazio para armazenar os dados de vendas.
# 2. Crie um loop infinito que solicite ao usuário o nome do vendedor e suas vendas.
# 3. Dentro do loop, use uma declaração if para verificar se o usuário digitou 'sair'.
# 4. Se o usuário digitar 'sair', encerre o loop usando break.
# 5. Se o usuário digitar qualquer outra coisa, use as entradas para calcular o total e a média de vendas para o vendedor e adicione-os ao dicionário.
# 6. Depois que o loop for encerrado, use um loop for para iterar sobre o dicionário e mostrar o total e a média de vendas para cada vendedor.
#
# Exemplo de saída:
#
# ```
# Digite o nome do vendedor (ou 'sair' para sair): João
# Digite as vendas: 100
# Digite o nome do vendedor (ou 'sair' para sair): Maria
# Digite as vendas: 200
# Digite o nome do vendedor (ou 'sair' para sair): João
# Digite as vendas: 300
# Digite o nome do vendedor (ou 'sair' para sair): sair
# João: Total de vendas = R$ 400.0, Média de vendas = R$ 200.0
# Maria: Total de vendas = R$ 200.0, Média de vendas = R$ 200.0
# ```
#
# Dica: use o método sum() para calcular o total de vendas e o método len() para calcular o número de vendas.
#

# In[ ]:


# solução


# ### Segunda versão do relatório de vendas
#

# Mantenha a mesma funcionalidade do programa anterior, mas agora valide a entrada do usuário.
# Se o usuário digitar um valor inválido para vendas, mostre a mensagem
# "Entrada inválida. Por favor, digite um número para vendas." e peça para o usuário digitar
# novamente. Tal validação deve ser feita usando try/except.
#
# Além disso, ao invés de armazenar cada venda em uma lista para cada vendedor, armazene
# o total de vendas e a quantidade de vendas em um dicionário. Por exemplo, se o usuário
# digitar "João" e "1000" para vendas, o dicionário deve ficar assim:
#
# ```python
# {'João': {'total_vendas': 1000, 'quantidade_vendas': 1}}
# ```
#
# Se, após, o usuário digitar "João" e "2000" para vendas, o dicionário deve ficar assim:
#
# ```python
# {'João': {'total_vendas': 3000, 'quantidade_vendas': 2}}
# ```
#
# Perceba como o total de vendas de João aumentou em 2000, assim como a quantidade aumentou em uma unidade.
#
# Ao final, mostre o total de vendas e a média de vendas de cada vendedor.
#
# Exemplo de saída:
#
# ```
# Digite o nome do vendedor (ou 'sair' para sair): João
# Digite as vendas: 1000
# Digite o nome do vendedor (ou 'sair' para sair): Maria
# Digite as vendas: 2000
# Digite o nome do vendedor (ou 'sair' para sair): João
# Digite as vendas: 2000
# Digite o nome do vendedor (ou 'sair' para sair): Maria
# Digite as vendas: 3000
# Digite o nome do vendedor (ou 'sair' para sair): sair
# João: Total de vendas = R$ 3000.00, Média de vendas = R$ 1500.00
# Maria: Total de vendas = R$ 5000.00, Média de vendas = R$ 2500.00
# ```
#

# In[ ]:


# solução


# ### Terceira versão do relatório de vendas

#  Mantenha a funcionalidade do programa, mas agora use funções para organizar o código. Crie funções para cada uma das operações: `solicitar_nome_vendedor`, `solicitar_vendas` e `atualizar_dados` e `print_dados`. O programa deve continuar funcionando da mesma forma, mas agora o código deve estar organizado em funções.

# In[ ]:


# solução


# ## Segmentação de clientes

# ### Primeira versão da segmentação de clientes

# Escreva um programa que segmenta clientes com base em suas compras totais.
# O usuário deve digitar o nome do cliente e suas compras totais, e o programa
# deve atribuir cada cliente a um segmento: 'Bronze' para compras de até R\\$ 1000,
# 'Prata' para compras de até R\\$ 5000 e 'Ouro' para compras acima de R\\$ 5000.
#
# Estruture seu programa da seguinte forma:
#
# 1. Crie um dicionário vazio para armazenar os clientes e seus segmentos.
# 2. Crie um loop infinito que solicite ao usuário o nome do cliente e suas compras totais.
# 3. Dentro do loop, use uma declaração if para atribuir o segmento apropriado ao cliente.
# 4. Se o usuário digitar 'sair' para o nome do cliente, encerre o loop usando break.
# 5. Fora do loop, use um loop for para imprimir o nome e o segmento de cada cliente.
#
# Exemplo de saída:
#
# ```
# Digite o nome do cliente (ou 'sair' para sair): João
# Digite o total de compras: 100
# Digite o nome do cliente (ou 'sair' para sair): Maria
# Digite o total de compras: 2000
# Digite o nome do cliente (ou 'sair' para sair): José
# Digite o total de compras: 6000
# Digite o nome do cliente (ou 'sair' para sair): sair
# João: Segmento do Cliente = Bronze
# Maria: Segmento do Cliente = Prata
# José: Segmento do Cliente = Ouro
# ```
#

# In[ ]:


# solução


# ### Segunda versão da segmentação de clientes
#

#
# Mantenha a mesma funcionalidade do programa anterior, mas agora valide a entrada do usuário.
# Se o usuário digitar um valor inválido para compras, mostre a mensagem
# "Entrada inválida. Por favor, digite um número para compras." e peça para o usuário digitar
# novamente. Tal validação deve ser feita usando try/except.
#
# Além disso, ao invés de deixar os limites de compras fixos no programa, armazene-os em uma
# lista de tuplas. Por exemplo:
#
# ```python
# segmentos = [(1000, 'Bronze'), (5000, 'Prata'), (float('inf'), 'Ouro')]
# ```
#
# Assim, outros segmentos podem ser adicionados facilmente. O primeiro elemento da tupla é o
# limite de compras e o segundo é o nome do segmento. O último elemento da lista é uma tupla
# com limite `float('inf')`, que representa o segmento Ouro. Isso significa que, se o valor de
# compras for maior que todos os limites, o segmento será Ouro.
#
# Depois, percorra essa lista e, para cada tupla, verifique se o valor de compras é menor ou igual
# ao limite. Se for, armazene o segmento em um dicionário. Por exemplo, se o usuário digitar
# "João" e "500" para compras, o dicionário deve ficar assim:
# `{'João': 'Bronze'}`
#

# In[ ]:


# solução


# ### Terceira versão da segmentação de clientes

# Mantenha a funcionalidade do programa, mas agora use funções para organizar o código. Crie funções para cada uma das operações: `solicitar_nome_cliente`, `solicitar_total_compras` e `atribuir_segmento` e `print_segmento_por_cliente`. O programa deve continuar funcionando da mesma forma, mas agora o código deve estar organizado em funções. Além disso, normalize que todos os nomes sejam armazenados em letras minúsculas.

# In[ ]:


# solução


# ## Analisador de texto

# Crie um programa que analise um texto fornecido pelo usuário.
# O programa deve contar o número de palavras (independentemente se há repetição ou não),
# a quantidade de cada palavra e a
# quantidade de cada letra. Ignore maiúsculas e minúsculas ao contar letras.
# Não se preocupe com pontuação e espaços ao contar palavras.
#
# O programa deve conter uma função chamada `analisar_texto` que recebe o texto
# como parâmetro e retorna a contagem de palavras, a frequência de palavras e a
# frequência de letras.
#
# Para o texto "Olá mundo! Este é um teste. Olá novamente." o programa deve
# imprimir:
#
# ```
# Contagem de palavras: 8
# Frequência de palavras: {'Olá': 2, 'mundo!': 1, 'Este': 1, 'é': 1, 'um': 1, 'teste.': 1, 'novamente.': 1}
# Frequência de letras: {'o': 4, 'l': 2, 'á': 2, 'm': 3, 'u': 2, 'n': 3, 'd': 1, '!': 1, 'e': 6, 's': 2, 't': 4, 'é': 1, '.': 2, 'v': 1, 'a': 1}
# ```
#
# **Observação**: Mais adiante no curso, aprenderemos a lidar com a pontuação.

# In[ ]:


# solução
