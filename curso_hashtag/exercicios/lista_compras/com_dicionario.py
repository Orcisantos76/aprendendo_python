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

Segunda versão da lista de compras


Mude o programa de lista de compras para usar um dicionário ao invés de uma lista.
O programa deve ter as mesmas funcionalidades, mas agora deve ser possível
adicionar mais de uma unidade de um item na lista de compras. Ou seja, o dicionário
deve armazenar o nome do item e a quantidade desejada pelo usuário. Por exemplo,
se o usuário digitar "banana" e "2", o dicionário deve armazenar "banana" como chave
e 2 como valor. A estrutura do dicionário ficaria assim: `{"banana": 2}`.

O programa deve permitir que o usuário adicione, remova e visualize o dicionário de compras.

Além disso, o programa deve mostrar uma mensagem de erro se o usuário tentar
usar uma opção inválida do menu. Por exemplo, se o usuário digitar 5, o programa
deve mostrar a mensagem "Opção inválida. Por favor, escolha uma opção válida." e
mostrar o menu novamente. Além disso, o programa deve ser *case insensitive*, ou seja,
"Maçã" e "maçã" devem ser considerados o mesmo item.
'''


lista_compra_dicionario = {'agua': 1}

while True:
    opcao = input('Escolha uma opcao:\n'
                  '1 Adicionar item\n'
                  '2 Remover item\n'
                  '3 Ver lista\n'
                  '4 Sair: ')
    if opcao == '1':
        item = input('Qual item será adicionado: ')
        item = item.lower()
        quantidade = int(input(f'Quantas unidade de {item}: '))
        lista_compra_dicionario[item] = quantidade
        print(f'{quantidade} unidades de {item} adicionadas.')
    elif opcao == '2':
        print(lista_compra_dicionario)
        item = input('Qual item será removido: ')
        del lista_compra_dicionario[item]
        print(lista_compra_dicionario)
    elif opcao == '3':
        print(lista_compra_dicionario)
    elif opcao == '4':
        print('Até mais...')
        break
    else:
        print('Opção inválida.')
