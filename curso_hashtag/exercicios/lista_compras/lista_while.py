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

Primeira versão da lista de compras

Escreva um programa que permita que um usuário crie uma lista de compras.
O usuário deve ser capaz de adicionar itens, remover itens e visualizar a lista.

Estruture seu programa da seguinte forma:

1. Crie uma lista vazia para armazenar os itens da lista de compras.
2. Crie um loop infinito que imprima um menu de opções ao usuário e permita que ele escolha uma opção.
3. Dentro do loop, use uma declaração if para executar a tarefa apropriada de acordo com a escolha do usuário.
4. Se o usuário escolher adicionar um item, solicite que ele digite o nome do item e adicione-o à lista.
5. Se o usuário escolher remover um item, solicite que ele digite o nome do item e remova-o da lista.
6. Se o usuário escolher ver a lista, mostre cada item da lista em sua própria linha.
7. Se o usuário escolher sair, encerre o loop usando break.

'''


lista_compras = ['agua']

while True:
    opcao = input('Escolha uma opcao:\n'
                  '1 Adicionar item\n'
                  '2 Remover item\n'
                  '3 Ver lista\n'
                  '4 Sair ')
    if opcao == '1':
        item = input('Qual item deseja adicionar a lista? ')
        lista_compras.append(item)
        print(f'{item} adicionado a lista {lista_compras}')
    elif opcao == '2':
        if lista_compras:
            print('Lista atual:', lista_compras)
            item = input('Qual item deseja remover da lista? ')
            if item in lista_compras:
                lista_compras.remove(item)
                print(f'O item "{item}" foi removido.')
            else:
                print('Item não encontrado.')
            print(lista_compras)
        else:
            print('A lista está vazia.')
    elif opcao == '3':
        for indice, item in enumerate(lista_compras):
            print(f'Na posicao {indice + 1}, temos {item}')
    elif opcao == '4':
        print('Até mais')
        break
    else:
        print('Opção inválida')
